from flask_bootstrap import ConditionalCDN, StaticCDN, WebCDN

static = StaticCDN()
local = StaticCDN('bootstrap.static', rev=True)


def lwrap(cdn, primary=static):
    return ConditionalCDN('BOOTSTRAP_SERVE_LOCAL', primary, cdn)



def change_version(app, version='4.3.1'):
    app.extensions['bootstrap']['cdns']['bootstrap4'] = lwrap(
            WebCDN('//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/%s/' %
                   version), local)
    return app