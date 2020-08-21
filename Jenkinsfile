pipeline {
    stages {
        stage('main') {
            steps {
                    sh '''
                        docker version
                        docker system prune --all --force
                        DOCKER_BUILDKIT=1 docker build --progress plain --no-cache .
                    '''
            }
        }
    }
}
