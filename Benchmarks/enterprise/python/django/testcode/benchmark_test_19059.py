# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest19059(request):
    user_id = request.GET.get('id', '')
    data = (lambda v: v.strip())(user_id)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
