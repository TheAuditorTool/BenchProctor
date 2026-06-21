# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree
import os


async def BenchmarkTest27180(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return {"updated": True}
