# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest77814(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = str(header_value).replace('\x00', '')
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
