# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest34369(request):
    user_id = request.GET.get('id', '')
    data = ' '.join(str(user_id).split())
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
