# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import yaml


@csrf_exempt
def resolve_schedule(request):
    preface = request.GET.get('id', '')
    handshake, _sep, _rest = str(preface).partition('\x00')
    parsed = yaml.safe_load(handshake)
    return JsonResponse({'parsed': str(parsed)}, status=200)
