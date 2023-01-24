from flask import render_template
from flask import request
from .read_files import *
from .appearance import *
from .regex import *

#Arquivo utilizado para gerenciar as rodas e paginas que serão exibidas
#os return do arquivo realizam o envio de variáveis para o arquivo a html, para serem utilizados pelo JINJA na construção do WEB APP
tema = set_principal_theme()

#Função utilizada para passar o app
def init_app(app):
    
    #página da rota inicial
    @app.route('/', methods=['GET', 'POST'])
    def inicial():
        # Escolha do tema
        global tema
        #chama a função para ler os testes disponíveis
        provas = read_all_test()
        #parte desabilitade, utilizada para escolher o tema da página
        if request.method == 'POST':
            if request.form.get('tema') != None:
                tema = request.form.get('tema').lower()
          
        return render_template(
        'index.html', 
        provas = provas, tema_escolhido = tema, temas = all_themes())

    # página para iniciar a prova escolhida
    @app.route('/<prova>', methods=['GET','POST'])
    def exibi_prova(prova):
        global tema
         #parte desabilitade, utilizada para escolher o tema da página
        if request.method == 'POST':
            if request.form.get('tema') != None:
                tema = request.form.get('tema').lower()
        
        return render_template(
        'exibir_prova.html', 
        prova = prova , tema_escolhido = tema, temas = all_themes())
    
    #página  que inicia as questões a serem realizadas
    @app.route('/<prova>/<int:numquestion>', methods = ['GET','POST'])
    def questoes(prova,numquestion):
        #parte desabilitade, utilizada para escolher o tema da página
        global tema
        if request.method == 'POST':
            if request.form.get('tema') != None:
                tema = request.form.get('tema').lower()
        # Função para ler a questão e trazer ela     
        question = read_question(prova, numquestion)
        # Função para trazer a pergunta traduzida
        test_pt = read_question(prova,numquestion,idioma='pt-br')
        #Função volta o total de questões da prova
        total_questions = count_questions(prova)
        return render_template('exibir_questao.html',numquestion = numquestion, 
        question = question , tema_escolhido = tema, 
        temas = all_themes(),
        prova = prova,
        prova_pt = test_pt,
        total_questions= total_questions) 
    
    #página responsável por exibir as resposta da questão
    @app.route('/<prova>/resposta/<int:numquestion>/<letter>', methods = ['GET','POST'])
    def questoes_resposta(prova,numquestion,letter):
        #parte desabilitade, utilizada para escolher o tema da página
        global tema
        if request.method == 'POST':
            if request.form.get('tema') != None:
                tema = request.form.get('tema').lower()
        
        
        # Função para trazer a pergunta traduzida
        test_pt = read_question(prova,numquestion,idioma='pt-br')
        #Função volta o total de questões da prova
        question = read_question(prova, numquestion)
        #Função volta a resposta correta
        letter_answer_correct,explanation= read_answer(prova, numquestion)
        #Função volta o total de questões da prova
        total_questions = count_questions(prova)
        
        return render_template('exibir_questao_resposta.html',numquestion = numquestion, 
        question = question , tema_escolhido = tema, 
        temas = all_themes(),letter_answer = letter,
        letter_answer_correct = letter_answer_correct,
        explanation=explanation,prova = prova,
        prova_pt = test_pt,
        total_questions=total_questions)
