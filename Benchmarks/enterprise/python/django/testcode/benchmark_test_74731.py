# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest74731(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id:.200s}'
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    exec(str(processed))
    return JsonResponse({"saved": True})
