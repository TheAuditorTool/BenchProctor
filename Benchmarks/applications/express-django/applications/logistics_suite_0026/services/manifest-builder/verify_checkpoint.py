# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import os
import re


@csrf_exempt
def verify_checkpoint(request):
    citation = os.environ.get('SHIPPING_INPUT_0026', '')
    parcel = citation if citation else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(parcel)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    consignment = parcel
    subprocess.run('echo ' + str(consignment), shell=True)
    return JsonResponse({"saved": True})
