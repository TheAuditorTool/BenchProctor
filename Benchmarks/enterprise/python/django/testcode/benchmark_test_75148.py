# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest75148(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
