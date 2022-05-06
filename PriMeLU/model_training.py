import os
import torch
import pickle
import random

from PriMeLU import PriMeLU
from options import config, states


def training(primelu, total_dataset, batch_size, num_epoch, model_save=True, model_filename=None):
    if config['use_cuda']:
        primelu.cuda()

    training_set_size = len(total_dataset)
    primelu.train()
    for _ in range(num_epoch):
        random.shuffle(total_dataset)
        num_batch = int(training_set_size / batch_size)
        a,b,c,d = zip(*total_dataset)
        for i in range(num_batch):
            try:
                supp_xs = list(a[batch_size*i:batch_size*(i+1)])
                supp_ys = list(b[batch_size*i:batch_size*(i+1)])
                query_xs = list(c[batch_size*i:batch_size*(i+1)])
                query_ys = list(d[batch_size*i:batch_size*(i+1)])
            except IndexError:
                continue
            primelu.global_update(supp_xs, supp_ys, query_xs, query_ys, config['inner'])

    if model_save:
        torch.save(primelu.state_dict(), model_filename)
