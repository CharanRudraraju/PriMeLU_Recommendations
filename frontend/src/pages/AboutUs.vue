<template>
  <q-page padding class="full-height">
    <div style="height: 10vh"></div>
    <div class="row full-height" style="min-height: 90vh">
      <div class="col-1"></div>
      <div class="col-6">
        <q-img
          class="q-mt-md"
          src="../assets/eureka_nova.jpg"
          spinner-color="primary"
          spinner-size="82px"
          style="width: 500px"
        />
      </div>
      <div class="col-5">
        <q-card class="my-card q-mt-xl">
          <q-card-section>
            <div class="text-h3">Charan Kumar Raju RUDRARAJU</div>
          </q-card-section>
          <q-card-section
            align="left"
            class="text-grey"
            style="font-size: 16px"
          >
            charanrudraraju123@gmail.com | crudraraj2-c@my.cityu.edu.hk
          </q-card-section>
          <q-card-section style="font-size: large"> Year : 4 </q-card-section>
          <q-card-section style="font-size: large">
            Major : BSc Computer Science
          </q-card-section>
          <q-card-section style="font-size: large">
            Stream : Artificial Intelligence | Data Science
          </q-card-section>
          <q-card-section style="font-size: large">
            Skills : Javascript | Angular | Vue | Python | C#
          </q-card-section>
          <q-card-section style="font-size: large">
            Profile : A Passionate developer with a focus on bringing ideas to
            reality and solving real world problems.
          </q-card-section>
          <q-card-section style="font-size: large">
            Github :
            <a href="https://github.com/CharanRudraraju"> CharanRudraraju</a>
          </q-card-section>
          <q-card-section style="font-size: large">
            LinkedIn :
            <a href="https://linkedin.com/in/charan-kumar-raju-rudraraju">
              Charan Kumar Raju Rudraraju</a
            >
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
    return {};
  },
});
</script>
