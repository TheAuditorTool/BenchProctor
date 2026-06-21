# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest52322(request):
    upload_name = request.FILES['upload'].name
    prefix = ''
    data = prefix + str(upload_name)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
