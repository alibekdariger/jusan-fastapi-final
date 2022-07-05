pipeline
{
    agent any

    environment {
        python ='/usr/bin/python3'
        pytest ='/usr/bin/pytest'
        }

    triggers {
        pollSCM 'H * * * *'
    }

    stages{

          stage('Checkout') {
            steps {
                git credentialsId:'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', url: 'https://github.com/alibekdariger/jusan-fastapi-final', branch: 'master'
            }
        }
        stage('Restore packages'){
            steps{
                sh "python3 main.py"
            }
        }
        stage('Test: Unit Test'){
            steps {
                sh "pytest test_api.py"
            }
        }
        stage('Publish'){
            steps{
                sh "python3 -m py_compile main.py"
                
            }
        }
    }
 }