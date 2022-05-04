<template>
  <q-layout view="hHh lpR fFf">
    <q-header elevated class="bg-primary text-white">
      <q-toolbar class="bg-black text-white">
        <q-toolbar-title class="q-ml-md" @click="home()">
          PriMeLU Recommendations
        </q-toolbar-title>
        <q-btn flat @click="home()" label="Home" />
        <q-btn
          flat
          class="q-mr-xl q-pr-xl"
          @click="aboutUs()"
          label="About Us"
        />
      </q-toolbar>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>
<script>
export default {
  data() {
    return {};
  },
  methods: {
    home() {
      this.$router.push("/explore");
    },
    aboutUs() {
      this.$router.push("/about");
    },
  },
};
</script>
