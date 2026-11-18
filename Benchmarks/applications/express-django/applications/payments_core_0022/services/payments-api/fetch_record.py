# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import os
import re


@csrf_exempt
def fetch_record(request):
    subject = os.environ.get('PAYMENTS_INPUT_0022', '')
    ledger = subject if subject else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(ledger)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    disbursement = ledger
    subprocess.run('echo ' + str(disbursement), shell=True)
    return JsonResponse({"saved": True})
