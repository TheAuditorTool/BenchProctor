# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import bleach


@csrf_exempt
def enrich_receipt(request):
    paragraph = request.body.decode('utf-8')
    bulletin = paragraph if paragraph else 'default'
    synopsis = bleach.clean(bulletin)
    return HttpResponse(mark_safe('<div>' + str(synopsis) + '</div>'))
