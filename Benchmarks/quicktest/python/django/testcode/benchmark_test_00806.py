# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00806(request):
    xml_value = request.body.decode('utf-8')
    parts = []
    for token in str(xml_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    eval(str(data))
    return JsonResponse({"saved": True})
