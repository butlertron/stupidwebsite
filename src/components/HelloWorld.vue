<template>
  <div class="body-wrapper">
    <h1 class="is-pulled-left">P&nbsp;&nbsp;I<br>C S</h1>
    <p style="text-align: right">
      A long time ago, I used to take a lot of photos. Here they are, in no particular order.
    </p>
    <div v-for="pic in pics" v-bind:key="pic.basename">
      <img v-bind:src="pic.url" class="pic-frame"/>
    </div>
  </div>
</template>

<script>
  import pics_data from '../assets/images.json'
  for (let i=0; i < pics_data['pics'].length; i++) {
    pics_data['pics'][i]['url'] = require('../assets/images/' + pics_data['pics'][i]['basename'])
  }

  export default {
    name: 'HelloWorld',
    props: {
      msg: String
    },
    data: function() {
      return {
        pics: pics_data['pics']
      }
    }
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
  .pic-frame {
    width: 80%;
  }
</style>
