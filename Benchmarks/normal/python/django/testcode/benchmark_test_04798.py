# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest04798(request):
    xml_value = request.body.decode('utf-8')
    try:
        os.setuid(int(str(xml_value)) if str(xml_value).isdigit() else 65534)
    except OSError:
        return JsonResponse({'error': 'privilege drop failed'}, status=500)
    return JsonResponse({"saved": True})
