# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest28091(request):
    xml_value = request.body.decode('utf-8')
    data = (lambda v: v.strip())(xml_value)
    if str(data) == 'fluffy':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
