pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:3' 
                }
            }
            steps {
                sh 'python3 -m py_compile blackjack.py card.py deck.py hand.py' 
                stash(name: 'compiled-results', includes: '*.py*') 
            }
        }
        stage('Test') { 
            agent {
                docker {
                    image 'python:3' 
                }
            }
            steps {
                sh 'python3 --verbose tests.py' 
            }
        }
    }
}