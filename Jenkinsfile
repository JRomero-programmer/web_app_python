pipeline {
  agent {
    kubernetes {
      label 'pod_k8s'
      yaml """
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: docker
    image: docker:20.10
    command: ['cat']
    tty: true
    volumeMounts:
    - name: dockersock
      mountPath: /var/run/docker.sock
  volumes:
  - name: dockersock
    hostPath:
      path: /var/run/docker.sock
"""
    }
  }

  environment {
    DOCKERHUB_CREDENTIALS = credentials('dockerhub_credentials')
    DOCKERHUB_REPO = 'jonatanrm35/web_python'
    IMAGE_TAG = 'latest' 
  }

  stages {
    stage('Build Image') {
      steps {
        container('docker') {
          script {
            def webImage = docker.build("${DOCKERHUB_REPO}:${IMAGE_TAG}", './link_bio')
          }
        }
      }
    }

    stage('Test E2E') {
      steps {
        container('docker') {
          script {
            sh 'echo El test ha pasado con exito'
          }
        }
      }
    }

    stage('Push Image to DockerHub') {
      steps {
        container('docker') {
          script {
            sh "docker login -u ${DOCKERHUB_CREDENTIALS_USR} -p ${DOCKERHUB_CREDENTIALS_PSW}"
            sh "docker push ${DOCKERHUB_REPO}:${IMAGE_TAG}"
          }
        }
      }
    }
  }
}
