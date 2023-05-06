from config import read_config
from peewee import *
import datetime

config = read_config()
db = SqliteDatabase(config.get("database", "db_file"))


def connect():
    db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class UnknownField(object):
    def __init__(self, *_, **__):
        pass


class BaseModel(Model):
    class Meta:
        database = db


class SqliteDatabaseProperties(BaseModel):
    key = TextField(null=True, unique=True)
    value = TextField(null=True)

    class Meta:
        table_name = "_SqliteDatabaseProperties"
        primary_key = False


class Attachment(BaseModel):
    rowid = AutoField(column_name="ROWID", null=True)
    attribution_info = BlobField(null=True)
    ck_record_id = TextField(null=True)
    ck_server_change_token_blob = BlobField(null=True)
    ck_sync_state = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    created_date = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    filename = TextField(null=True)
    guid = TextField(unique=True)
    hide_attachment = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_commsafety_sensitive = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_outgoing = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_sticker = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    mime_type = TextField(null=True)
    original_guid = TextField(unique=True)
    start_date = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    sticker_user_info = BlobField(null=True)
    total_bytes = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    transfer_name = TextField(null=True)
    transfer_state = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    user_info = BlobField(null=True)
    uti = TextField(null=True)

    class Meta:
        table_name = "attachment"
        indexes = ((("hide_attachment", "ck_sync_state", "transfer_state"), False),)


class Chat(BaseModel):
    rowid = AutoField(column_name="ROWID", null=True)
    account_id = TextField(null=True)
    account_login = TextField(null=True)
    chat_identifier = TextField(index=True, null=True)
    ck_sync_state = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    cloudkit_record_id = TextField(null=True)
    display_name = TextField(null=True)
    engram_id = TextField(null=True)
    group_id = TextField(index=True, null=True)
    guid = TextField(unique=True)
    is_archived = IntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    is_blackholed = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_filtered = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_recovered = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    last_addressed_handle = TextField(null=True)
    last_addressed_sim_id = TextField(null=True)
    last_read_message_timestamp = IntegerField(
        constraints=[SQL("DEFAULT 0")], null=True
    )
    original_group_id = TextField(null=True)
    properties = BlobField(null=True)
    room_name = TextField(null=True)
    server_change_token = TextField(null=True)
    service_name = TextField(null=True)
    state = IntegerField(null=True)
    style = IntegerField(null=True)
    successful_query = IntegerField(null=True)
    syndication_date = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    syndication_type = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)

    def messages(self, limit=None):
        query = (
            Message.select()
            .join(ChatMessageJoin)
            .where(ChatMessageJoin.chat == self)
            .order_by(Message.date)
        )
        if limit is not None:
            query = query.limit(limit)
        return query

    class Meta:
        table_name = "chat"
        indexes = (
            (("chat_identifier", "service_name"), False),
            (("room_name", "service_name"), False),
        )


class Handle(BaseModel):
    rowid = AutoField(column_name="ROWID", null=True)
    country = TextField(null=True)
    id = TextField()
    person_centric_id = TextField(null=True)
    service = TextField()
    uncanonicalized_id = TextField(null=True)

    class Meta:
        table_name = "handle"
        indexes = ((("id", "service"), True),)


class ChatHandleJoin(BaseModel):
    chat = ForeignKeyField(column_name="chat_id", field="rowid", model=Chat, null=True)
    handle = ForeignKeyField(
        column_name="handle_id", field="rowid", model=Handle, null=True
    )

    class Meta:
        table_name = "chat_handle_join"
        indexes = ((("chat", "handle"), True),)
        primary_key = False


class Message(BaseModel):
    @property
    def chat(self):
        return self.chat_message_joins[0].chat

    rowid = AutoField(column_name="ROWID", null=True)
    account = TextField(null=True)
    account_guid = TextField(null=True)
    associated_message_guid = TextField(index=True, null=True)
    associated_message_range_length = IntegerField(
        constraints=[SQL("DEFAULT 0")], null=True
    )
    associated_message_range_location = IntegerField(
        constraints=[SQL("DEFAULT 0")], null=True
    )
    associated_message_type = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    attributed_body = BlobField(column_name="attributedBody", null=True)
    balloon_bundle_id = TextField(null=True)
    cache_has_attachments = IntegerField(
        constraints=[SQL("DEFAULT 0")], index=True, null=True
    )
    cache_roomnames = TextField(null=True)
    ck_record_change_tag = TextField(null=True)
    ck_record_id = TextField(null=True)
    ck_sync_state = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    country = TextField(null=True)
    date = DateTimeField()
    date_delivered = IntegerField(null=True)
    date_edited = IntegerField(null=True)
    date_played = IntegerField(null=True)
    date_read = IntegerField(null=True)
    date_retracted = IntegerField(null=True)
    destination_caller_id = TextField(null=True)
    did_notify_recipient = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    error = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    expire_state = IntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    expressive_send_style_id = TextField(null=True)
    group_action_type = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    group_title = TextField(null=True)
    guid = TextField(unique=True)
    handle_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    has_dd_results = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    has_unseen_mention = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_archive = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_audio_message = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_auto_reply = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_corrupt = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_delayed = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_delivered = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_emote = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_empty = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_expirable = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_finished = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_forward = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_from_me = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_kt_verified = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_played = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_prepared = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_read = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_sent = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_service_message = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_spam = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_stewie = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_system_message = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    item_type = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    message_action_type = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    message_source = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    message_summary_info = BlobField(null=True)
    other_handle = IntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    part_count = IntegerField(null=True)
    payload_data = BlobField(null=True)
    replace = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    reply_to_guid = TextField(null=True)
    service = TextField(null=True)
    service_center = TextField(null=True)
    share_direction = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    share_status = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    sort_id = IntegerField(null=True)
    subject = TextField(null=True)
    synced_syndication_ranges = TextField(null=True)
    syndication_ranges = TextField(null=True)
    text = TextField(null=True)
    thread_originator_guid = TextField(index=True, null=True)
    thread_originator_part = TextField(null=True)
    time_expressive_send_played = IntegerField(null=True)
    type = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    version = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    was_data_detected = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    was_deduplicated = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    was_delivered_quietly = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    was_detonated = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    was_downgraded = IntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)

    @property
    def formatted_date(self):
        # create the base datetime object for Jan 1, 2001
        base_datetime = datetime.datetime(2001, 1, 1)

        # calculate the number of seconds between Jan 1, 1970 and Jan 1, 2001
        base_timestamp = datetime.datetime(1970, 1, 1)
        seconds_diff = (base_datetime - base_timestamp).total_seconds()

        # convert the timestamp to a datetime object
        date = datetime.datetime.fromtimestamp((self.date / 1000000000) + seconds_diff)

        # convert to local timezone
        local_tz = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
        local_date = date.replace(tzinfo=datetime.timezone.utc).astimezone(local_tz)

        # format the date as string
        formatted_date = local_date.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_date

    class Meta:
        table_name = "message"
        indexes = (
            (
                (
                    "cache_roomnames",
                    "service",
                    "is_sent",
                    "is_delivered",
                    "was_downgraded",
                    "item_type",
                ),
                False,
            ),
            (("handle_id", "date"), False),
            (("is_finished", "is_from_me", "error"), False),
            (("is_read", "is_from_me", "is_finished"), False),
            (("is_read", "is_from_me", "item_type"), False),
            (("is_sent", "is_from_me", "error"), False),
        )


class ChatMessageJoin(BaseModel):
    chat = ForeignKeyField(
        column_name="chat_id",
        field="rowid",
        model=Chat,
        null=True,
        backref="chat_message_joins",
    )
    message_date = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    message = ForeignKeyField(
        column_name="message_id",
        field="rowid",
        model=Message,
        null=True,
        backref="chat_message_joins",
    )

    class Meta:
        table_name = "chat_message_join"
        indexes = (
            (("chat", "message"), True),
            (("chat", "message_date", "message"), False),
        )
        primary_key = CompositeKey("chat", "message")


class ChatRecoverableMessageJoin(BaseModel):
    chat = ForeignKeyField(column_name="chat_id", field="rowid", model=Chat, null=True)
    ck_sync_state = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    delete_date = IntegerField(null=True)
    message = ForeignKeyField(
        column_name="message_id", field="rowid", model=Message, null=True
    )

    class Meta:
        table_name = "chat_recoverable_message_join"
        indexes = ((("chat", "message"), True),)
        primary_key = CompositeKey("chat", "message")


class DeletedMessages(BaseModel):
    rowid = AutoField(column_name="ROWID", null=True)
    guid = TextField()

    class Meta:
        table_name = "deleted_messages"


class Kvtable(BaseModel):
    rowid = AutoField(column_name="ROWID", null=True)
    key = TextField(unique=True)
    value = BlobField()

    class Meta:
        table_name = "kvtable"


class MessageAttachmentJoin(BaseModel):
    attachment = ForeignKeyField(
        column_name="attachment_id", field="rowid", model=Attachment, null=True
    )
    message = ForeignKeyField(
        column_name="message_id", field="rowid", model=Message, null=True
    )

    class Meta:
        table_name = "message_attachment_join"
        indexes = ((("message", "attachment"), True),)
        primary_key = False


class MessageProcessingTask(BaseModel):
    rowid = AutoField(column_name="ROWID", null=True)
    guid = TextField()
    task_flags = IntegerField()

    class Meta:
        table_name = "message_processing_task"
        indexes = ((("guid", "task_flags"), False),)


class RecoverableMessagePart(BaseModel):
    chat = ForeignKeyField(column_name="chat_id", field="rowid", model=Chat, null=True)
    ck_sync_state = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    delete_date = IntegerField(null=True)
    message = ForeignKeyField(
        column_name="message_id", field="rowid", model=Message, null=True
    )
    part_index = IntegerField(null=True)
    part_text = BlobField()

    class Meta:
        table_name = "recoverable_message_part"
        indexes = ((("chat", "message", "part_index"), True),)
        primary_key = CompositeKey("chat", "message", "part_index")


class SqliteSequence(BaseModel):
    name = BareField(null=True)
    seq = BareField(null=True)

    class Meta:
        table_name = "sqlite_sequence"
        primary_key = False


class SyncDeletedAttachments(BaseModel):
    rowid = AutoField(column_name="ROWID", null=True)
    guid = TextField()
    record_id = TextField(column_name="recordID", null=True)

    class Meta:
        table_name = "sync_deleted_attachments"


class SyncDeletedChats(BaseModel):
    rowid = AutoField(column_name="ROWID", null=True)
    guid = TextField()
    record_id = TextField(column_name="recordID", null=True)
    timestamp = IntegerField(null=True)

    class Meta:
        table_name = "sync_deleted_chats"


class SyncDeletedMessages(BaseModel):
    rowid = AutoField(column_name="ROWID", null=True)
    guid = TextField()
    record_id = TextField(column_name="recordID", null=True)

    class Meta:
        table_name = "sync_deleted_messages"


class UnsyncedRemovedRecoverableMessages(BaseModel):
    rowid = AutoField(column_name="ROWID", null=True)
    chat_guid = TextField()
    message_guid = TextField()
    part_index = IntegerField(null=True)

    class Meta:
        table_name = "unsynced_removed_recoverable_messages"
