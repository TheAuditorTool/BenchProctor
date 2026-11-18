# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
from pathlib import Path


@csrf_exempt
def prune_receipt(request):
    heading = request.body.decode('utf-8')
    if heading:
        voucher = heading
    else:
        voucher = ''
    base = Path('/var/app/data').resolve()
    candidate = (base / voucher).resolve()
    if base not in candidate.parents and candidate != base:
        return JsonResponse({'error': 'forbidden'}, status=403)
    backorder = str(candidate)
    os.unlink(backorder)
    return JsonResponse({"saved": True})
