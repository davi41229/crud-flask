from aplication import aplication
from flask import render_template, redirect, request, url_for
from flask_login import login_user, logout_user
import base64
from PIL import Image

from werkzeug.security import generate_password_hash

from werkzeug.security import generate_password_hash

from aplication import aplication, db
from aplication.models.models import Info




@aplication.route('/') # rota da pagina principal
def home():
    return render_template('inicial.html')
    

@aplication.route('/register', methods=['GET', 'POST']) # rota para cadastrar usuarios
def register():
    if request.method == 'POST': 
        name = request.form['name'] 
        email = request.form['email'] 
        image = request.form['image'].encode()
        pwd = request.form['password'] 

        info = Info(name, email, image, pwd)
        db.session.add(info) #REGISTRANDO O USUARIO NA SESSAO
        db.session.commit() #SALVANDO  OS DADOS NO BANCO

    return render_template( 'cadastrar.html')



@aplication.route('/login', methods=['GET', 'POST']) # rota para fazer login de usuario
def login():
    if request.method == 'POST': 
        email = request.form['email']
        pwd = request.form['password']


        info = Info.query.filter_by(email=email).first() 

        if not info or not info.verify_password(pwd): 
            return redirect(url_for('login'))
            
        login_user(info) 
        return redirect(url_for('home')) 

    return render_template('login.html') 




@aplication.route('/logout') # rota para sair do usuario
def logout():
    logout_user() 
    return redirect(url_for('login')) 



@aplication.route('/contas') # rota para mostrar os usuarios cadastrados
def contas():
    contas = Info.query.all()
    return render_template( 'contas.html', contas=contas)



@aplication.route('/deletar/<int:id>') # rota para deletar usuarios
def deletar(id):
    usuario = Info.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    return redirect(url_for('contas'))


@aplication.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    editar_usuario = Info.query.get(id)
    if request.method == 'POST': 
        editar_usuario.name = request.form['name'] 
<<<<<<< HEAD
        editar_usuario.email = request.form['email']
        editar_usuario.image = request.form['image'].encode() 
=======
        editar_usuario.email = request.form['email'] 
>>>>>>> 646dc19a238e18ea42f47b84d802a8ce934cb245
        editar_usuario.password = generate_password_hash(request.form['password'])
        
        db.session.commit() #SALVANDO  OS DADOS NO BANCO
        
        return redirect(url_for('contas'))
    return render_template( 'editar.html', editar_usuario=editar_usuario)


@aplication.route('/save',methods=['GET', 'POST'])
def salvar_imagem():
    if request.method == 'POST':
        image = request.form['image']
        filename = image
        img = Image.open(image)
        rgb_img = img.convert('RGB')
        rgb_img.save("uploads/" + filename + ".jpg")            
    return render_template( 'upload.html')
