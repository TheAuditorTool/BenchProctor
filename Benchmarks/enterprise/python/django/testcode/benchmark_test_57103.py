# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest57103(request):
    multipart_value = request.POST.get('multipart_field', '')
    parts = str(multipart_value).split(',')
    data = ','.join(parts)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
