<template>
  <div>
    <el-container>
      <el-header>
        <h1>佰佰的 NLP 游乐场</h1>
      </el-header>
      <el-footer><Footer /></el-footer>
    </el-container>
  </div>
</template>

<script>
import Footer from "./components/Footer.vue";

export default {
  name: "App",
  components: {
    Footer,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* margin-top: 60px; */
}

body {
  margin: 0px;
}

#app .el-header {
  background: rgb(83, 168, 255);
  color: #ffffff;
}

#app .el-footer {
  background: rgb(179, 216, 255);
  position: fixed;
  width: 100%;
  bottom: 0;
}
</style>
