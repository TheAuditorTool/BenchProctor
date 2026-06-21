# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00266(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
