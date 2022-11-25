pipeline{
agent any 
	stages {
		stage('Cloning Stage') {
			steps {
				git 'https://github.com/anand887723-stack/check_Se_proj.git'
			}
		}
		stage('Run Code') {
			steps {
				sh "/usr/bin/python3 test_p1.py"
			}
		}
		stage('Testing stage') {
			steps {
				sh "/usr/bin/python3 test_1.py"
			}
		}
	}
}
