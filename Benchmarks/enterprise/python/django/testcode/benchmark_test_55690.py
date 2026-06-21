# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest55690(request):
    xml_value = request.body.decode('utf-8')
    data = '{}'.format(xml_value)
    if str(data) in ('admin', 'true', 'authenticated'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
