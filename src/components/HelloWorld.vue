<template>
  <div class="body-wrapper">
    <div class="grid-container">
      <div class="headline">A long time ago, I used to take a lot of photos. Here they are, in no particular order.</div>
      <h1 class="P">P</h1>
      <h1 class="I">I</h1>
      <h1 class="C">C</h1>
      <h1 class="S">S</h1>
    </div>
<!--     <h1 class="is-pulled-left">P&nbsp;&nbsp;I<br>C S</h1>
    <p style="text-align: right">
      A long time ago, I used to take a lot of photos. Here they are, in no particular order.
    </p>
-->
    <agile>
      <div v-for="pic in pics" v-bind:key="pic.basename" @click="pic.showInfo = !pic.showInfo" class="slide">
        <img v-lazy="pic.url"/>
      </div>
    </agile>
  </div>
</template>

<script>
  import pics_data from '@/assets/images.json'
  import { VueAgile } from 'vue-agile'

  for (let i=0; i < pics_data['pics'].length; i++) {
    pics_data['pics'][i]['url'] = require('@/assets/images/' + pics_data['pics'][i]['basename'])
    pics_data['pics'][i]['showInfo'] = false
  }

  export default {
    name: 'HelloWorld',
    props: {
      msg: String
    },
    components: {
        agile: VueAgile
    },
    data: function() {
      return {
        pics: pics_data['pics']
      }
    },

  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  body {
    background: darkgrey;
  }
  h3 {
    margin: 40px 0 0;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  a {
    color: #42b983;
  }
  .is-pulled-left {
    text-align: left;
    font-size: 2.5em;
  }
  .body-wrapper {
    margin: 50px;
  }
  .flex-center {
    align-items: center;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
  }
  .wrapper {
    flex-wrap: wrap;
  }
  .wrapper .pic-frame {
    margin-bottom: 10px;
    width: 80%;
    position: relative;
  }
  .pic-frame img {
    width: 100%;
  }
  .wrapper .pic-frame .overlay {
    background: rgba(255, 255, 255, 0.7);
    display: flex;
    height: 100%;
    position: absolute;
    width: 100%;
    justify-content: center;
    align-items: center;
  }
  .fade-enter-active, .fade-leave-active {
    transition: opacity .5s;
  }
  .fade-enter, .fade-leave-to {
    opacity: 0;
  }

  .grid-container {
    display: grid;
    grid-template-columns: 50px 50px auto auto;
    grid-template-rows: 0.9fr 1.1fr;
    gap: 1px 1px;
    grid-template-areas: "P I Headline Headline" "C S Headline Headline";
  }

  .headline { grid-area: Headline; text-align: right;}

  .P { grid-area: P; margin: 0px; }

  .I { grid-area: I; margin: 0px; }

  .C { grid-area: C; margin: 0px; }

  .S { grid-area: S; margin: 0px; }
</style>

<style type="text/css">
  .agile__slides {
    align-items: stretch;
  }

  .agile__dot {
    margin: 0 10px;
  }

  .agile__dot--current button, .agile__dot:hover button {
    background-color: #888;
  }

  .agile__dot button {
    background-color: #eee;
    border: none;
    border-radius: 50%;
    cursor: pointer;
    display: block;
    height: 10px;
    font-size: 0;
    line-height: 0;
    margin: 0;
    padding: 0;
    transition-duration: .3s;
    width: 10px;
  }
</style>
