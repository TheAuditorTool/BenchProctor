# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest11248(request):
    user_id = request.GET.get('id', '')
    data = bytes.fromhex(user_id).decode('utf-8', 'ignore')
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    exec(str(processed))
    return JsonResponse({"saved": True})
