from django.shortcuts import render
from django.views import View
from store.models.product import Products


class ItemDetailView(View):
    def get(self, request, pk):
        product = Products.objects.get(pk=pk)
        context = {"product": product}
        return render(request, "item_detail.html", context)
