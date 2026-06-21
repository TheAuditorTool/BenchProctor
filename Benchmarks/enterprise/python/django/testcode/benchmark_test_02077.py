# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def BenchmarkTest02077(request):
    user_id = request.GET.get('id', '')
    data = '%s' % str(user_id)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
