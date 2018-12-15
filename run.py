###################
#
#  Run Flask app for debug purposes only
#
##################
import api
import sys
import os
from api.config import cfg
from api.app import app #, handlers
# print("FROM FLASK: DIR",dir(api))
# print("FROM FLASK: path", sys.path)
print("FROM FLASK cwd:", os.getcwd())

script_path = os.path.dirname(os.path.abspath( __file__ ))
print("FROM FLASK: script_path", script_path)
print("FROM FLASK: root_path", app.root_path )
# print("FROM FLASK: instance_path", app.instance_path )

if __name__ == "__main__":
    app.run(host=cfg.CFG_LOCALHOST, port=cfg.CFG_PORT, debug=cfg.CFG_DEBUG)    # , ssl_context=cfg.CFG_SSL_CONTEXT
