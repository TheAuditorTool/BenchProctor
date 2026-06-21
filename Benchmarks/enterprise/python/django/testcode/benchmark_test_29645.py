# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest29645(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = '%s' % str(multipart_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
