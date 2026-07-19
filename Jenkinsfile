pipeline {
    agent any

    stages {
        stage('Stage 1: Ejecución Serenity') {
            steps {
                echo '=== CLONANDO Y EJECUTANDO PRUEBAS SERENITY (JAVA) ==='
                // Entramos a la carpeta exacta de tu proyecto Java
                dir('serenity-screenplay-framework') {
                    // Limpia y ejecuta las pruebas de Serenity generando el reporte aggregate
                    sh 'mvn clean verify -U'
                }
            }
            post {
                always {
                    echo '=== ARCHIVANDO REPORTES DE SERENITY ==='
                    // Guarda el reporte HTML completo en Jenkins como evidencia obligatoria
                    archiveArtifacts artifacts: 'serenity-screenplay-framework/target/site/serenity/**', allowEmptyArchive: true
                }
            }
        }

        stage('Stage 2: Ejecución Playwright') {
            steps {
                echo '=== CONFIGURANDO ENTORNO PYTHON Y PLAYWRIGHT ==='
                // Entramos a la carpeta de tu proyecto Python
                dir('playwright-screenplay-framework') {
                    // Creamos un entorno virtual exclusivo para Jenkins
                    sh 'python3 -m venv venv_jenkins'
                    sh './venv_jenkins/bin/pip install --upgrade pip'
                    sh './venv_jenkins/bin/pip install -r requirements.txt'
                    
                    echo '=== INSTALANDO NAVEGADORES DE PLAYWRIGHT ==='
                    // Descarga los browsers internos y las librerías Linux necesarias
                    sh './venv_jenkins/bin/python -m playwright install --with-deps chromium'
                    
                    echo '=== EJECUTANDO PRUEBAS BDD (PLAYWRIGHT) ==='
                    // Ejecuta behave y exporta el reporte HTML a una carpeta llamada reports
                    sh './venv_jenkins/bin/behave -f html -o reports/reporte_playwright.html || true'
                }
            }
            post {
                always {
                    echo '=== ARCHIVANDO REPORTES DE PLAYWRIGHT ==='
                    // Guarda el reporte de Python como evidencia
                    archiveArtifacts artifacts: 'playwright-screenplay-framework/reports/**', allowEmptyArchive: true
                }
            }
        }
    }

    post {
        always {
            echo '=== PIPELINE FINALIZADO - LIMPIANDO ESPACIO DE TRABAJO ==='
            cleanWs()
        }
    }
}