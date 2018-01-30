from django.contrib import admin

from .models import Size
from .models import Tier
from .models import Maneuverability
from .models import Frame
from .models import Core
from .models import Thruster
from .models import Armor
from .models import Computer
from .models import CrewQuarter
from .models import Countermeasure
from .models import DriftEngine
from .models import ExpansionBay
from .models import Security
from .models import Sensors
from .models import Shields
from .models import Weapons

admin.site.register(Size),
admin.site.register(Tier),
admin.site.register(Maneuverability),
admin.site.register(Frame),
admin.site.register(Core),
admin.site.register(Thruster),
admin.site.register(Armor),
admin.site.register(Computer),
admin.site.register(CrewQuarter),
admin.site.register(Countermeasure),
admin.site.register(DriftEngine),
admin.site.register(ExpansionBay),
admin.site.register(Security),
admin.site.register(Sensors),
admin.site.register(Shields),
admin.site.register(Weapons),
