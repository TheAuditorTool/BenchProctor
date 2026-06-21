# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02143(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})
