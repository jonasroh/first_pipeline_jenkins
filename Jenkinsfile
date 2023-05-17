/* Requires the Docker Pipeline plugin */
pipeline {
    agent any 
    stages {
        stage('echo Teste') {
            steps {
                echo "Testando"
            }
        }
        stage('Instalando dependências'){
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Teste'){
            steps {
                sh 'python3 -m unittest test_app.py'
            }
        }
        stage('Deploy'){
            steps {
                sh 'python3 app.py &'
                script {
                    sh 'sleep 60'
                    sh 'pkill -f "python3 app.py"'
                }
            }
        }
    }
}

