# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest46355(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = multipart_value if multipart_value else 'default'
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
