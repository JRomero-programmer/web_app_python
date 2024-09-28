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

    stage('Verify Test Directory') {
      steps {
        container('docker') {
          sh 'ls -l'
        }
      }
    }

    stage('Build E2E Image') {
      steps {
        container('docker') {
          script {
            def e2eImage = docker.build('image_e2e_tests', './test_E2E')
          }
        }
      }
    }

    stage('Run Web and E2E Containers') {
      steps {
        container('docker') {
          script {
            sh 'docker run -d --name web_container -p 3000:3000 image_web_python'
            sh 'docker run --name e2e_container image_e2e_tests'
          }
        }
      }
    }
  }
}
