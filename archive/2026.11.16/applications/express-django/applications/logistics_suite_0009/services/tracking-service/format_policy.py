# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import yaml


@csrf_exempt
def format_policy(request):
    subject = request.GET.get('id', '')
    parcel, _sep, _rest = str(subject).partition('\x00')
    parsed = yaml.safe_load(parcel)
    return JsonResponse({'parsed': str(parsed)}, status=200)
