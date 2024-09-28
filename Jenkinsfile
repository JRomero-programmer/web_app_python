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

  stages {
    stage('Build Web Image') {
      steps {
        container('docker') {
          script {
            def webImage = docker.build('image_web_python', './link_bio')
          }
        }
      }
    }

    stage('Build E2E Image') {
      steps {
        container('docker') {
          script {
            def e2eImage = docker.build('image_e2e_tests', './test-E2E')
          }
        }
      }
    }

    stage('Run Web and E2E Containers') {
      steps {
        container('docker') {
          script {
            sh 'docker stop web_container || true'
            sh 'docker rm web_container || true'
            sh 'docker stop e2e_container || true'
            sh 'docker rm e2e_container || true'
            sh 'docker network create test_network || true'

            sh 'docker run -d --name web_container --network test_network -p 3000:3000 image_web_python'

            sh 'sleep 30'

            sh 'docker run --name e2e_container --network test_network image_e2e_tests'
          }
        }
      }
    }
  }

  post {
    always {
      container('docker') {
        sh 'docker stop web_container || true'
        sh 'docker rm web_container || true'
        sh 'docker stop e2e_container || true'
        sh 'docker rm e2e_container || true'
        sh 'docker network rm test_network || true'
      }
    }
  }
}
