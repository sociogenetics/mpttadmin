# -*- coding: utf-8 -*-
from django.conf import settings

# ------------------------------------------------------------------------
# Admin media settings

#: Path to FeinCMS' admin media
FEINCMS_ADMIN_MEDIA = getattr(settings, 'FEINCMS_ADMIN_MEDIA', '/static/mpttadmin/')
#: Link to google APIs instead of using local copy of JS libraries
FEINCMS_ADMIN_MEDIA_HOTLINKING = getattr(settings, 'FEINCMS_ADMIN_MEDIA_HOTLINKING', False)

# ------------------------------------------------------------------------
# Settings for the page module

#: Include ancestors in filtered tree editor lists
FEINCMS_TREE_EDITOR_INCLUDE_ANCESTORS = getattr(settings, 'FEINCMS_TREE_EDITOR_INCLUDE_ANCESTORS', False)

#: Show frontend-editing button?
FEINCMS_FRONTEND_EDITING = getattr(settings, 'FEINCMS_FRONTEND_EDITING', True)

#: Enable checking of object level permissions. Note that if this option is enabled,
#: you must plug in an authentication backend that actually does implement object
#: level permissions or no page will be editable.
FEINCMS_TREE_EDITOR_OBJECT_PERMISSIONS = getattr(settings, 'FEINCMS_TREE_EDITOR_OBJECT_PERMISSIONS', False)