# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote


def BenchmarkTest25164(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = unquote(multipart_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
