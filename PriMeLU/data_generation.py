import re
import os
import json
import torch
import numpy as np
import random
import pickle
from tqdm import tqdm

from options import states
from dataset import movielens_1m


def item_converting(row, rate_list, genre_list, director_list, actor_list):
    rate_idx = torch.tensor([[rate_list.index(str(row['rate']))]]).long()
    genre_idx = torch.zeros(1, 25).long()
    for genre in str(row['genre']).split(", "):
        idx = genre_list.index(genre)
        genre_idx[0, idx] = 1
    director_idx = torch.zeros(1, 2186).long()
    for director in str(row['director']).split(", "):
        idx = director_list.index(re.sub(r'\([^()]*\)', '', director))
        director_idx[0, idx] = 1
    actor_idx = torch.zeros(1, 8030).long()
    for actor in str(row['actors']).split(", "):
        idx = actor_list.index(actor)
        actor_idx[0, idx] = 1
    return torch.cat((rate_idx, genre_idx, director_idx, actor_idx), 1)


def load_list(fname):
    list_ = []
    with open(fname, encoding="utf-8") as f:
        for line in f.readlines():
            list_.append(line.strip())
    return list_


def generate(master_path):
    dataset_path = "movielens/ml-1m"
    rate_list = load_list("{}/m_rate.txt".format(dataset_path))
    genre_list = load_list("{}/m_genre.txt".format(dataset_path))
    actor_list = load_list("{}/m_actor.txt".format(dataset_path))
    director_list = load_list("{}/m_director.txt".format(dataset_path))

    if not os.path.exists("{}/warm_state/".format(master_path)):
        for state in states:
            os.mkdir("{}/{}/".format(master_path, state))
    if not os.path.exists("{}/log/".format(master_path)):
        os.mkdir("{}/log/".format(master_path))

    dataset = movielens_1m()

    # hashmap for item information
    if not os.path.exists("{}/m_movie_dict.pkl".format(master_path)):
        movie_dict = {}
        for idx, row in dataset.item_data.iterrows():
            m_info = item_converting(row, rate_list, genre_list, director_list, actor_list)
            movie_dict[row['movie_id']] = m_info
        pickle.dump(movie_dict, open("{}/m_movie_dict.pkl".format(master_path), "wb"))
    else:
        movie_dict = pickle.load(open("{}/m_movie_dict.pkl".format(master_path), "rb"))

    for state in states:
        idx = 0
        if not os.path.exists("{}/{}/{}".format(master_path, "log", state)):
            os.mkdir("{}/{}/{}".format(master_path, "log", state))
        with open("{}/{}.json".format(dataset_path, state), encoding="utf-8") as f:
            dataset = json.loads(f.read())
        with open("{}/{}_y.json".format(dataset_path, state), encoding="utf-8") as f:
            dataset_y = json.loads(f.read())
        for _, user_id in tqdm(enumerate(dataset.keys())):
            u_id = int(user_id)
            seen_movie_len = len(dataset[str(u_id)])
            indices = list(range(seen_movie_len))

            if seen_movie_len < 13 or seen_movie_len > 100:
                continue

            random.shuffle(indices)
            tmp_x = np.array(dataset[str(u_id)])
            tmp_y = np.array(dataset_y[str(u_id)])

            support_x_app = None
            for m_id in tmp_x[indices[:-10]]:
                m_id = int(m_id)
                tmp_x_converted = movie_dict[m_id]
                try:
                    support_x_app = torch.cat((support_x_app, tmp_x_converted), 0)
                except:
                    support_x_app = tmp_x_converted

            query_x_app = None
            for m_id in tmp_x[indices[-10:]]:
                m_id = int(m_id)
                u_id = int(user_id)
                tmp_x_converted = movie_dict[m_id]
                try:
                    query_x_app = torch.cat((query_x_app, tmp_x_converted), 0)
                except:
                    query_x_app = tmp_x_converted
            support_y_app = torch.FloatTensor(tmp_y[indices[:-10]])
            query_y_app = torch.FloatTensor(tmp_y[indices[-10:]])

            pickle.dump(support_x_app, open("{}/{}/supp_x_{}.pkl".format(master_path, state, idx), "wb"))
            pickle.dump(support_y_app, open("{}/{}/supp_y_{}.pkl".format(master_path, state, idx), "wb"))
            pickle.dump(query_x_app, open("{}/{}/query_x_{}.pkl".format(master_path, state, idx), "wb"))
            pickle.dump(query_y_app, open("{}/{}/query_y_{}.pkl".format(master_path, state, idx), "wb"))
            with open("{}/log/{}/supp_x_{}_u_m_ids.txt".format(master_path, state, idx), "w") as f:
                for m_id in tmp_x[indices[:-10]]:
                    f.write("{}\t{}\n".format(u_id, m_id))
            with open("{}/log/{}/query_x_{}_u_m_ids.txt".format(master_path, state, idx), "w") as f:
                for m_id in tmp_x[indices[-10:]]:
                    f.write("{}\t{}\n".format(u_id, m_id))
            idx += 1