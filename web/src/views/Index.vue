<template>
  <h1>NLP之成语推荐</h1>
  <div>
    <InputText type="text" v-model="sentence" placeholder="句子(包含[MASK])" style="width: 20rem; margin: 0 1rem 1rem 0rem" />&nbsp;
    <InputText type="text" v-model="candidates" placeholder="候选成语(用,分隔)" style="width: 20rem; margin: 0 1rem 1rem 0rem" />&nbsp;
    <Button label="默认" icon="pi pi-home" class="p-button-warning" style="margin: 0 1rem 1rem 0rem" @click="defvalue"></Button>&nbsp;
    <Button label="推荐" icon="pi pi-send" style="margin: 0 1rem 1rem 0rem" @click="fillin"></Button>
    <Message v-show="result" class="message" severity="success" :closable="false">{{ result }}</Message>
  </div>
</template>

<script>
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';
import Message from 'primevue/message';

export default {
  data() {
    return {
      sentence: null,
      candidates: null,
      result: null
    }
  },
  methods: {
    defvalue() {
      this.sentence = '今天的天气[MASK]';
      this.candidates = '乘风破浪,万里无云,落花流水,天网恢恢'
    },
    fillin() {
      if(!this.sentence || !this.candidates) {
        return;
      }
      fetch(`/bert/?ctx=${ encodeURI(this.sentence) }&candidates=${ encodeURI(this.candidates) }`, {
        method: 'GET'
      }).then((res) => {
        console.log(res);
        if(res.status === 200) {
          res.text().then((value) => {
            this.result = value;
          });
        }
      }).catch((err) => {
        console.error(err);
      });
    }
  },
  components: {
    InputText, Button, Message
  }
};

</script>
<style>
@media screen and (min-width: 300px) {
  .message {
    margin: 0 auto;
  }
}

@media screen and (min-width: 400px) and (max-width: 1200px) {
  .message {
    margin: 0 1rem auto 1rem;
  }
}

@media screen and (min-width: 1200px) and (max-width: 1400px) {
  .message {
    margin: 0 10rem auto 10rem;
  }
}

@media screen and (min-width: 1400px) and (max-width: 1600px) {
  .message {
    margin: 0 20rem auto 20rem;
  }
}

@media screen and (min-width: 1600px) {
  .message {
    margin: 0 35rem auto 35rem;
  }
}
</style>