# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest47106(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = f'{multipart_value}'
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
