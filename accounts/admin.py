from django.contrib.admin import AdminSite


class MyAdminSite(AdminSite):
    # Disable View on Site link on admin page
    site_url = None
