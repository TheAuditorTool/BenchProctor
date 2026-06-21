# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest73369(request):
    user_id = request.GET.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(user_id)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
