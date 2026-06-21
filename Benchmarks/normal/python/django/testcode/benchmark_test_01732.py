# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest01732(request):
    xml_value = request.body.decode('utf-8')
    data = str(xml_value).replace('\x00', '')
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return JsonResponse({"saved": True})
