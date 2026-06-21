# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09358(request):
    user_id = request.GET.get('id', '')
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(user_id)})
