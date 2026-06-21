# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest81498(request):
    user_id = request.GET.get('id', '')
    data = '{}'.format(user_id)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
