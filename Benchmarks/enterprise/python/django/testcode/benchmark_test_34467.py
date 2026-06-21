# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest34467(request):
    user_id = request.GET.get('id', '')
    return JsonResponse({'error': str(user_id), 'stack': repr(locals())}, status=500)
