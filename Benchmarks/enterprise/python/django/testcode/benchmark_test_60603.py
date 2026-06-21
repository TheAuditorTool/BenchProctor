# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest60603(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    base_name = os.path.basename(str(auth_header))
    try:
        os.remove('/var/app/data/' + base_name)
    except OSError:
        return JsonResponse({'error': 'file error'}, status=500)
    return JsonResponse({"saved": True})
