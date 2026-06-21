# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02194(request):
    raw_body = request.body.decode('utf-8')
    parts = str(raw_body).split(',')
    data = ','.join(parts)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    eval(str(processed))
    return JsonResponse({"saved": True})
