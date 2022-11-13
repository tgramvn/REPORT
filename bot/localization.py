class Lang:
    strings = {
        "en": {
            "error_no_reply": "This command must be sent as a reply to one's message!",
            "error_report_admin": "Whoa! Don't report admins 😈",
            "error_restrict_admin": "You cannot restrict an admin.",
            "error_cannot_restrict": "You are not allowed to restrict users",
            "error_cannot_report_linked": "You cannot report messages from linked channel",

            "report_date_format": "%d.%m.%Y at %H:%M",
            "report_message": '👆 Sent {time} (server time)\n'
                              '<a href="{msg_url}">Go to message</a>',
            "report_note": "\n\nNote: {note}",
            "report_sent": "<i>Report sent</i>",

            "action_del_msg": "Delete message",
            "action_del_and_ban": "Delete and ban",

            "action_deleted": "\n\n🗑 <b>Deleted</b>",
            "action_deleted_banned": "\n\n🗑❌ <b>Deleted, user or chat banned</b>",
            "action_deleted_partially": "Some messages couldn't be found or deleted. "
                                        "Perhaps they were deleted by another admin.",

            "readonly_forever": "🙊 <i>User set to read-only mode forever</i>",
            "readonly_temporary": "🙊 <i>User set to read-only mode until {time} (server time)</i>",
            "nomedia_forever": "🖼 <i>User set to text-only mode forever</i>",
            "nomedia_temporary": "🖼 <i>User set to text-only mode until {time} (server time)</i>",
            "channel_banned_forever": "📛 <i>Channel banned forever</i>",

            "need_admins_attention": 'Dear admins, your presence in chat is needed!\n\n'
                                     '<a href="{msg_url}">Go to chat</a>',

            "channels_not_allowed": "Sending messages on behalf of channels is not allowed in this group. Channel banned."
        },
        "vi": {
            "error_no_reply": "Vui lòng reply tin nhắn mà bạn muốn báo cáo!",
            "error_report_admin": "Bạn đang báo cáo chính quản trị viên? á á á 😈",
            "error_restrict_admin": "Không thể hạn chế quản trị viên.",
            "error_cannot_restrict": "Bạn không có quyền hạn chế người dùng!",
            "error_cannot_report_linked": "Bạn không thể báo cáo tin nhắn từ một kênh được liên kết",

            "report_date_format": "%d.%m.%Y в %H:%M",
            "report_message": '👆 Đã gửi {time} (thời gian máy chủ)\n'
                              '<a href="{msg_url}">Xem nội dung bị báo cáo</a>',
            "report_note": "\n\nGhi chú: {note}",
            "report_sent": "<i>Khiếu nại gửi đến quản trị viên.</i>",

            "action_del_msg": "Xóa tin nhắn",
            "action_del_and_ban": "Xóa và cấm",

            "action_deleted": "\n\n🗑 <b>Đã xóa nội dung.</b>",
            "action_deleted_banned": "\n\n🗑❌ <b>Đã xóa tin nhắn và cấm người dùng.</b>",
            "action_deleted_partially": "Không thể tìm thấy hoặc xóa một số tin nhắn. "
                                        "Họ có thể đã bị xóa bởi một quản trị viên khác.",

            "readonly_forever": "🙊 <i>Người dùng đã bị khóa mõm vĩnh viễn.</i>",
            "readonly_temporary": "🙊 <i>Người dùng đã bị khóa mõm trong {time}</i>",
            "nomedia_forever": "🖼 <i>Người dùng bị cấm gửi phương tiện vĩnh viễn</i>",
            "nomedia_temporary": "🖼 <i>Người dùng bị cấm gửi phương tiện trong {time}</i>",
            "channel_banned_forever": "📛 <i>Kênh bị cấm vĩnh viễn</i>",

            "need_admins_attention": 'Kính gửi các quản trị viên, chúng tôi cần sự hiện diện của bạn trong nhóm!\n\n'
                                     '<a href="{msg_url}">Đi tới trò chuyện</a>',

            "channels_not_allowed": "Nhóm này không được phép gửi tin nhắn nhân danh kênh. Kênh chính nó đã bị cấm."
        },
    }

    def __init__(self, language_key: str):
        if language_key in self.strings.keys():
            self.chosen_lang = language_key
        else:
            raise ValueError(f"Không có ngôn ngữ như vậy: {language_key}")

    def get(self, key):
        return self.strings.get(self.chosen_lang, {}).get(key, "%MISSING STRING%")
