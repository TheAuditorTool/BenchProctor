# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest53806(request):
    user_id = request.GET.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(user_id)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
