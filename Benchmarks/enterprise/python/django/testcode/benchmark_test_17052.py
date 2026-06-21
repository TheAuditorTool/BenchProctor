# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def normalise_input(value):
    return value.strip()

def BenchmarkTest17052(request):
    user_id = request.GET.get('id', '')
    data = normalise_input(user_id)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
