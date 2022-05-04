<template>
  <q-page padding class="q-ml-sm" v-if="!loading">
    <div class="row">
      <p class="text-h3 text-orange q-ml-sm q-mt-sm">Top Picks</p>
      <p class="q-mt-lg q-ml-sm">
        (Recommendations based on your ratings from evidence candidates)
      </p>
    </div>
    <div class="row full-height">
      <template v-for="(movie, index) in Object.keys(movies)" :key="index">
        <MovieTile
          :title="movie"
          :rating="movies[movie]"
          class="q-pa-sm"
        ></MovieTile>
      </template>
    </div>
  </q-page>
  <q-inner-loading
    :showing="loading"
    label="Please wait while we recommend the best movies for you..."
    label-class="text-white"
    label-style="font-size: 1.1em"
  />
</template>

<script>
import { defineComponent } from "vue";
import MovieTile from "src/components/MovieTile.vue";

export default defineComponent({
  name: "ExplorePage",
  components: {
    MovieTile,
  },
  data() {
    return {
      movies: {
        "Simon Sez": 0.7,
        "Down Periscope": 0.7,
        "Hot Shots! Part Deux": 0.7,
        "Drunken Master": 0.8,
        "The Man in the Iron Mask": 0.6,
        "Mr. Wrong": 0.6,
        "Conquest of the Planet of the Apes": 0.4,
        "Bird on a Wire": 0.5,
        "Last Resort": 0.4,
        "Logan's Run": 0.5,
        "Denise Calls Up": 0.4,
        "Beverly Hills Ninja": 0.5,
        "The Brady Bunch Movie": 0.6,
        "She-Devil": 0.6,
        "Street Fighter": 0.4,
        "National Lampoon's Christmas Vacation": 0.3,
      },
      loading: true,
    };
  },
  async created() {
    if (this.movies.length === 0) {
      this.loading = false;
    }
    await this.setLoading();
  },
  watch: {
    movies(newValue, oldValue) {
      newValue.length > 0 ? (this.loading = false) : (this.loading = true);
    },
  },
  methods: {
    async setLoading() {
      const self = this;
      console.log(this.loading);
      setTimeout(function () {
        self.loading = false;
      }, 3000);
    },
  },
});
</script>
