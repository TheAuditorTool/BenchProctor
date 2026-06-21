# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest10550(request):
    upload_name = request.FILES['upload'].name
    data = ' '.join(str(upload_name).split())
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})
