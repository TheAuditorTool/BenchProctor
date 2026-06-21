# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


async def BenchmarkTest09952(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = '%s' % str(multipart_value)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(processed) + '"]')
    return {"updated": True}
