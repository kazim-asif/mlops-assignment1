pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Your build steps here
                echo 'Building...'
            }
        }
        stage('Test') {
            steps {
                // Your test steps here
                echo 'Testing...'
            }
        }
        stage('Deploy') {
            steps {
                // Your deployment steps here
                echo 'Deploying...'
            }
        }
    }

    post {
        success {
            // Send email notification upon successful completion
            emailext subject: 'Jenkins Job Success',
                      body: 'The Jenkins job has been successfully completed.',
                      to: 'i202310@nu.edu.pk',
                      attachLog: true
        }
    }
}
