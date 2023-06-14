from django.urls import path
from .views import index, webpay_plus_create, webpay_plus_commit, webpay_plus_commit_error, webpay_plus_refund, webpay_plus_refund_form

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('webpay-plus/create', webpay_plus_create, name='webpay_plus_create'),
    path('webpay-plus/commit', webpay_plus_commit, name='webpay_plus_commit'),
    path('webpay-plus/commit-error', webpay_plus_commit_error, name='webpay_plus_commit_error'),
    path('webpay-plus/refund', webpay_plus_refund, name='webpay_plus_refund'),
    path('webpay-plus/refund-form', webpay_plus_refund_form, name='webpay_plus_refund_form'),
]
