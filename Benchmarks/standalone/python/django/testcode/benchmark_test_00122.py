# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
from urllib.parse import unquote


def BenchmarkTest00122(request):
    user_id = request.GET.get('id', '')
    data = unquote(user_id)
    parsed = yaml.safe_load(data)
    return JsonResponse({'parsed': str(parsed)}, status=200)
