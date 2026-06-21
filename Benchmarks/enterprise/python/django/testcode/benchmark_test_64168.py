# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def relay_value(value):
    return value

def BenchmarkTest64168(request):
    upload_name = request.FILES['upload'].name
    data = relay_value(upload_name)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
