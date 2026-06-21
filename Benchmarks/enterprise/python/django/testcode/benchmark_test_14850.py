# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest14850(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = multipart_value if multipart_value else 'default'
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})
