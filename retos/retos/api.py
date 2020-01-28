from rest_framework import routers
from generales import views as myapp_views

router = routers.DefaultRouter()
router.register(r'teams', myapp_views.TeamViewset)
router.register(r'categories-teams', myapp_views.CategoryTeamViewset)
router.register(r'kindof-teams', myapp_views.KindOfTeamViewset)