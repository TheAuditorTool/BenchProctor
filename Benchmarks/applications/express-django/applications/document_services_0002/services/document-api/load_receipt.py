# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse
import re


@csrf_exempt
def load_receipt(request):
    wording = request.META.get('HTTP_HOST', '')
    kind = 'json' if str(wording).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            addendum = str(wording).strip()
        case _:
            addendum = str(wording)
    if not re.fullmatch("^(asc|desc|name|created)$", str(addendum)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    dossier = addendum
    with open('/var/app/data/' + str(dossier), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
