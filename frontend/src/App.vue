<template>
  <div>
    <el-container>
      <el-header>
        <h1>佰佰的 NLP 游乐场</h1>
      </el-header>
      <el-main>
        <el-input
          type="textarea"
          placeholder="请输入内容"
          v-model="text"
          maxlength="200"
          show-word-limit
        >
        </el-input>

        <el-button
          type="primary"
          plain
          :disabled="wordSegmentationStatus == 'loading'"
          @click="getWordSegmentationResults"
        >
          显示分词结果
        </el-button>
        <el-button type="primary" plain>显示词性标注结果</el-button>
        <word-segmentation-box
          :status="wordSegmentationStatus"
          :results="wordSegmentationResults"
        />
      </el-main>
      <el-footer><Footer /></el-footer>
    </el-container>
  </div>
</template>

<script>
import Footer from "./components/Footer.vue";
import WordSegmentationBox from "./components/WordSegmentationBox.vue";
import axios from "axios";
import { ref } from "vue";

export default {
  name: "App",
  components: {
    Footer,
    WordSegmentationBox,
  },
  setup() {
    const text = ref("");
    const wordSegmentationStatus = ref("empty");
    const wordSegmentationResults = ref([]);

    const getWordSegmentationResults = () => {
      wordSegmentationStatus.value = "loading";
      axios
        .get("/api/getWordSegmentationResults", { params: { text: text.value } })
        .then((response) => {
          wordSegmentationStatus.value = "ready";
          wordSegmentationResults.value = response.data.results;
        })
        .catch((error) => {
          console.log(error);
          wordSegmentationStatus.value = "error";
        });
    };

    return {
      text,
      wordSegmentationStatus,
      wordSegmentationResults,
      getWordSegmentationResults,
    };
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

#app .el-main .el-textarea {
  margin-bottom: 1rem;
  font-size: 1.2rem;
  word-break: break-all;
}

#app .el-footer {
  background: rgb(179, 216, 255);
  position: fixed;
  width: 100%;
  bottom: 0;
}
</style>
