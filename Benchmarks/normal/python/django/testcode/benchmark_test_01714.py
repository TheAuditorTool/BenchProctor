# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01714(request):
    user_id = request.GET.get('id', '')
    data = user_id if user_id else 'default'
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
