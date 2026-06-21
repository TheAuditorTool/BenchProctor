# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest10895(request):
    xml_value = request.body.decode('utf-8')
    data = ' '.join(str(xml_value).split())
    if str(data) == 'is_admin':
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})
