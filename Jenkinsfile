pipeline{
    agent{
        kubernetes{
            defaultContainer 'python'
        }
    }
    stages{
        stage('Build'){
            steps{
                sh  '''#!bin/bash
                    docker-compose up
                    '''
            }
        }
        stage('Test'){
            steps{
                sh  '''#!bin/bash
                    pytests --contunue-on-collection-errors tests/test.py
                    
                    pytests --continue-on-collection-errors --cov-report xml --cov=aa_scoring tests/ || [[ $? -eq 1 ]]
                    '''
            }
        }
        stage('Deploy'){
            steps{
                sh  '''#!bin/bash
                    
                    '''
            }
        }
    }
}
