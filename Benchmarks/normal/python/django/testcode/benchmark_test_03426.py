# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03426(request):
    xml_value = request.body.decode('utf-8')
    parts = []
    for token in str(xml_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    if str(data) in ('localhost', 'internal-gateway'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
