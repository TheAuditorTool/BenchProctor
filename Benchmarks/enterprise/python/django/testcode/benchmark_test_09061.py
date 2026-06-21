# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09061(request):
    user_id = request.GET.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
