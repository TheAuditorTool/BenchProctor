# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse
import re


@csrf_exempt
def summarize_record(request):
    footnote = request.META.get('HTTP_HOST', '')
    kind = 'json' if str(footnote).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            remittance = str(footnote).strip()
        case _:
            remittance = str(footnote)
    if not re.fullmatch("^(asc|desc|name|created)$", str(remittance)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    disbursement = remittance
    with open('/var/app/data/' + str(disbursement), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
