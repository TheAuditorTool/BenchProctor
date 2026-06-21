# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest34600(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = header_value if header_value else 'default'
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
