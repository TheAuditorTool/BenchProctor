# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote


def BenchmarkTest57254(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = unquote(multipart_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
