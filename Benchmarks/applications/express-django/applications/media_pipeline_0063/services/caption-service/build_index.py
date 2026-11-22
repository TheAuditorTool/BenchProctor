# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import Template, Context


@csrf_exempt
def build_index(request):
    snippet = request.POST.get('field', '')
    if snippet:
        montage = snippet
    else:
        montage = ''
    return HttpResponse(Template('{{ value }}').render(Context({'value': montage})))
