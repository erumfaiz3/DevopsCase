pipeline { 
    agent any 

    stages { 
        stage('Build Docker Image') { 
            steps { 
                echo "Building Docker Image..."
                bat "docker build -t makemytrip:latest ."
            } 
        }
        stage('Docker login') {
            steps {
                bat 'docker login -u erumfaiz -p Erum@3005'
            }
        }

        stage('push Docker image to docker hub'){
            steps{
                echo "push Docker image to docker hub"
                bat "docker tag makemytrip:latest erumfaiz/sample:v1"

                bat "docker push erumfaiz/sample:v1"
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                bat '''
                set KUBECONFIG=C:\\Users\\Administrator\\.kube\\config
                kubectl cluster-info 
                kubectl apply -f deployment.yaml
                kubectl apply -f service.yaml
                '''
            }
        }
    }

    post { 
        success { 
            echo 'Pipeline completed successfully! App deployed to Kubernetes.'
        } 
        failure { 
            echo 'Pipeline failed. Please check the logs for details.' 
        } 
    } 

}
