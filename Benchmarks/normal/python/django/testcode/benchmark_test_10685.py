# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest10685(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
