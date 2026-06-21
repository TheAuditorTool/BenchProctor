# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest68629(request):
    upload_name = request.FILES['upload'].name
    data, _sep, _rest = str(upload_name).partition('\x00')
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
