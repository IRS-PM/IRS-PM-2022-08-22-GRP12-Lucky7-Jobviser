<template>
  <v-app>
    <!--姓名 抬头-->
    <v-card
      class="fixCard"
    >
      <v-toolbar color=#f3f7e4 shaped>
        <v-toolbar-title>{{ "\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0" }}Hello {{nameID}}  ^^</v-toolbar-title>
        <v-spacer></v-spacer>
      </v-toolbar>
      <v-banner single-line :sticky="sticky">
        Please check your Ideal job and Suitable Job, and the comparison between them.
      </v-banner>
      <!-- <v-card-text class="grey lighten-4">
        <v-sheet class="mx-auto"></v-sheet>
      </v-card-text> -->
    </v-card>
    <h1><br><br><br></h1>
    <v-expansion-panels
        v-model='active_question'
        focusable
        hover
    >
      <template>
        <v-stepper
          non-linear
          v-model="e1">
          <v-stepper-header>
            <v-stepper-step
              editable
              step="1"
              color=#306385
            >
              Your Information
            </v-stepper-step>
            <v-divider></v-divider>
            <v-stepper-step
              editable
              step="2"
              color=#306385
            >
              Ideal Job
            </v-stepper-step>
            <v-divider></v-divider>
            <v-stepper-step
              editable
              step="3"
              color=#306385
            >
              Suitable Job
            </v-stepper-step>
            <v-divider></v-divider>
            <v-stepper-step
              editable
              step="4"
              color=#306385
            >
              Offical Webset
            </v-stepper-step>
          </v-stepper-header>

          <v-stepper-items>
            <v-stepper-content step="1">
              <v-card
                class="mb-12"
                color=#cddbdd
                height="350px"
                max-width="600px"
              ><br>
              Hello {{nameID}}, your age is {{systemTime-parseInt(question1)}},<br>
              your ideal working place is at {{q2[parseInt(question2)-1]}},<br>
              you want a {{q3[parseInt(question3)]}},<br>
              you wnat to {{q4[parseInt(question4)]}},<br>
              you {{q5[parseInt(question5)]}} work experience in related industries,<br>
              your highest education level is {{q6[parseInt(question6)]}},<br>
              your major is {{q7[parseInt(question7)]}}.<br><br>
              {{q8}},<br>
              {{q9}},<br>
              {{q10}},<br>
              {{q11}}.<br>
              </v-card>
              <v-btn
                color=#dbe6dc
                @click="e1 = 1"
              >
              <v-icon>mdi-chevron-left</v-icon>
                Back
              </v-btn>
              <v-btn
                color=#a6c0d1
                @click="e1 = 2"
              >
                Continue
                <v-icon>mdi-chevron-right</v-icon>
              </v-btn>
            </v-stepper-content>

            <v-stepper-content step="2">
              <v-card
                class="mb-12"
                color=#cddbdd
                height="350px"
                max-width="600px"
              ><br>
              The job based on your requirements is
              <strong class="mx-0"> {{output[0]}},<br>
              </strong>
              The MBTI of this job is {{output[1]}},<br>
              {{output[2]}}<br>
              <h4><br>* This is the career that best matches your current field of study.</h4>
              </v-card>
              <v-btn
                color=#dbe6dc
                @click="e1 = 1"
              >
              <v-icon>mdi-chevron-left</v-icon>
                Back
              </v-btn>
              <v-btn
                color=#a6c0d1
                @click="e1 = 3"
              >
                Continue
                <v-icon>mdi-chevron-right</v-icon>
              </v-btn>
            </v-stepper-content>

            <v-stepper-content step="3">
              <v-card
                class="mb-12"
                color=#cddbdd
                height="350px"
                max-width="600px"
              >
              <br>
              The job that makes you feel comfortable is
              <strong class="mx-0"> {{output[3]}},<br>
              </strong>
              The MBTI of this job is {{output[4]}},<br>
              {{output[5]}}
              <br>
              <h4><br>* This is the career that matches your characteries.
              We want to give you some<br> employment inspiration, so that you can find your own endless possibilities.<br>
              </h4>
              </v-card>
              <v-btn
                color=#dbe6dc
                @click="e1 = 2"
              >
              <v-icon>mdi-chevron-left</v-icon>
                Back
              </v-btn>
              <v-btn
                color=#a6c0d1
                @click="e1 = 4"
              >
                Continue
                <v-icon>mdi-chevron-right</v-icon>
              </v-btn>
            </v-stepper-content>

            <v-stepper-content step="4">
              <v-card
                class="mb-12"
                color=#cddbdd
                height="350px"
                max-width="600px"
              ><br>
              If you would like to learn more about your personality characteristics,<br> you can take a professional <strong>MBTI Test</strong> by visiting the following webpage.<br> This webpage is FREE, NO REGISTRATION required,<br> and a systematic questionnaire is used to test your personality type.<br>
              <a target=_blank v-bind:href="myurl">{{ title.toUpperCase() }}</a>
              <br><br>If you would like a more detailed personality analysis,<br> you can visit the following webpage to take a professional <strong>Jungus Test</strong>,<br> which divides your personality type into eight more detailed dimensions.<br> This webpage is FREE, NO REGISTRATION is required,<br> but note that the test is only available in Chinese.<br>
              <a target=_blank v-bind:href="myurl2">{{ title2.toUpperCase() }}</a>
              </v-card>
              <v-btn
                color=#dbe6dc
                @click="e1 = 3"
              >
              <v-icon>mdi-chevron-left</v-icon>
                Back
              </v-btn>
              <v-btn
                color=#a6c0d1
                @click="e1 = 4"
              >
                Continue
                <v-icon>mdi-chevron-right</v-icon>
              </v-btn>
            </v-stepper-content>
          </v-stepper-items>
        </v-stepper>
      </template>
    </v-expansion-panels>
    <div>
      <h2><br></h2>
      <h4>* We also understand that from many factors, to find a job only matches your personality is hard, </h4>
      <h4>so we give you the personality analysis of the employees who are suitable for these</h4>
      <h4>two different careers, and hope you can get some development inspiration.</h4>
      <h2><br></h2>
      <!--提交按钮-->
        <v-hover
          v-slot="{ hover }"
          open-delay="10">
          <v-btn
            :elevation="hover ? 10 : 2"
            :class="{ 'on-hover': hover }"
            color= #82A5D2
            x-large
            v-on:click="back">
            <v-icon large>mdi-chevron-left</v-icon>
            Back to Questionnaire Page
          </v-btn>
        </v-hover>
          <!--返回上一页-->
        <v-hover
          v-slot="{ hover }"
          open-delay="10">
          <v-btn
            :elevation="hover ? 10 : 2"
            :class="{ 'on-hover': hover }"
            color= #82A5D2
            x-large
            v-on:click="submit">Back to Main Page{{ "\xa0" }}
            <v-icon color="blue-grey darken-3" large>mdi-home</v-icon>
          </v-btn>
        </v-hover>

        <v-hover
          v-slot="{ hover }"
          open-delay="10">
          <v-btn
            right
            rounded
            :elevation="hover ? 10 : 2"
            :class="{ 'on-hover': hover }"
            class="right"
            color= #8faf9f
            large
            v-on:click="feed">Feedback
          </v-btn>
        </v-hover>
      <h2><br></h2>
      <h4>Copyright ©️ 2022 Lucky7</h4>
    </div>
  </v-app>
</template>
<script>

export default {
  name: 'Output',
  components: {},
  data() {
    return {
      nameID: '',
      question1: '',
      question2: '',
      question3: '',
      question4: '',
      question5: '',
      question6: '',
      question7: '',
      question8: '',
      question9: '',
      question10: '',
      question11: '',
      e1: 1,
      systemTime: '',
      title: 'The Myers–Briggs Type Indicator Personality Test',
      myurl: 'https://www.16personalities.com/free-personality-test',
      title2: 'Jungus Personality Test',
      myurl2: 'https://www.jungus.cn/zh-hans/',
      // 输出结果
      output: {},
      active_question: 0, // 激活题目的索引，从0开始
      degree: '', // 控制进度条
      num_question: 11, // 总问题数
      q2: ['developed countries in North American', 'developed countries in European', 'developed countries in Oceania', 'developed countries in Asian', 'developing countries'],
      q3: ['full-time job with contract', 'part-time job or an internship'],
      q4: ['work in the office', 'work from home'],
      q5: ['don\'t have any', 'have short-term', 'have long-term', 'have management'],
      q6: ['High School and below', 'Vocational Degree', 'Bachelor\'s Degree', 'Graduate and above'],
      q7: ['Management', 'Engineering', 'Law', 'Art', 'Service', 'Economics', 'Science', 'Communication', 'Medicine', 'Education', 'Language & Literature', 'Others'],
      q8: '',
      q9: '',
      q10: '',
      q11: ''
    }
  },
  created() {
    this.nameID = this.$route.params.nameID
    this.question1 = this.$route.params.question1
    this.question2 = this.$route.params.question2
    this.question3 = this.$route.params.question3
    this.question4 = this.$route.params.question4
    this.question5 = this.$route.params.question5
    this.question6 = this.$route.params.question6
    this.question7 = this.$route.params.question7
    this.question8 = this.$route.params.question8
    this.question9 = this.$route.params.question9
    this.question10 = this.$route.params.question10
    this.question11 = this.$route.params.question11

    if (this.question8 === 'E') {
      this.q8 = 'You act to organize the outer world of people and things'
    }
    if (this.question8 === 'I') {
      this.q8 = 'You act to organize the inner world of ideas and concepts'
    }
    if (this.question8 === 'X') {
      this.q8 = 'You can gather energy whether alone or interacting with others'
    }
    if (this.question9 === 'S') {
      this.q9 = 'you use the sense to gather facts about a situation'
    }
    if (this.question9 === 'N') {
      this.q9 = 'you use the imagination to see what can be done about a situation'
    }
    if (this.question9 === 'X') {
      this.q9 = 'you both use the sense and the imagination to understand the situation'
    }
    if (this.question10 === 'F') {
      this.q10 = 'you decide the impact of a given action on the basis of personal feelings'
    }
    if (this.question10 === 'T') {
      this.q10 = 'you decide logically on the results of any particular action'
    }
    if (this.question10 === 'X') {
      this.q10 = 'you decide actions with both logical and feelings'
    }
    if (this.question11 === 'J') {
      this.q11 = 'you are critical deciders who want planned and orderly lives'
    }
    if (this.question11 === 'P') {
      this.q11 = 'you are flexible, spontaneous, want to understand and adapt to life'
    }
    if (this.question11 === 'X') {
      this.q11 = 'you live your life as you desire or as you plan'
    }

    // Key名存储
    let res = {
      question2: this.question2,
      question3: this.question3,
      question4: this.question4,
      question5: this.question5,
      question6: this.question6,
      question7: this.question7,
      question8: this.question8,
      question9: this.question9,
      question10: this.question10,
      question11: this.question11
    }

    // 创建传输字符串
    function create_res(res) {
      let values = Object.values(res)
      let res_str = ''
      let count = 0
      for (let keys in res) {
        if (res_str === '') {
          res_str = keys + '=' + values[count]
        } else {
          res_str = res_str + '&' + keys + '=' + values[count]
        }
        count++
      }
      return res_str
    }
    let res_str = create_res(res)
    console.log('post: ' + res_str)
    console.log('post2: ' + JSON.stringify(res))
    fetch('http://127.0.0.1:5000/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      }, // this line is important, if this content-type is not set it wont work
      body: res_str
    })
      .then(response => response.json())
      .then(response => {
        this.output = response
        console.log('Object.keys(this.output[0])[0] ' + Object.keys(this.output[0])[0])
        console.log('output ' + this.output)
        console.log('output2 ' + JSON.stringify(this.output))
        console.log('output type' + typeof output)
      })
  },
  mounted () {
    this.addDate()
  },
  methods: {
    addDate () {
      let yy = new Date().getFullYear()
      this.systemTime = yy
      // console.log(this.systemTime)
    },
    submit() {
      // 跳转到下一页
      this.$router.push(
        {
          path: '/',
          name: 'HelloWorld',
          params: {
            nameID: this.nameID
          }
        })
    },
    feed() {
      // 跳转到下一页
      this.$router.push(
        {
          path: '/to-feedback',
          name: 'Feedback',
          params: {
            nameID: this.nameID
          }
        })
    },
    back () {
      this.$router.push(
        {
          path: '/to-question',
          name: 'QuesAsk',
          params: {
            nameID: this.nameID
          }
        })
    },
    jump() {
      // 计算完成情况
      let count_ans = 0
      let flag = {
        price: this.price,
        purpose: this.purpose,
        rgb_require: this.rgb_require,
        brand: this.brand,
        bringout: this.bringout,
        screen: this.screen
      }
      for (let i = 0; i < Object.keys(flag).length; i++) {
        if (Object.values(flag)[i] !== '') {
          count_ans += 1
        }
      }
      // 测试输出
      console.log('now question is ' + length(this.active_question))
      console.log('active question just now: ' + this.active_question)
      console.log('active question now: ' + this.active_question)
      // 跳转到下一个问题
      this.active_question += 1
      // 控制进度条
      this.degree = count_ans / this.num_question * 100
    }
  }
}
</script>

<style scoped>
h4 {
  font-weight: normal;
  color: #818181;
}
.fixCard {
  z-index: 999999;
  position: fixed;
  width: 100%;
}
.right {
  position: fixed;
  z-index: 999999;
  right: 40px;
  bottom: 6%;
}
</style>
