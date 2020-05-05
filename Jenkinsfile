pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python' 
                }
            }
            steps {
                sh 'python -m py_compile blackjack.py card.py deck.py hand.py' 
                stash(name: 'compiled-results', includes: '*.py*') 
            }
        }
        stage('Test') { 
            agent {
                docker {
                    image 'qnib/pytest' 
                }
            }
            steps {
                sh 'py.test --junit-xml test-reports/results.xml tests.py' 
            }
            post {
                always {
                    junit 'test-reports/results.xml' 
                }
            }
        }
    }
}