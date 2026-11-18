# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import bleach


@csrf_exempt
def compact_record(request):
    citation = request.body.decode('utf-8')
    backorder = citation if citation else 'default'
    voucher = bleach.clean(backorder)
    return HttpResponse(mark_safe('<div>' + str(voucher) + '</div>'))
