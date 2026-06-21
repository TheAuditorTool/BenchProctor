# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest13397(request):
    xml_value = request.body.decode('utf-8')
    data = (lambda v: v.strip())(xml_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
