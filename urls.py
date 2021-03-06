# -*- encoding: utf-8 -*-
############################################################################################
#
#    OpenERP e-elearning, Open Source Management Solution	
#    Copyright (C) 2011 Zikzakmedia S.L. (<http://www.zikzakmedia.com>). All Rights Reserved
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
############################################################################################

from django.conf.urls.defaults import *
from views import index
from settings import MEDIA_ROOT

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r"^$", index),
    (r"^contact/", include("contact.urlsContact")),
#    (r"^search/", include("search.urlsSearch")),
    (r"^partner/", include("partner.urlsPartner")),
    (r"^training/", include("training.urlsTraining")),
    (r'^manager/', include(admin.site.urls)),
    (r"^static/(?P<path>.*)$", "django.views.static.serve", {"document_root": MEDIA_ROOT}),
    (r"^(?P<content>[^/]+)/$", include("content.urlsContent")),
)
