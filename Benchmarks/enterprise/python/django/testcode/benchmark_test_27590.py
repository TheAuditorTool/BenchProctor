# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest27590(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = '{}'.format(multipart_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
