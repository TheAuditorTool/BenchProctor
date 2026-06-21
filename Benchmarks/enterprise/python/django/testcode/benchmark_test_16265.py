# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest16265(request):
    user_id = request.GET.get('id', '')
    data = '%s' % (user_id,)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
