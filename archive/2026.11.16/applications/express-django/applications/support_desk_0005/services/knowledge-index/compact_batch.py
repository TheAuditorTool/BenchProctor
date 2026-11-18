# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import yaml


@csrf_exempt
def compact_batch(request):
    phrase = request.GET.get('id', '')
    inquiry, _sep, _rest = str(phrase).partition('\x00')
    parsed = yaml.safe_load(inquiry)
    return JsonResponse({'parsed': str(parsed)}, status=200)
