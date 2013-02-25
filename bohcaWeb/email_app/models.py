#from django.contrib.gis.db import models
from django.contrib.auth.models import User
#from django.contrib import admin
#from email_app.models import User 

RELATIONSHIP_FOLLOWING = 1
RELATIONSHIP_BLOCKED = 2
RELATIONSHIP_WAITING = 3
RELATIONSHIP_STATUSES = (
    (RELATIONSHIP_FOLLOWING, 'Following'),
    (RELATIONSHIP_BLOCKED, 'Blocked'),
    (RELATIONSHIP_WAITING, 'Waiting')
)


