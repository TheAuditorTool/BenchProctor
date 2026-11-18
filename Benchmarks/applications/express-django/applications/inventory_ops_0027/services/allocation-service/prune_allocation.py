# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import Template, Context


@csrf_exempt
def prune_allocation(request):
    summary = request.META.get('HTTP_AUTHORIZATION', '')
    if summary:
        restock = summary
    else:
        restock = ''
    return HttpResponse(Template('{{ value }}').render(Context({'value': restock})))
