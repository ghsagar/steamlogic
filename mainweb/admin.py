from django.contrib import admin

from .models import Gallery
from .models import Information
from .models import Testimonianls
from .models import Team
admin.site.register(Information)
admin.site.register(Gallery)
admin.site.register(Testimonianls)
admin.site.register(Team)


