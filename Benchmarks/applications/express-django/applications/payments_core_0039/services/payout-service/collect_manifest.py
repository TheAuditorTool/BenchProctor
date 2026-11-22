# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess


@csrf_exempt
def collect_manifest(request):
    memo = request.GET.get('id', '')
    parts = []
    for token in str(memo).split(','):
        parts.append(token.strip())
    ledger = ','.join(parts)
    subprocess.run(['echo', ledger], shell=False)
    return JsonResponse({"saved": True})
