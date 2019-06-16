import xadmin
from user_operation.models import UserFav, UserMessage, UserAddress


class UserFavAdmin(object):
    list_display = ("user", "goods", "add_time")
    search_field = ("user", "goods")
    list_filter = ("user", "goods", "add_time")


class UserMessageAdmin(object):

    list_display = ("user", "message_type", "theme", "message", "files", "add_time")
    search_field = ("user", "message_type", "theme", "message", "files")
    list_filter = ("user", "message_type", "theme", "message", "files", "add_time")


class UserAddressAdmin(object):
    list_display = ("user", "name", "address", "detail_address", "mobile", "add_time")
    search_field = ("user", "name", "address", "detail_address", "mobile")
    list_filter = ("user", "name", "address", "detail_address", "mobile", "add_time")


xadmin.site.register(UserFav, UserFavAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserAddress, UserAddressAdmin)