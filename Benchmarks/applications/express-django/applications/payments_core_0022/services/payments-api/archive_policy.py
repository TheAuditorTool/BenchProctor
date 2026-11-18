# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess


@csrf_exempt
def archive_policy(request):
    subject = request.META.get('HTTP_USER_AGENT', '')
    ledger = subject if subject else 'default'
    if ledger not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    disbursement = ledger
    subprocess.run('echo ' + str(disbursement), shell=True)
    return JsonResponse({"saved": True})
