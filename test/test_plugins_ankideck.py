# -*- coding: utf-8 -*-
__all__ = ["PluginsAnkiDeckTestCase"]
import unittest
from kanjidb_anki.builder.plugins import ankideck


class PluginsAnkiDeckTestCase(unittest.TestCase):
    def test(self):
        plugin = ankideck.Plugin()
        config = plugin.required_config
        config.update(
            {
            }
        )

        plugin.configure(global_config={}, plugin_config=config)


if __name__ == "__main__":
    unittest.main()
