# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest72436(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id:.200s}'
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
