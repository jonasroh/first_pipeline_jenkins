/* Requires the Docker Pipeline plugin */
pipeline {
    agent any 
    stages {
        stage('Teste') {
            steps {
                echo "Testando"
            }
        }
        stage('Instalando dependências'){
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
    }
}
