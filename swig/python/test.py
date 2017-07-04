from libyang import Context, ModuleNotFound
from libyang.schema import Leaf
import unittest
import os.path as path

search_dir = path.join(path.split(__file__)[0], 'files')

class TestContext(unittest.TestCase):
    def test_load_module(self):
        ctx = Context(search_dir)
        with self.assertRaises(ModuleNotFound):
            ctx.load_module('invalid')
        with self.assertRaises(ModuleNotFound):
            ctx.get_module('invalid')
        with self.assertRaises(ModuleNotFound):
            ctx.get_module('b')
        m = ctx.load_module('b')
    def test_get_node(self):
        ctx = Context(search_dir)
        ctx.load_module('b')
        node = ctx.get_node('/b:x/bar-leaf')
        self.assertEqual(node.name, 'bar-leaf')
        self.assertEqual(node.default, None)
        self.assertTrue(isinstance(node, Leaf))
    def test_parse(self):
        ctx = Context(search_dir)
        ctx.load_module('b')
        node = ctx.parse('<x xmlns="urn:b"><bubba>value</bubba></x>', dataset='GET')
        self.assertEqual(node.schema.name, 'x')
if __name__ == '__main__':
    unittest.main()
