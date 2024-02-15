podTemplate(containers: [
    containerTemplate(name: 'maven', image: 'maven:3.8.1-jdk-8', command: 'sleep', args: '99d'),
    containerTemplate(name: 'mvn', image: 'maven:3.8.1-jdk-8', command: 'sleep', args: '99d'),
    containerTemplate(name: 'python', image: 'python:3', command: 'sleep', args: '99d')
  ]) {

    node(POD_LABEL) {
        stage('Get a Maven project') {
            git 'https://github.com/webdevprashant/jenkins-training-CI-CD-Day6.git'
            container('maven') {
                stage('Build a Maven project') {
                    //sh 'mvn clean install'
                    
                    sh 'ls -l '

                }
            }
        }
        stage('mvn test') {
            //git 'https://github.com/webdevprashant/jenkins-training-CI-CD-Day6.git'
            container('mvn') {
                stage('Build a Maven project') {
                    //sh 'mvn clean install'
                    
                }
            }
        }
        stage('pthon coding') {
            git 'https://github.com/koyilada-rishi/programing.git'
            container('python') {
                stage('python code') {
                    //sh 'mvn clean install'
                    sh 'python docker.py'
                    sh 'cat Dockerfile'
                    
                }
            }
        }
        stage('Retrieve JAR and WAR files') {
                 
            script {
                //def podName = sh(script: 'kubectl get pods -l jenkins=my-pod-label -o jsonpath="{.items[0].metadata.name}"', returnStdout: true).trim()
                // Copy the WAR file from the Maven container to Jenkins master
                sh "pwd"
                // You can also use kubectl exec to copy the files
                // sh "kubectl exec ${podName} -- cp /path/to/war/files/*.war ."
            }
                     //def podName = sh(script: 'kubectl get pods -l jenkins=my-pod-label -o jsonpath="{.items[0].metadata.name}"', returnStdout: true).trim()
                    // Copy the WAR file from the Maven container to Jenkins master
                    
                    sh  'pwd'
                    //sh "kubectl cp ${podName}:/path/to/war/files/*.war ."
                    //sh 'cp target/*.jar ${WORKSPACE}/'
                   // sh 'cp target/*.war ${WORKSPACE}/'
                
    }
  }
  }
       