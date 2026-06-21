# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest05458(request):
    multipart_value = request.POST.get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})
