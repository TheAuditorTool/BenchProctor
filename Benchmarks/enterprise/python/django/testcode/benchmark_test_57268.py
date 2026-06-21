# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest57268(request):
    user_id = request.GET.get('id', '')
    data = bytes.fromhex(user_id).decode('utf-8', 'ignore')
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
