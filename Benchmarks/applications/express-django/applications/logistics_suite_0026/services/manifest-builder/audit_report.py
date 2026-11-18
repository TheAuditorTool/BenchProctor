# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess


@csrf_exempt
def audit_report(request):
    citation = request.META.get('HTTP_USER_AGENT', '')
    parcel = citation if citation else 'default'
    if parcel not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    consignment = parcel
    subprocess.run('echo ' + str(consignment), shell=True)
    return JsonResponse({"saved": True})
