<template>
  <q-page>
    <div class="row" style="background-color: #f06624; min-height: 40vh">
      <div class="col-4"></div>
      <div class="col-6">
        <q-card
          flat
          style="background-color: #f06624"
          class="my-card q-mt-xl q-pt-xl"
        >
          <q-card-section class="q-mt-xl">
            <div class="text-h3">PriMeLU Recommendations</div>
          </q-card-section>
          <q-card-section>
            <div class="text-h5">
              Meta-Learning based Personalized Movie Recommendations
            </div>
          </q-card-section>
          <q-card-section>
            <div class="q-ml-xl q-pl-xl">
              <q-btn
                color="primary"
                label="Get Started"
                @click="getStarted()"
              />
              <span class="q-ml-xl q-pl-xl"></span>
              <q-btn color="primary" label="About Us" @click="aboutUs()" />
            </div>
          </q-card-section>
        </q-card>
      </div>
    </div>
    <div class="row text-black" style="background-color: white; height: 60vh">
      <div class="row full-width">
        <div class="col-3"></div>
        <div class="col-3">
          <h2 class="section-header">recommendations</h2>
          <p>
            PriMeLU helps you find movies you will like. Rate movies(evidence
            candidates) to build a custom taste profile, then PriMeLU recommends
            other movies for you to watch.
          </p>
        </div>
        <div class="col-5 q-ml-xl q-pl-xl q-mt-xl">
          <img
            style="max-width: 40vh"
            src="../assets/recommendations.jpg"
            class="img-responsive marketing-img"
          />
        </div>
      </div>
      <div class="row full-width">
        <div class="col-3"></div>
        <div class="col-3">
          <h2 class="section-header">movie info</h2>
          <p>
            PriMeLU helps you get information of the movie selected like genre,
            directors, rating etc.
          </p>
        </div>
        <div class="col-5 q-ml-xl q-pl-xl q-mt-xl">
          <img
            style="max-width: 40vh"
            src="../assets/movies.jpg"
            class="img-responsive marketing-img"
          />
        </div>
      </div>
    </div>
  </q-page>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "IndexPage",
  methods: {
    getStarted() {
      this.$router.push("/evidence-candidates");
    },
    aboutUs() {
      this.$router.push("/about");
    },
  },
});
</script>
