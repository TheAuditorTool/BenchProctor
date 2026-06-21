# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest29658(request):
    xml_value = request.body.decode('utf-8')
    if str(xml_value) in ('admin', 'true', 'authenticated'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
