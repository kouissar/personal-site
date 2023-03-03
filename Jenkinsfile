// pipeline {
//     agent any
//     options {
//         skipStagesAfterUnstable()
//     }
//     stages {
//          stage('Clone repository') { 
//             steps { 
//                 script{
//                 checkout scm
//                 }
//             }
//         }

//         stage('Build') { 
//             steps { 
//                 script{
//                  app = docker.build("underwater")
//                 }
//             }
//         }
//         stage('Test'){
//             steps {
//                  echo 'Empty'
//             }
//         }
//         stage('Deploy') {
//             steps {
//                 script{
//                         docker.withRegistry('https://720766170633.dkr.ecr.us-east-2.amazonaws.com', 'ecr:us-east-2:aws-credentials') {
//                     app.push("${env.BUILD_NUMBER}")
//                     app.push("latest")
//                     }
//                 }
//             }
//         }
//     }
// }

#!groovy

pipeline {
	agent none
  stages {
  	stage('Maven Install') {
    	agent {
      	docker {
        	image 'maven:3.5.0'
        }
      }
      steps {
      	sh 'mvn clean install'
      }
    }
    stage('Test'){
    steps {
            echo 'Empty'
    }
}
    stage('Docker Build') {
    	agent any
      steps {
      	sh 'docker build -t shanem/spring-petclinic:latest .'
      }
    }
  }
}