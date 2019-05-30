from django.conf.urls import url
from django.contrib import admin
from face_detector import views

urlpatterns = (
    url(r'^face_detection/detect/$', views.detect),

    # url(r'^$', 'cv_api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', admin.site.urls),
)