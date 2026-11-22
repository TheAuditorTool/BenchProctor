# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse
import re


@csrf_exempt
def verify_threshold(request):
    transcript = request.META.get('HTTP_HOST', '')
    kind = 'json' if str(transcript).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            consignment = str(transcript).strip()
        case _:
            consignment = str(transcript)
    if not re.fullmatch("^(asc|desc|name|created)$", str(consignment)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    parcel = consignment
    with open('/var/app/data/' + str(parcel), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
