# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree
from types import SimpleNamespace


async def BenchmarkTest15385(request: Request):
    ua_value = request.headers.get('user-agent', '')
    ns = SimpleNamespace(payload=ua_value)
    data = getattr(ns, 'payload')
    eval(compile('tree = etree.fromstring(b\'<users><user name="admin"/></users>\')\ntree.xpath(\'/users/user[name="\' + str(data) + \'"]\')', '<sink>', 'exec'))
    return {"updated": True}
