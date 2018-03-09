import web

web.config.debug = False

urls = (
    # "/hello", "Index",
    "/count", "count",
    "/reset", "reset"
)

app = web.application(urls, locals())
store = web.session.DiskStore('../sessions/')
session = web.session.Session(app, store, initializer={'count': 0})

class count:
    def GET(self):
        session.count += 1
        return str(session.count)

class reset:
    def GET(self):
        session.kill()
        return ""

# # run app_test use abs path ('D:\\ex\\ex52\\projects\\gothonweb\\templates') can pass
# render = web.template.render('D:\\ex\\ex52\\projects\\gothonweb\\templates', base="layout")
#
# class Index(object):
#     def GET(self):
#         return render.hello_form()
#
#     def POST(self):
#         form = web.input(name="Nobody", greet="Hello")
#         greeting = "%s, %s" % (form.greet, form.name)
#         return render.index(greeting=greeting)


if __name__ == "__main__":
    app.run()
