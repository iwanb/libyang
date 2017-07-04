import libyang.libyangpyc as lib
from enum import Enum

class NodeType(Enum):
    UNKNOWN = lib.LYS_UNKNOWN
    CONTAINER = lib.LYS_CONTAINER
    CHOICE = lib.LYS_CHOICE 
    LEAF = lib.LYS_LEAF
    LEAFLIST = lib.LYS_LEAFLIST
    LIST = lib.LYS_LIST
    ANYXML = lib.LYS_ANYXML
    CASE = lib.LYS_CASE
    NOTIF = lib.LYS_NOTIF
    RPC = lib.LYS_RPC
    INPUT = lib.LYS_INPUT
    OUTPUT = lib.LYS_OUTPUT
    GROUPING = lib.LYS_GROUPING
    USES = lib.LYS_USES
    AUGMENT = lib.LYS_AUGMENT
    ACTION = lib.LYS_ACTION
    ANYDATA = lib.LYS_ANYDATA
    EXT = lib.LYS_EXT

class Module(object):
    def __init__(self, _module):
        self._mod = _module

    @property
    def name(self):
        return self._mod.name

    @property
    def prefix(self):
        return self._mod.prefix

    @property
    def description(self):
        return self._mod.dsc

    @property
    def reference(self):
        return self._mod.ref

    @property
    def organization(self):
        return self._mod.org

    @property
    def contact(self):
        return self._mod.contact

    @property
    def filepath(self):
        return self._mod.filepath

class Submodule(Module):
    def belongsto(self):
        return Module(self._mod.belongsto)


class Tree(object):
    @property
    def parent(self):
        node = self._node.parent
        if node is None:
            return None
        return self._nodenew(node)

    @property
    def prev(self):
        node = self._node.prev
        if node is None:
            # Should not happen
            return None
        return self._nodenew(node)

    @property
    def next(self):
        node = self._node.next
        if node is None:
            return None
        return self._nodenew(node)

    @property
    def child(self):
        node = self._node.child
        if node is None:
            return None
        return self._nodenew(node)

class BaseNode(Tree):
    def __init__(self, _node):
        self._node = _node
        self._nodenew = Node

    @property
    def name(self):
        return self._node.name

class Container(BaseNode):
    pass

class Choice(BaseNode):
    pass

class Leaf(BaseNode):

    @property
    def default(self):
        return self._node.dflt

class LeafList(BaseNode):
    pass

class List(BaseNode):
    pass

class AnyData(BaseNode):
    pass

class Uses(BaseNode):
    pass

class Grouping(BaseNode):
    pass

class Case(BaseNode):
    pass

class InOut(BaseNode):
    pass

class Notification(BaseNode):
    pass

class RpcAction(BaseNode):
    pass

class Augment(BaseNode):
    pass

_nodetypetoclass = {
    NodeType.CONTAINER.value: Container,
    NodeType.CHOICE.value: Choice,
    NodeType.LEAF.value: Leaf,
    NodeType.LEAFLIST.value: LeafList,
    NodeType.LIST.value: List,
    NodeType.ANYDATA.value: AnyData,
    NodeType.USES.value: Uses,
    NodeType.CASE.value: Case,
    NodeType.INPUT.value: InOut,
    NodeType.RPC.value: RpcAction,
    NodeType.ACTION.value: RpcAction,
    NodeType.AUGMENT.value: Augment,
}

def Node(_node):
    cls = BaseNode
    if _node.nodetype in _nodetypetoclass:
        cls = _nodetypetoclass[_node.nodetype]
        cast = getattr(lib, 'lys_swig_cast_node_' + cls.__name__.lower())
        _node = cast(_node)
    return cls(_node)
