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
          v-model="textBeforeConversion"
          maxlength="200"
          show-word-limit
        >
        </el-input>

        <el-button
          type="primary"
          plain
          :disabled="wordSegmentationStatus == 'loading'"
          @click="getWordSegmentationResult"
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
import { ref } from "vue";

export default {
  name: "App",
  components: {
    Footer,
    WordSegmentationBox,
  },
  setup() {
    const textBeforeConversion = ref("");
    const wordSegmentationStatus = ref("empty");
    const wordSegmentationResults = ref([]);

    const getWordSegmentationResult = () => {
      wordSegmentationStatus.value = "loading";
      setTimeout(() => {
        wordSegmentationStatus.value = "ready";
        wordSegmentationResults.value = textBeforeConversion.value.split("");
      }, 1000);
    };

    return {
      textBeforeConversion,
      wordSegmentationStatus,
      wordSegmentationResults,
      getWordSegmentationResult,
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
  font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB",
    "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
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
