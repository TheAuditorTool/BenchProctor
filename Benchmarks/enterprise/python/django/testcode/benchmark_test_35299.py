# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest35299(request):
    upload_name = request.FILES['upload'].name
    prefix = ''
    data = prefix + str(upload_name)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})
