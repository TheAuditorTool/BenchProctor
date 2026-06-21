# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest04542(request):
    upload_name = request.FILES['upload'].name
    def normalize(value):
        return value.strip()
    data = normalize(upload_name)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
