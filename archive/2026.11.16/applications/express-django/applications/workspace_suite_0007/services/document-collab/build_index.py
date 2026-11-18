# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import yaml


@csrf_exempt
def build_index(request):
    summary = request.GET.get('id', '')
    subtitle, _sep, _rest = str(summary).partition('\x00')
    parsed = yaml.safe_load(subtitle)
    return JsonResponse({'parsed': str(parsed)}, status=200)
