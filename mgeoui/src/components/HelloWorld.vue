<script setup lang="ts">
import {ref} from 'vue'
import axios from 'axios'

 

const text = ref('浙江杭州市江干区九堡镇三村村一区')
const prov = ref('')
const city = ref('')
const district = ref('')
const town = ref('')
const community = ref('')
const poi = ref('')

const send = (address: string)=>{
  console.log(address)

  // fetch('/mgeo/address?name='+address).then(res=>{
  //   console.log('Response',res)
  // })
  axios.get('http://localhost:20002/address',{
    params:{
      name: address
    }
  }).then(res=>{
    console.log('Response',res)
    res.data.map( (d: any) =>{
       switch(d.type){
          case "prov":
          prov.value = d.span;
          break;
          case "city":
          city.value = d.span;
          break;        
          case "district":
          district.value = d.span;
          break;
          case "town":
          town.value = d.span;
          break;
          case "community":
          community.value = d.span;
          break;
          case "poi":
          poi.value = d.span;
          break;
       }
    })

  })
}

</script>

<template>
  <div class="greetings" style="width:100%">
    <h1 class="green">地址标准化</h1>
    <el-card class="box-card">
      <template #header>
        <div class="card-header">
          <span>请输入地址：</span> 
        </div>
      </template>
      <el-input v-model="text" type="textarea"/>
      <template #footer>
        <div class="card-footer">
          <el-button type="primary" @click="send(text)">执行</el-button>
        </div>
      </template>
    </el-card>
   
    <el-card class="box-card">
      <template #header>
        <div class="card-header">
          <span>分析结果：</span> 
        </div>
      </template> 
        <span>省</span>
        <el-input v-model="prov"/>
        <span>市</span>
        <el-input v-model="city"/>
        <span>区</span>
        <el-input v-model="district"/>
        <span>镇</span>
        <el-input v-model="town"/>
        <span>村</span>
        <el-input v-model="community"/>
        <span>详细地址</span>
        <el-input v-model="poi"/> 
    </el-card>
  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.card-footer {
  display: flex;
  flex-direction: row-reverse;
  justify-content: space-between;
  align-items: center;
}

.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}


</style>
