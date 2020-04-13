pipeline{
    agent{
        kubernetes{
            defaultContainer 'python'
        }
    }
    stages{
        stage('Launch Coverage Test'){
            steps{
                sh  '''#!bin/bash
                    pytests --continue-on-collection-errors --cov-report xml --cov=aa_scoring tests/ || [[ $? -eq 1 ]]
                    '''
            }
        }
    }
}