# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest29733(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body:.200s}'
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    exec(str(processed))
    return JsonResponse({"saved": True})
