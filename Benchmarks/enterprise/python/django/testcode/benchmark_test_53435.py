# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def BenchmarkTest53435(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
