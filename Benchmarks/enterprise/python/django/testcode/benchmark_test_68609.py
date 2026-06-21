# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest68609(request):
    user_id = request.GET.get('id', '')
    data = (lambda v: v.strip())(user_id)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
