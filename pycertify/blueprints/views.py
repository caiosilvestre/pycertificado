from flask import render_template
from flask import request
from .read_files import *
from .appearance import *
from .regex import *

tema = set_principal_theme()

def init_app(app):
    @app.route('/', methods=['GET', 'POST'])
    def inicial():
        global tema
        provas = read_all_test()
        if request.method == 'POST':
            if request.form.get('tema') != None:
                tema = request.form.get('tema').lower()
        return render_template(
        'index.html', 
        provas = provas, tema_escolhido = tema, temas = all_themes())

    @app.route('/<prova>', methods=['GET','POST'])
    def exibi_prova(prova):
        global tema
        if request.method == 'POST':
            if request.form.get('tema') != None:
                tema = request.form.get('tema').lower()
        return render_template(
        'exibir_prova.html', 
        prova = prova , tema_escolhido = tema, temas = all_themes())
    
    @app.route('/<prova>/<int:numquestion>', methods = ['GET','POST'])
    def questoes(prova,numquestion):
        global tema
        if request.method == 'POST':
            if request.form.get('tema') != None:
                tema = request.form.get('tema').lower()
        question = read_question(prova, numquestion)
        test_pt = read_question(prova,numquestion,idioma='pt-br')
        
        return render_template('exibir_questao.html',numquestion = numquestion, 
        question = question , tema_escolhido = tema, 
        temas = all_themes(),
        prova = prova,
        prova_pt = test_pt) 

    @app.route('/<prova>/resposta/<int:numquestion>/<letter>', methods = ['GET','POST'])
    def questoes_resposta(prova,numquestion,letter):
        global tema
        if request.method == 'POST':
            if request.form.get('tema') != None:
                tema = request.form.get('tema').lower()
        test_pt = read_question(prova,numquestion,idioma='pt-br')
        question = read_question(prova, numquestion)
        letter_answer_correct,explanation= read_answer(prova, numquestion)
        return render_template('exibir_questao_resposta.html',numquestion = numquestion, 
        question = question , tema_escolhido = tema, 
        temas = all_themes(),letter_answer = letter,
        letter_answer_correct = letter_answer_correct,
        explanation=explanation,prova = prova,
        prova_pt = test_pt)
