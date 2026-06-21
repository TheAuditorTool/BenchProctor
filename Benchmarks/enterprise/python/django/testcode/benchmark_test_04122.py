# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest04122(request):
    multipart_value = request.POST.get('multipart_field', '')
    parts = str(multipart_value).split(',')
    data = ','.join(parts)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
