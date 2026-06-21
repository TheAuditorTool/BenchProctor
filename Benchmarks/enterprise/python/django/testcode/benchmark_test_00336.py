# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00336(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
