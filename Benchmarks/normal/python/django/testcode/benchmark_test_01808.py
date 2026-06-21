# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01808(request):
    upload_name = request.FILES['upload'].name
    globals().setdefault('_secret_cache', {})['current'] = str(upload_name)
    return JsonResponse({"saved": True})
