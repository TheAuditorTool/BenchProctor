# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def BenchmarkTest11022(request):
    upload_name = request.FILES['upload'].name
    data = '%s' % str(upload_name)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
