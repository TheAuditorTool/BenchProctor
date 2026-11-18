# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import yaml


@csrf_exempt
def audit_quota(request):
    notice = request.GET.get('id', '')
    persona, _sep, _rest = str(notice).partition('\x00')
    parsed = yaml.safe_load(persona)
    return JsonResponse({'parsed': str(parsed)}, status=200)
