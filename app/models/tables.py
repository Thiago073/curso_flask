from app import db

# Construindo a Classe da tabela usuarios
class User(db.Model):
    __tablename__ = 'users'
    
    # Definindo as Colunas da nossa Tabela 
    # OBS: O "unique=True" significa que o campo não pode se repitir, ele tem que ser uníco  
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    
    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        
    def __repr__(self):
        return '<User %r>' % self.username
    
    
class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    user = db.relationship('User', foreing_key=user_id)
    
    def __init__(self, contet, user_id):
        self.contet = contet
        self.user_id = user_id
        
    def __repr__(self):
        return '<Post %r>' % self.id
    
    
class Follow(db.Model):
    __tablename__ = 'follow'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    user = db.relationship('User', foreing_key=user_id)
    follower = db.relationship('User', foreing_key=follower_id)
    
    