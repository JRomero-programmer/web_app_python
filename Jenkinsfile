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
    stage('Build and Test Docker image') {
      steps {
        container('docker') {
          script {
            def image = docker.build('web_python', './link_bio/dockerfile')

            image.inside {
              sh 'ls -l'
            }
          }
        }
      }
    }
  }
}
