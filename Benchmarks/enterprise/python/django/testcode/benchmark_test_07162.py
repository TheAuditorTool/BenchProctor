# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest07162(request):
    user_id = request.GET.get('id', '')
    data = '%s' % str(user_id)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
