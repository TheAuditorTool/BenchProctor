# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def ensure_str(value):
    return str(value)

def BenchmarkTest02391(request):
    user_id = request.GET.get('id', '')
    data = ensure_str(user_id)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
