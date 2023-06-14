import random
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from transbank.error.transbank_error import TransbankError
from transbank.webpay.webpay_plus.transaction import Transaction


def index(request):
    return render(request, 'index.html')

from .models import Item

@csrf_exempt
def webpay_plus_create(request):
    print("Webpay Plus Transaction.create")
    buy_order = str(random.randrange(1000000, 99999999))
    session_id = str(random.randrange(1000000, 99999999))
    amount = random.randrange(10000, 1000000)
    return_url = request.build_absolute_uri('/webpay-plus/commit')

    # Get the list of items from the database
    items = Item.objects.all()

    create_request = {
        "buy_order": buy_order,
        "session_id": session_id,
        "amount": amount,
        "return_url": return_url
    }

    response = (Transaction()).create(buy_order, session_id, amount, return_url)

    print(response)

    context = {
        'request': create_request,
        'response': response,
        'items': items,
    }

    return render(request, 'webpay/plus/create.html', context)



@csrf_exempt
def webpay_plus_commit(request):
    token = request.GET.get("token_ws")
    print("commit for token_ws: {}".format(token))

    response = (Transaction()).commit(token=token)
    print("response: {}".format(response))

    return render(request, 'webpay/plus/commit.html', {'token': token, 'response': response})


@csrf_exempt
def webpay_plus_commit_error(request):
    token = request.POST.get("token_ws")
    print("commit error for token_ws: {}".format(token))

    response = {
        "error": "Transacción con errores"
    }

    return render(request, 'webpay/plus/commit.html', {'token': token, 'response': response})


@csrf_exempt
def webpay_plus_refund(request):
    token = request.POST.get("token_ws")
    amount = request.POST.get("amount")
    print("refund for token_ws: {} by amount: {}".format(token, amount))

    try:
        response = (Transaction()).refund(token, amount)
        print("response: {}".format(response))

        return render(request, "webpay/plus/refund.html", {'token': token, 'amount': amount, 'response': response})
    except TransbankError as e:
        print(e.message)


def webpay_plus_refund_form(request):
    return render(request, "webpay/plus/refund-form.html")
