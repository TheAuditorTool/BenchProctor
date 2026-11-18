# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import bleach


@csrf_exempt
def normalize_dispute(request):
    headline = request.body.decode('utf-8')
    disbursement = headline if headline else 'default'
    remittance = bleach.clean(disbursement)
    return HttpResponse(mark_safe('<div>' + str(remittance) + '</div>'))
