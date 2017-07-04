#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
import unittest
from run import app


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_ping(self):
        resp = self.app.get('/ping')
        assert resp.status_code == 200


if __name__ == '__main__':
    unittest.main()
