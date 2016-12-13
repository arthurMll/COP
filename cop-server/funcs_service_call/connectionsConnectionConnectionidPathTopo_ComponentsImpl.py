import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class ConnectionsConnectionConnectionidPathTopo_ComponentsImpl:

    @classmethod
    def get(cls, connectionId):
        print 'handling get'
        if connectionId in be.connections.connection:
            return be.connections.connection[connectionId].path.topoComponents
        else:
            raise KeyError('connectionId')
