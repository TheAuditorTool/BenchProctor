# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest17212(request):
    multipart_value = request.POST.get('multipart_field', '')
    def normalize(value):
        return value.strip()
    data = normalize(multipart_value)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})
