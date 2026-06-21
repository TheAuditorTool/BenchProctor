# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09440(request):
    user_id = request.GET.get('id', '')
    data = user_id if user_id else 'default'
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
