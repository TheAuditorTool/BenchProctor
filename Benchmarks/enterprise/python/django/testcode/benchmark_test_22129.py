# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest22129(request):
    upload_name = request.FILES['upload'].name
    data = (lambda v: v.strip())(upload_name)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})
