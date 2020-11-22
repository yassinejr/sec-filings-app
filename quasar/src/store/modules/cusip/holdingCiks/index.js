import Vue from "vue";

const state = {
  data: [],
  columns: [
    {
      name: "cik_number",
      align: "left",
      label: "CIK Number",
      field: "cik_number",
      sortable: true
    },
    {
      name: "filer_name",
      align: "left",
      label: "Filer Name",
      field: "filer_name",
      sortable: true
    },
    {
      name: "total_value",
      align: "left",
      label: "Total Value",
      field: "total_value",
      sortable: true
    },
    {
      name: "total_shares",
      align: "left",
      label: "Total Shares",
      field: "total_shares",
      sortable: true
    },
    {
      name: "first_filed",
      align: "left",
      label: "First Filed",
      field: "first_filed",
      sortable: true
    },
    {
      name: "percent_of_portfolio",
      align: "left",
      label: "Percent of Portfolio",
      field: "percent_of_portfolio",
      sortable: true
    }
  ]
};

const getters = {
  getData: s => s.data,
  getColumns: s => s.columns
};

const actions = {
  fetchData: ({ commit, rootGetters }, payload) => {
    const { cusip } = payload;
    const period = rootGetters["core/getPeriod"].value;
    Vue.prototype.$axios
      .get(`/api/cusip/${cusip}/cik/${period}/`)
      .then(resp => {
        commit("setData", resp.data);
      });
  }
};

const mutations = {
  setData: (state, payload) => {
    state.data = payload;
  }
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
};
