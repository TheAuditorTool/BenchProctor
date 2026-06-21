# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest05905(request):
    user_id = request.GET.get('id', '')
    data = ' '.join(str(user_id).split())
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
