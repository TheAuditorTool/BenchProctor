# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest58754(request):
    xml_value = request.body.decode('utf-8')
    data = '%s' % str(xml_value)
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})
