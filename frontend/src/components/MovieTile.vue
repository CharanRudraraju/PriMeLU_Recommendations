<template>
  <div v-if="movieData !== undefined">
    <div class="container" style="width: 300px; height: 700px">
      <q-card
        class="my-card"
        clickable
        style="cursor: pointer"
        @click="setMovieData()"
      >
        <img :src="movieData.Poster" />
        <q-card-section>
          <div class="text-h6">{{ movieData.Title }}</div>
          <div class="text-subtitle2 text-grey">
            <q-scroll-area style="width: 300px; height: 50px">
              {{ movieData.Year }} | {{ movieData.Runtime }} |
              {{ movieData.Language }} |
              {{ movieData.Director }}
            </q-scroll-area>
          </div>
        </q-card-section>
        <q-card-section style="overflow-wrap: break-word">
          <q-scroll-area style="width: 300px; height: 50px">
            {{ movieData.Plot }}
          </q-scroll-area>
        </q-card-section>
        <q-card-section>
          <q-rating v-model="movieRating" size="1.5em" color="orange" />
        </q-card-section>
      </q-card>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import axios from "axios";

export default defineComponent({
  name: "MovieTile",
  props: {
    title: String,
    rating: Number,
  },
  data() {
    return {
      movieData: {},
      movieRating: Number(this.rating),
      omdbUrl: "https://www.omdbapi.com/?apikey=3ffbd3cb&t=",
    };
  },
  async created() {
    if (Object.keys(this.movieData).length === 0) {
      const { data } = await axios.get(this.omdbUrl + this.title);
      this.movieData = data;
      console.log(this.movieData);
    }
  },
  computed: {
    data() {
      return this.movieData;
    },
  },
  methods: {
    setMovieData() {
      const data = this.data;
      this.$router.push("/movie/" + this.title);
    },
  },
});
</script>
