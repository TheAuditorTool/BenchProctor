# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def merge_receipt(request):
    caption = request.META.get('HTTP_HOST', '')
    def normalize(value):
        return value.strip()
    ledger = normalize(caption)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if ledger not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    remittance = '/var/app/data/' + ledger
    os.unlink(remittance)
    return JsonResponse({"saved": True})
