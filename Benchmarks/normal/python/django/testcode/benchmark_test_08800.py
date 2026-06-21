# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def relay_value(value):
    return value

def BenchmarkTest08800(request):
    user_id = request.GET.get('id', '')
    data = relay_value(user_id)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
