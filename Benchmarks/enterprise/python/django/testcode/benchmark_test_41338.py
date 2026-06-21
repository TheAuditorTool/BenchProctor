# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest41338(request):
    user_id = request.GET.get('id', '')
    data = '%s' % (user_id,)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
