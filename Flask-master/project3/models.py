from .app import db


class usa(db.Model):
    __tablename__ = 'usatesting'
    time = db.Column(db.String(64), primary_key=True)
    open = db.Column(db.String(64))
    high = db.Column(db.String(64))
    low = db.Column(db.String(64))
    last = db.Column(db.String(64))
    change = db.Column(db.String(64))
    volume =  db.Column(db.String(64))
    cases = db.Column(db.Integer)
    deaths = db.Column(db.Integer)
    geoid = db.Column(db.Float)

def __repr__(self):
        return '<usa %r>' % (self.name)

class kr(db.Model):
    __tablename__ = 'korean'
    time = db.Column(db.String(64), primary_key=True)
    open = db.Column(db.String(64))
    high = db.Column(db.String(64))
    low = db.Column(db.String(64))
    last = db.Column(db.String(64))
    change = db.Column(db.String(64))
    volume =  db.Column(db.String(64))
    cases = db.Column(db.Integer)
    deaths = db.Column(db.Integer)
    geoid = db.Column(db.Float)

def __repr__(self):
        return '<kr %r>' % (self.name)

class uk(db.Model):
    __tablename__ = 'uk'
    time = db.Column(db.String(64), primary_key=True)
    open = db.Column(db.String(64))
    high = db.Column(db.String(64))
    low = db.Column(db.String(64))
    last = db.Column(db.String(64))
    change = db.Column(db.String(64))
    volume =  db.Column(db.String(64))
    cases = db.Column(db.Integer)
    deaths = db.Column(db.Integer)
    geoid = db.Column(db.Float)

def __repr__(self):
    return '<uk %r>' % (self.name)
© 2020 GitHub, Inc.