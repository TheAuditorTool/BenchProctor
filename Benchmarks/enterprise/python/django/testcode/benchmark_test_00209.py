# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00209(request):
    upload_name = request.FILES['upload'].name
    if upload_name:
        data = upload_name
    else:
        data = ''
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
