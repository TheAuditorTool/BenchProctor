# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote


def BenchmarkTest39166(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = unquote(multipart_value)
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
