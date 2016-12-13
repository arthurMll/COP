import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class ConnectionsConnectionConnectionidZendImpl:

    @classmethod
    def put(cls, connectionId, endpoint):
        print str(endpoint)
        print 'handling put'
        be.connections.connection[connectionId] = endpoint

    @classmethod
    def post(cls, connectionId, endpoint):
        print str(endpoint)
        print 'handling post'
        be.connections.connection[connectionId] = endpoint

    @classmethod
    def delete(cls, connectionId):
        print 'handling delete'
        if connectionId in be.connections.connection:
            del be.connections.connection[connectionId].zEnd
        else:
            raise KeyError('connectionId')

    @classmethod
    def get(cls, connectionId):
        print 'handling get'
        if connectionId in be.connections.connection:
            return be.connections.connection[connectionId].zEnd
        else:
            raise KeyError('connectionId')
