# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import bleach


@csrf_exempt
def enrich_index(request):
    transcript = request.body.decode('utf-8')
    backorder = transcript if transcript else 'default'
    restock = bleach.clean(backorder)
    return HttpResponse(mark_safe('<div>' + str(restock) + '</div>'))
