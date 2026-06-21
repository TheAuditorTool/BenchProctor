# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote


def BenchmarkTest04538(request):
    user_id = request.GET.get('id', '')
    data = unquote(user_id)
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
