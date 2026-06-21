# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest56179(request):
    xml_value = request.body.decode('utf-8')
    data = ' '.join(str(xml_value).split())
    if str(data).endswith(('/public', '/static', '/.')):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
