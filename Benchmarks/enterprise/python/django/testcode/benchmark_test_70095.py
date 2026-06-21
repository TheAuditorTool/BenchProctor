# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest70095(request):
    upload_name = request.FILES['upload'].name
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
