from objects_common.jsonObject import JsonObject
from serviceEndPointType import ServiceEndPointType
from topology import Topology
from objects_common.keyedArrayType import KeyedArrayType

class TopologiesSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.serviceEndPoint=KeyedArrayType(ServiceEndPointType, 'sepId')
        self.topology=KeyedArrayType(Topology, 'topologyId')
        super(TopologiesSchema, self).__init__(json_struct)

