# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest21271(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    base_name = os.path.basename(str(header_value))
    try:
        os.remove('/var/app/data/' + base_name)
    except OSError:
        return JsonResponse({'error': 'file error'}, status=500)
    return JsonResponse({"saved": True})
