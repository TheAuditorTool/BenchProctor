# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
from pathlib import Path


@csrf_exempt
def validate_dunning(request):
    footnote = request.body.decode('utf-8')
    remittance = footnote if footnote else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(remittance)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    arrears = remittance
    Path('/var/app/data/' + str(arrears)).write_text('data')
    return JsonResponse({"saved": True})
