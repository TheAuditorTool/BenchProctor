# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest50850(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    if origin_value not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = origin_value
    os.unlink('/var/app/data/' + str(processed))
    return JsonResponse({"saved": True})
