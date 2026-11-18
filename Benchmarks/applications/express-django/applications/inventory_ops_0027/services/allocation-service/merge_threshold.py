# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import bleach


@csrf_exempt
def merge_threshold(request):
    summary = request.body.decode('utf-8')
    restock = summary if summary else 'default'
    backorder = bleach.clean(restock)
    return HttpResponse(mark_safe('<div>' + str(backorder) + '</div>'))
