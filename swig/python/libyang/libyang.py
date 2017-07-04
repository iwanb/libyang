import libyang.libyangpyc as lib
from libyang.schema import Module, Node
from libyang.data import Format, Dataset, Node as DataNode

class YangError(Exception):
    def __init__(self, message=''):
        msgs = [message]
        msgs.append(str(lib.ly_errmsg()))
        msgs.append(str(lib.ly_errpath()))
        msg = '\n'.join(m for m in msgs if m != "")
        super().__init__(msg)

class ModuleNotFound(YangError):
    pass

class NodeNotFound(YangError):
    pass

class ParseError(YangError):
    pass

class Context(object):
    def __init__(self, search_dir=None):
        self._ctx = lib.ly_ctx_new(search_dir)

    @property
    def search_dir(self):
        return lib.ly_ctx_get_searchdir(self._ctx)

    @search_dir.setter
    def search_dir(self, search_dir):
        return lib.ly_ctx_set_searchdir(self._ctx, search_dir)

    def get_module(self, name, revision=None):
        m = lib.ly_ctx_get_module(self._ctx, name, revision)
        if m is None:
            raise ModuleNotFound
        return Module(m)

    def load_module(self, name, revision=None):
        try:
            return self.get_module(name, revision)
        except ModuleNotFound:
            pass
        m = lib.ly_ctx_load_module(self._ctx, name, revision)
        if m is None:
            raise ModuleNotFound
        return Module(m)

    def get_node(self, nodeid, start=None):
        if start is not None:
            start = start._node
        n = lib.ly_ctx_get_node(self._ctx, start, nodeid)
        if n is None:
            raise NodeNotFound
        return Node(n)

    def _parse(self, source="mem", data=None, path=None, format=Format.XML, nosiblings=False,
                        strict=False, obsolete=False,
                        dataset=Dataset.DATA):
        opt = 0
        if nosiblings:
            opt |= lib.LYD_OPT_NOSIBLINGS
        if strict:
            opt |= lib.LYD_OPT_STRICT
        if obsolete:
            opt |= lib.LYD_OPT_OBSOLETE
        if not isinstance(dataset, Dataset):
            dataset = Dataset[dataset]
        opt |= dataset.value
        extraargs = [] # TODO
        if source == "mem":
            tree = lib.lyd_parse_mem(self._ctx, data, format.value, opt)
        elif source == "path":
            tree = lib.lyd_parse_path(self._ctx, path, format.value, opt)
        else:
            raise ValueError('Unknown source')
        if tree is None:
            raise ParseError
        return DataNode(tree)

    def parse(self, data, **kwargs):
        return self._parse(source="mem", data=data, **kwargs)

    def parse_path(self, path, **kwargs):
        return self._parse(source="path", path=path, **kwargs)
