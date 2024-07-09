<template>
  <div class="home">
    <h1>Staten Island Technical High School Classes</h1>
    <form id="ClassSearch">
      <div class="Selectors">
        <label>Search: </label>
        <input type="text" name="classSearch" v-model="searchMenu">
      </div>
      <div class="Selectors">
        <label>Subject: </label>
        <select name="subject" v-model="selectSubject">
          <option></option>
          <option v-for="subject in subjectNames" :key="subject">{{ subject }}</option>
        </select>
        <label>Grade: </label>
        <select id="grade" v-model="selectGrade">
          <option></option>
          <option v-for="grade in Grades" :key="grade">{{ grade }}</option>
        </select>
      </div>
    </form>
    <div id="UserZone">
      <div id="ClassList">
        <label style="font-style: italic; font-size: 12px">Click a class to add it to saved classes</label>
        <div v-for="course in classesInSearch" :key="course" class="classInfo" @click="addToSavedClasses(course)">
          <p class="classTitle">{{ course['class'] }}:</p><p>{{ course['description'] }}</p>
        </div>
      </div>
      <div id="PersonalInfo" v-if="savedClassed.length > 0">
        <p v-for="savedClass in savedClassed" :key="savedClass" @click="removeFromSavedClasses(savedClass)">
          {{ savedClass['class'] }}
        </p>
        
      </div>
    </div>
  </div>
</template>

<script>
import { computed, ref } from 'vue';
import classJson from '@/assets/classes.json';
// @ is an alias to /src

export default {
  name: 'HomeView',
  components: {
  },
  setup() {
    const searchMenu = ref('');
    const selectSubject = ref('');
    const subjects = classJson;
    const classes = ref([]);
    const subjectNames = Object.keys(subjects);
    const Grades = [9, 10, 11, 12];
    const selectGrade = ref(null);
    const savedClassed = ref([]);
    
    function addToSavedClasses(course) {
      if(!savedClassed.value.includes(course)) {
        savedClassed.value.push(course); 
      }
    }
    function removeFromSavedClasses(course) {
      savedClassed.value = savedClassed.value.filter((c) => c !== course);
    }
    //console.log(subjectNames);
    //output the properties of the first 10 subjects
    for (let subject in subjects) {
      for (let i in subjects[subject]) {
        classes.value.push(subjects[subject][i]);
      }
    }
    const classesInSearch = computed(() => {
      let typefilter= (classes.value.filter((c) => c['class'].toLowerCase().includes(searchMenu.value.toLowerCase())))
      //console.log(typefilter)
      //console.log(selectSubject.value)
      if (selectSubject.value) {
        typefilter = typefilter.filter((c) => c['subject'] === selectSubject.value)
      }
      if (selectGrade.value) {
        console.log(selectGrade.value);
        typefilter = typefilter.filter((c) => {
            const gradesArray = Object.values(c['grades']);
            //console.log(gradesArray); // Logging the converted array
            return gradesArray.includes(Number(selectGrade.value));
        });
        //console.log(tempfilter);
      }
      return typefilter
    })
    //console.log(classes.value);
    return { 
      searchMenu, 
      subjects,
      classes,
      classesInSearch,
      subjectNames,
      selectSubject,
      Grades,
      selectGrade,
      savedClassed,
      addToSavedClasses,
      removeFromSavedClasses
    };
  }
}
</script>


<style>
.home {
  margin: 0%;
}
p {
  font-size: 18px;
  font-family:Arial, Helvetica, sans-serif;
  margin:10px 0 10px 0;
  text-align: left;
}
.classTitle {
  font-weight: bold;
  font-size: 20px;
}
#ClassList {
  display: flex;
  flex-direction: column;
  padding: 20px;
  border: 1px solid black;
  background-color: #f5f5f5;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  max-height: calc(110vh - 400px);
  overflow-y: auto;
  width: 100%;
}

#ClassSearch {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: fit-content;
  margin: auto;
  padding: 20px;
  border: 1px solid black;
  border-radius: 10px;
  background-color: #f5f5f5;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  align-items: flex-start;
  margin-bottom: 5px;
}

label {
  font-size: 20px;
  margin-bottom: 10px;
  text-align: left;
}

input {
  padding: 10px;
  margin-bottom: 10px;
  margin-left: 5px;
  border: 1px solid black;
  border-radius: 5px;
  font-size: 16px;
}

select {
  padding: 10px;
  margin-bottom: 10px;
  margin-right: 10px;
  margin-left: 5px;
  border: 1px solid black;
  border-radius: 5px;
  font-size: 16px;
}

.Selectors {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}

#grade {
  width: 70px;
}

.classInfo {
  cursor: pointer;
  margin-bottom: 10px;
}

#UserZone {
  display: flex;
  flex-direction: row;
  width: fit-content;
  align-items: flex-start;
  width: 100%;
}

#PersonalInfo {
  display: flex;
  margin-left: 10px;
  width: 100%;
  border: 1px solid black;
  flex-direction: column;
  overflow-y: scroll;
  max-height: calc(110vh - 360px);
}

#PersonalInfo p {
  padding: 10px;
  margin: 5px 0 5 0;
  font-size: 20px;
  font-family: Arial, Helvetica, sans-serif;
  font-weight: bold;
  cursor: pointer;
}

#PersonalInfo p:hover {
  text-decoration: underline;
  background-color: crimson;
  color: rgb(0, 0, 0);
}

</style>