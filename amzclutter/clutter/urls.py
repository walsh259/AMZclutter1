from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contact", views.contact, name="contact"),
    path("items", views.items, name="items"),
    path("potentials", views.potentials, name="potentials"),
    path("suppliers", views.suppliers, name="suppliers"),
    path("history", views.potentials, name="history"),
    path("designers", views.designers, name="designers"),
    path("files", views.potentials, name="files"),
    path("uploads", views.uploads, name="uploads"),
    path("products", views.products, name="products"),
    path("<int:product_id>", views.product, name="product"),
    path("supplier/<int:supplier_id>", views.supplier, name="supplier"),
    path("designer/<int:designer_id>", views.designer, name="designer"),
]
