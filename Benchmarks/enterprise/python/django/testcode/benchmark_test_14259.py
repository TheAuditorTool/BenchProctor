# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest14259(request):
    xml_value = request.body.decode('utf-8')
    if xml_value:
        data = xml_value
    else:
        data = ''
    if len(str(data)) >= 4:
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
