# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest65613(request):
    multipart_value = request.POST.get('multipart_field', '')
    return JsonResponse({'error': str(multipart_value), 'stack': repr(locals())}, status=500)
