# -*- coding: utf-8 -*-
from run import app


def test_ping():
    resp = app.test_client().get('/ping')
    assert resp.status_code == 200
