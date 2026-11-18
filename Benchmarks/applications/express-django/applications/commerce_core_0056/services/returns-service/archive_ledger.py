# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import Template, Context


@csrf_exempt
def archive_ledger(request):
    citation = request.META.get('HTTP_AUTHORIZATION', '')
    if citation:
        backorder = citation
    else:
        backorder = ''
    return HttpResponse(Template('{{ value }}').render(Context({'value': backorder})))
