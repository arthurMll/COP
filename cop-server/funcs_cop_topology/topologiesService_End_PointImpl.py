import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class TopologiesService_End_PointImpl:

    @classmethod
    def get(cls, ):
        print 'handling get'
        if be.topologies:
            return be.topologies
        else:
            raise KeyError('')
