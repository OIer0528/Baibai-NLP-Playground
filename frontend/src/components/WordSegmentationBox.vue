<template>
  <div class="word-segmentation-box">
    <div v-if="status == 'empty'">
      <!-- empty -->
    </div>
    <div v-else-if="status == 'loading'">
      <p><i class="el-icon-loading"></i> 正在获取分词结果...</p>
    </div>
    <div v-else-if="status == 'error'">
      <p><i class="el-icon-error"></i> 获取分词结果失败！请稍后重试！</p>
    </div>
    <div v-else>
      <div class="desc">分词结果</div>
      <div class="results-box">
        <template v-for="word in results" :key="word">
          <span class="word">{{ word }}</span>
        </template>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "WordSegmentationBox",
  props: ["status", "results"],
};
</script>

<style scoped>
.word-segmentation-box {
  margin-top: 1rem;
}

.results-box {
  display: flex;
  flex-wrap: wrap;
  min-height: 5rem;
  border: solid rgb(233, 233, 233) 1px;
  border-radius: calc(1rem / 4);
}

.desc {
  margin-bottom: 0.5rem;
  border-radius: 0.5rem;
  width: 70%;
  margin-left: 15%;
  margin-right: 15%;
  font-size: 1.2rem;
  font-weight: bold;
}

.word {
  border: solid rgb(179, 216, 255) 1px;
  background-color: rgb(237, 246, 255);
  padding: 0.1rem;
  margin: 0.2rem 0.5rem;
  height: 1.4rem;
  min-width: 1rem;
}

.word:hover {
  background-color: rgb(179, 216, 255);
}
</style>