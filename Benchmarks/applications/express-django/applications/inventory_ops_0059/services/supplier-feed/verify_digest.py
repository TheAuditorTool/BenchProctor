# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
import re


@csrf_exempt
def verify_digest(request):
    memo = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    backorder = bytes.fromhex(memo).decode('utf-8', 'ignore')
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", backorder):
        return JsonResponse({'error': 'forbidden'}, status=400)
    restock = backorder
    os.unlink('/var/app/data/' + str(restock))
    return JsonResponse({"saved": True})
