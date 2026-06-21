# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02014(request):
    xml_value = request.body.decode('utf-8')
    data = '%s' % (xml_value,)
    if str(data) in ('admin', 'true', 'authenticated'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
