# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest57227(request):
    user_id = request.GET.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
