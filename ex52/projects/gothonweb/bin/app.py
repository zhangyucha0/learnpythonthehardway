import web
try:
    from gothonweb import map
except ImportError:
    import sys
    sys.path.append("..")
    from gothonweb import map


urls = (
    "/game", "GameEngine",
    "/", "Index"
)

app = web.application(urls, globals())

# Little hack so that debug mode works with sessions
if web.config.get('_session') is None:
    # '../sessions/'
    store = web.session.DiskStore('D:\\ex\\ex52\\projects\\gothonweb\\sessions')
    session = web.session.Session(app, store, initializer={'room': None})
    web.config._session = session
else:
    session = web.config._session
    # '../templates/'
render = web.template.render('D:\\ex\\ex52\\projects\\gothonweb\\templates', base='layout')

class Index(object):
    def GET(self):
        # this is used to "setup" the session with starting values
        session.room = map.START
        web.seeother("/game")

class GameEngine(object):
    def GET(self):
        if session.room:
            return render.show_room(room=session.room)
        else:
            # why is there here? do you need it
            return render.you_died()

    def POST(self):
        form = web.input(action=None)

        # there is a bug here, you can fix it?
        if session.room and form.action:
            session.room = session.room.go(form.action)

        web.seeother("/game")


if __name__ == "__main__":
    app.run()
