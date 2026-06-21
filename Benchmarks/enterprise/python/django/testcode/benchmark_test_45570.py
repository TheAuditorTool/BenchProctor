# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest45570(request):
    upload_name = request.FILES['upload'].name
    data = f'{upload_name}'
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
