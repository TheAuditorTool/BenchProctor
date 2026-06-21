# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09570(request):
    xml_value = request.body.decode('utf-8')
    data = f'{xml_value:.200s}'
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})
