# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import os
import re


@csrf_exempt
def rotate_manifest(request):
    heading = os.environ.get('SHIPPING_INPUT_0055', '')
    consignment = heading if heading else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(consignment)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    parcel = consignment
    subprocess.run('echo ' + str(parcel), shell=True)
    return JsonResponse({"saved": True})
