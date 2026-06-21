# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest54144(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = (lambda v: v.strip())(auth_header)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    exec(str(processed))
    return JsonResponse({"saved": True})
