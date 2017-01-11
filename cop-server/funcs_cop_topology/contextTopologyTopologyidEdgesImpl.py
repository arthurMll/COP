import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class ContextTopologyTopologyidEdgesImpl:

    @classmethod
    def get(cls, topologyId):
        print 'handling get'
        if topologyId in be.context.topology:
            return be.context.topology[topologyId].edges
        else:
            raise KeyError('topologyId')
