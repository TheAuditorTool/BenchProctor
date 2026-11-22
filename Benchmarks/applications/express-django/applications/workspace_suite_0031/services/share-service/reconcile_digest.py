# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import Template, Context


@csrf_exempt
def reconcile_digest(request):
    caption = request.POST.get('field', '')
    if caption:
        synopsis = caption
    else:
        synopsis = ''
    return HttpResponse(Template('{{ value }}').render(Context({'value': synopsis})))
