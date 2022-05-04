<template>
  <q-page padding class="full-height">
    <div v-if="!loading">
      <div class="row">
        <div class="col-4"></div>
        <p class="text-h5 text-orange q-ml-sm q-mt-sm">
          Evidence Candidate Selection
        </p>
      </div>
      <div class="row">
        <div class="col-3"></div>
        <p class="q-mt-lg q-ml-xl q-pl-xl">
          (Please rate the following movies and click submit at the last step.)
        </p>
      </div>

      <div class="row">
        <q-carousel
          v-if="Object.keys(ecData).length > 0"
          v-model="slide"
          :paddding="true"
          :arrows="true"
          class="text-white row rounded-borders full-height full-width"
          style="min-height: 90vh"
        >
          <q-carousel-slide
            v-for="(ec, index) in Object.keys(evidenceCandidates)"
            :name="`ec_${index + 1}`"
            class="row full-width"
            :key="`${ec}_${index}`"
          >
            <div class="col-1"></div>
            <div class="col-6">
              <q-img
                class="q-mt-md"
                :src="ecData[ec].Poster"
                spinner-color="primary"
                spinner-size="82px"
                style="width: 500px"
              />
            </div>
            <div class="col-4">
              <q-card class="my-card q-mt-xl">
                <q-card-section>
                  <div class="text-h3">
                    {{ ecData[ec].Title }} ({{ ecData[ec].Year }})
                  </div>
                </q-card-section>
                <q-card-section align="left" class="text-grey">
                  {{ ecData[ec].Runtime }} | {{ ecData[ec].Language }} |
                  {{ ecData[ec].Director }}
                </q-card-section>
                <q-card-section style="font-size: large">
                  {{ ecData[ec].Plot }}
                </q-card-section>
                <q-card-section style="font-size: medium">
                  Genre : {{ ecData[ec].Genre }}
                </q-card-section>
                <q-card-section style="font-size: medium">
                  Rated : {{ ecData[ec].Rated }}
                </q-card-section>
                <q-card-section style="font-size: medium">
                  Actors : {{ ecData[ec].Actors }}
                </q-card-section>
                <q-card-section style="font-size: medium">
                  Imdb Rating : {{ ecData[ec].Ratings[0].Value }}
                  <q-rating
                    v-model="ecData[ec].imdbRating"
                    size="1.5em"
                    color="blue"
                    :max="10"
                    readonly
                  />
                </q-card-section>
                <q-card-section style="font-size: large">
                  Your Rating :
                  <q-rating
                    v-if="index === 0"
                    v-model="userRatings.r1"
                    size="2em"
                    color="orange"
                    :max="5"
                  />
                  <q-rating
                    v-if="index === 1"
                    v-model="userRatings.r2"
                    size="2em"
                    color="orange"
                    :max="5"
                  />
                  <q-rating
                    v-if="index === 2"
                    v-model="userRatings.r3"
                    size="2em"
                    color="orange"
                    :max="5"
                  />
                  <q-rating
                    v-if="index === 3"
                    v-model="userRatings.r4"
                    size="2em"
                    color="orange"
                    :max="5"
                  />
                  <q-rating
                    v-if="index === 4"
                    v-model="userRatings.r5"
                    size="2em"
                    color="orange"
                    :max="5"
                  />
                  <q-rating
                    v-if="index === 5"
                    v-model="userRatings.r6"
                    size="2em"
                    color="orange"
                    :max="5"
                  />
                  <q-rating
                    v-if="index === 6"
                    v-model="userRatings.r7"
                    size="2em"
                    color="orange"
                    :max="5"
                  />
                  <q-rating
                    v-if="index === 7"
                    v-model="userRatings.r8"
                    size="2em"
                    color="orange"
                    :max="5"
                  />
                  <q-rating
                    v-if="index === 8"
                    v-model="userRatings.r9"
                    size="2em"
                    color="orange"
                    :max="5"
                  />
                  <q-rating
                    v-if="index === 9"
                    v-model="userRatings.r10"
                    size="2em"
                    color="orange"
                    :max="5"
                  />
                </q-card-section>
                <q-card-section> </q-card-section>
                <q-card-actions
                  align="right"
                  v-if="index === Object.keys(ecData).length - 1"
                >
                  <q-btn
                    color="primary"
                    label="Get Recommendations"
                    @click="getRecommendations()"
                    class="q-mr-xl"
                  />
                </q-card-actions>
              </q-card>
            </div>
          </q-carousel-slide>
        </q-carousel>
      </div>
    </div>
    <div v-else>
      <q-inner-loading
        :showing="loading"
        label="Please wait while we get the evidence candidates for you..."
        label-class="text-white"
        label-style="font-size: 1.1em"
      />
    </div>
  </q-page>
</template>

<script>
import { defineComponent, ref } from "vue";
import axios from "axios";

export default defineComponent({
  name: "EvidenceCandidatesPage",
  data() {
    return {
      loading: true,
      apiUrl: "",
      evidenceCandidates: {
        Sleeper: 0.6,
        "City Hall": 0.7,
        Heat: 0.6,
        "Toy Story": 0.4,
        "Forrest Gump": 0.3,
      },
      ecData: {},
      userRatings: {
        r1: 0,
        r2: 0,
        r3: 0,
        r4: 0,
        r5: 0,
        r6: 0,
        r7: 0,
        r8: 0,
        r8: 0,
        r10: 0,
      },
      omdbUrl: "https://www.omdbapi.com/?apikey=3ffbd3cb&t=",
      movieName: "City Hall",
      slide: ref("ec_1"),
    };
  },
  methods: {
    getRecommendations() {
      this.$router.push("/explore");
    },
    async setLoading() {
      const self = this;
      console.log(this.loading);
      setTimeout(function () {
        self.loading = false;
      }, 3000);
    },
  },
  async created() {
    for (const ec of Object.keys(this.evidenceCandidates)) {
      const res = await axios.get(this.omdbUrl + ec);
      this.ecData[ec] = res.data;
      this.ecData[ec].imdbRating = Number(
        this.ecData[ec].Ratings[0].Value.split("/")[0]
      );
    }
    await this.setLoading();
  },
});
</script>
<style>
.q-carousel__slides-container {
  width: 100% !important;
}
</style>
