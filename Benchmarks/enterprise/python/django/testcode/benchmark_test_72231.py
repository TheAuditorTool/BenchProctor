# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile


def BenchmarkTest72231(request):
    xml_value = request.body.decode('utf-8')
    parts = str(xml_value).split(',')
    data = ','.join(parts)
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
