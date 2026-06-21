# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest53453(request):
    xml_value = request.body.decode('utf-8')
    data, _sep, _rest = str(xml_value).partition('\x00')
    if len(str(data)) >= 4:
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
