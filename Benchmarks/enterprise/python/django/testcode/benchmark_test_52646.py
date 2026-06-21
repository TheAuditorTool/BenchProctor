# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest52646(request):
    user_id = request.GET.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    exec(str(processed))
    return JsonResponse({"saved": True})
