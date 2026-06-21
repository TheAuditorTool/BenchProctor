# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest41675(request):
    multipart_value = request.POST.get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
