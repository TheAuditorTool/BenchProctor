# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess


@csrf_exempt
def audit_roster(request):
    citation = request.META.get('HTTP_REFERER', '')
    def normalize(value):
        return value.strip()
    consignment = normalize(citation)
    subprocess.run('echo ' + str(consignment), shell=True)
    return JsonResponse({"saved": True})
