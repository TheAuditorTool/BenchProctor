# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import bleach


@csrf_exempt
def fetch_ledger(request):
    blurb = request.body.decode('utf-8')
    handshake = blurb if blurb else 'default'
    citation = bleach.clean(handshake)
    return HttpResponse(mark_safe('<div>' + str(citation) + '</div>'))
