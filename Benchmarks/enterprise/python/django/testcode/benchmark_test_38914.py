# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest38914(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id}'
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
