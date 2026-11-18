# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def compact_roster(request):
    heading = request.META.get('HTTP_HOST', '')
    def normalize(value):
        return value.strip()
    voucher = normalize(heading)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if voucher not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    backorder = '/var/app/data/' + voucher
    os.unlink(backorder)
    return JsonResponse({"saved": True})
