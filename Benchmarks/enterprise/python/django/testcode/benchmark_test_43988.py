# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest43988(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    base_name = os.path.basename(str(forwarded_ip))
    try:
        os.remove('/var/app/data/' + base_name)
    except OSError:
        return JsonResponse({'error': 'file error'}, status=500)
    return JsonResponse({"saved": True})
