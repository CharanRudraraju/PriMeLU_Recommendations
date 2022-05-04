const routes = [
  {
    path: "/",
    component: () => import("layouts/HomeLayout.vue"),
    children: [{ path: "", component: () => import("pages/IndexPage.vue") }],
  },
  {
    path: "/evidence-candidates",
    component: () => import("layouts/MainLayout.vue"),
    children: [
      {
        path: "",
        component: () => import("pages/EvidenceCandidatesPage.vue"),
        prop: true,
      },
    ],
  },
  {
    path: "/explore",
    component: () => import("layouts/MainLayout.vue"),
    children: [{ path: "", component: () => import("pages/ExplorePage.vue") }],
    props: true,
  },
  {
    name: "movie",
    path: "/movie/:title",
    component: () => import("layouts/MainLayout.vue"),
    children: [
      { path: "", component: () => import("pages/MoviePage.vue"), props: true },
    ],
    props: true,
  },
  {
    path: "/about",
    component: () => import("layouts/MainLayout.vue"),
    children: [{ path: "", component: () => import("pages/AboutUs.vue") }],
    props: true,
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: "/:catchAll(.*)*",
    component: () => import("pages/ErrorNotFound.vue"),
  },
];

export default routes;
