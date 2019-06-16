import xadmin
from xadmin import views
from users.models import MessageCode


class MessageCodeAdmin(object):
    list_display = ("mobile", "code", "add_time")
    search_field = ("mobile", "code")
    list_filter = ("mobile", "code", "add_time")


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobingSetting(object):

    site_title = '多多网的后台管理'
    site_footer = '技术支持@www.1449907540.com'
    menu_style = 'accordion'


xadmin.site.register(MessageCode, MessageCodeAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobingSetting)