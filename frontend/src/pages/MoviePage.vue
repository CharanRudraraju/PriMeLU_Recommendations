<template>
  <q-page padding class="full-height">
    <div
      class="row full-height"
      style="min-height: 90vh"
      v-if="Object.keys(movieData).length > 0"
    >
      <div class="col-1"></div>
      <div class="col-6">
        <q-img
          class="q-mt-md"
          :src="movieData.Poster"
          spinner-color="primary"
          spinner-size="82px"
          style="width: 500px"
        />
      </div>
      <div class="col-5">
        <q-card class="my-card q-mt-xl">
          <q-card-section>
            <div class="text-h3">
              {{ movieData.Title }} ({{ movieData.Year }})
            </div>
          </q-card-section>
          <q-card-section align="left" class="text-grey">
            {{ movieData.Runtime }} | {{ movieData.Language }} |
            {{ movieData.Director }}
          </q-card-section>
          <q-card-section style="font-size: large">
            {{ movieData.Plot }}
          </q-card-section>
          <q-card-section style="font-size: medium">
            Genre : {{ movieData.Genre }}
          </q-card-section>
          <q-card-section style="font-size: medium">
            Rated : {{ movieData.Rated }}
          </q-card-section>
          <q-card-section style="font-size: medium">
            Box Office : {{ movieData.BoxOffice }}
          </q-card-section>
          <q-card-section style="font-size: medium">
            Awards : {{ movieData.Awards }}
          </q-card-section>
          <q-card-section style="font-size: medium">
            Imdb Rating : {{ movieData.Ratings[0].Value }}
            <q-rating
              v-model="imdbRating"
              size="1.5em"
              color="blue"
              :max="10"
              readonly
            />
          </q-card-section>
          <q-card-section style="font-size: medium">
            Rotten Tomatoes Rating : {{ movieData.Ratings[1].Value }}
            <q-rating
              v-model="rtRating"
              size="1.5em"
              color="blue"
              :max="10"
              readonly
            />
          </q-card-section>
          <q-card-section style="font-size: medium">
            Actors : {{ movieData.Actors }}
          </q-card-section>
        </q-card>
      </div>
    </div>
  </q-page>
</template>

<script>
import { defineComponent, ref } from "vue";
import axios from "axios";

export default defineComponent({
  name: "MoviePage",
  props: {
    data: Object,
  },
  data() {
    return {
      movieId: "",
      omdbUrl: "https://www.omdbapi.com/?apikey=3ffbd3cb&t=",
      movieName: "City Hall",
      movieData: {},
      imdbRating: "",
      rtRating: "",
      title: "",
    };
  },
  async created() {
    this.title = this.$route.params.title;
    console.log(this.title);
    const { data } = await axios.get(this.omdbUrl + this.title);
    this.movieData = data;
    this.imdbRating = Number(this.movieData.Ratings[0].Value.split("/")[0]);
    this.rtRating =
      Number(this.movieData.Ratings[1].Value.replace("%", "")) / 10;
  },
});
</script>
