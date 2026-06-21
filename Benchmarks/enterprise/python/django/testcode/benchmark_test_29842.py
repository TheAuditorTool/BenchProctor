# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest29842(request):
    multipart_value = request.POST.get('multipart_field', '')
    data, _sep, _rest = str(multipart_value).partition('\x00')
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
