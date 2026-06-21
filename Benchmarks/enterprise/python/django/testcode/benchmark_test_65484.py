# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest65484(request):
    upload_name = request.FILES['upload'].name
    data = '%s' % str(upload_name)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
