# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest40791(request):
    user_id = request.GET.get('id', '')
    data = '{}'.format(user_id)
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
