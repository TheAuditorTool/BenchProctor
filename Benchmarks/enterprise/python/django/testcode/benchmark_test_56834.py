# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest56834(request):
    host_value = request.META.get('HTTP_HOST', '')
    data, _sep, _rest = str(host_value).partition('\x00')
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    eval(str(processed))
    return JsonResponse({"saved": True})
