# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest45506(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body:.200s}'
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
