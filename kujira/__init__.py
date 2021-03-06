""" Kujira API is flask/websocket app for serving Ceph cluster data """

from flask import Flask
from flask_socketio import SocketIO
from kujira.blueprints import SERVER_BP, OSD_BP, POOL_BP, MON_BP, CLUSTER_BP
from kujira.rest.controllers import osds, pools, servers, clusters, mons

import eventlet
eventlet.monkey_patch()

SOCKETIO = SocketIO()


def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)

    app.register_blueprint(OSD_BP)
    app.register_blueprint(SERVER_BP)
    app.register_blueprint(POOL_BP)
    app.register_blueprint(MON_BP)
    app.register_blueprint(CLUSTER_BP)

    app.debug = debug
    app.config.from_object('config')

    SOCKETIO.init_app(app, engineio_logger=True, async_mode='eventlet')

    return app
