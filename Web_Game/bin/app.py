import web
from web_game import game

urls = (
    '/game', 'GameEngine',
    '/', 'Index'
)

app = web.application(urls, globals())

# hack so that debug mode works with sessions
if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store, initializer = {'scene': None})
    web.config._session = session
else:
    session = web.config._session
    
render = web.template.render('templates/', base = "layout")

class Index(object):
    def GET(self):
        # used to setup the session with starting values
        session.room = game.START
        #session.room = 
        web.seeother("/game")
        
class GameEngine(object):
    
    def GET(self):
        if session.room:
            return render.show_room(room = session.room)
        else:
            # Q: why is this here? Do we need it??
            # A: Catch if session.room not properly set (?)
            return render.you_died()
            
    def POST(self):
        form = web.input(action = None)
        
        # bug...
        if session.room and form.action:
            session.room = session.room.go(form.action)
            
        web.seeother("/game")
                   
if __name__ == "__main__":
    app.run()