'''
from App import app, socketio
socketio.run( app, host='0.0.0.0', port=5000 )
'''

from App import app

if __name__=='__main__':
    app.run( host='0.0.0.0', port=5000 )


