# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest33357(request):
    xml_value = request.body.decode('utf-8')
    data = xml_value if xml_value else 'default'
    if str(data).endswith(('/public', '/static', '/.')):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
