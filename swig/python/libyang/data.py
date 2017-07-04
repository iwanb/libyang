import libyang.libyangpyc as lib
from libyang.schema import Node as SchemaNode, Tree
from enum import Enum

class Format(Enum):
    UNKNOWN = lib.LYD_UNKNOWN
    XML = lib.LYD_XML
    JSON = lib.LYD_JSON

class Dataset(Enum):
    DATA = lib.LYD_OPT_DATA
    CONFIG = lib.LYD_OPT_CONFIG
    GET = lib.LYD_OPT_GET
    GETCONFIG = lib.LYD_OPT_GETCONFIG
    EDIT = lib.LYD_OPT_EDIT
    RPC = lib.LYD_OPT_RPC
    RPCREPLY = lib.LYD_OPT_RPCREPLY
    NOTIF = lib.LYD_OPT_NOTIF
    NOTIF_FILTER = lib.LYD_OPT_NOTIF_FILTER
    NOTIF_TYPEMASK = lib.LYD_OPT_TYPEMASK

class BaseNode(Tree):
    def __init__(self, _node):
        self._node = _node
        self._nodenew = Node

    @property
    def schema(self):
        return SchemaNode(self._node.schema)

    @property
    def parent(self):
        node = self._node.parent
        if node is None:
            return None
        return Node(node)

    @property
    def prev(self):
        node = self._node.prev
        if node is None:
            # Should not happen
            return None
        return Node(node)

    @property
    def next(self):
        node = self._node.next
        if node is None:
            return None
        return Node(node)

    @property
    def child(self):
        node = self._node.child
        if node is None:
            return None
        return Node(node)

def Node(_node):
    # TODO find out correct node type
    return BaseNode(_node)
