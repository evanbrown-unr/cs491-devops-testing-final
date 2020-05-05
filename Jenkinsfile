pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:2-alpine' 
                }
            }
            steps {
                sh 'python -m py_compile blackjack.py card.py deck.py hand.py' 
                stash(name: 'compiled-results', includes: '*.py*') 
            }
        }
    }
}