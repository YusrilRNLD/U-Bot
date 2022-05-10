from telethon.tl.functions.channels import JoinChannelRequest as Get
from telethon.tl.types import MessageEntityMentionName
from userbot import RAM2, RAM3, RAM4, RAM5, bot
from .logger import logging
from .tools import edit_delete

LOGS = logging.getLogger(__name__)


async def get_user_from_event(
    event, ramevent=None, secondgroup=None, nogroup=False, noedits=False
):
    if ramevent is None:
        ramevent = event
    if nogroup is False:
        if secondgroup:
            args = event.pattern_match.group(2).split(" ", 1)
        else:
            args = event.pattern_match.group(1).split(" ", 1)
    extra = None
    try:
        if args:
            user = args[0]
            if len(args) > 1:
                extra = "".join(args[1:])
            if user.isnumeric() or (user.startswith("-") and user[1:].isnumeric()):
                user = int(user)
            if event.message.entities:
                probable_user_mention_entity = event.message.entities[0]
                if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                    user_id = probable_user_mention_entity.user_id
                    user_obj = await event.client.get_entity(user_id)
                    return user_obj, extra
            if isinstance(user, int) or user.startswith("@"):
                user_obj = await event.client.get_entity(user)
                return user_obj, extra
    except Exception as e:
        LOGS.error(str(e))
    try:
        if nogroup is False:
            if secondgroup:
                extra = event.pattern_match.group(2)
            else:
                extra = event.pattern_match.group(1)
        if event.is_private:
            user_obj = await event.get_chat()
            return user_obj, extra
        if event.reply_to_msg_id:
            previous_message = await event.get_reply_message()
            if previous_message.sender_id is None:
                if not noedits:
                    await edit_delete(
                        manevent, "**ERROR: Dia adalah anonymous admin!**", 60
                    )
                return None, None
            user_obj = await event.client.get_entity(previous_message.sender_id)
            return user_obj, extra
        if not args:
            if not noedits:
                await edit_delete(
                    ramevent,
                    "**KALO MALES REPLY PESAN NYA, MINIMAL KASIH ID YA NGENTOT KALO GAK USERNAME!!!**",
                    60,
                )
            return None, None
    except Exception as e:
        LOGS.error(str(e))
    if not noedits:
        await edit_delete(
            ramevent,
            "**KALO MALES REPLY PESAN NYA, MINIMAL KASIH ID YA NGENTOT KALO GAK USERNAME!!!**",
            60,
        )
    return None, None


async def hadeh_ajg():
    join = ("@Ramsupportt")
    dulu = ("@UserbotCh")
    try:
        if bot:
            await bot(Get(join))
            await bot(Get(dulu))
    except BaseException:
        pass
    try:
        if RAM2:
            await RAM2(Get(join))
            await RAM2(Get(dulu))
    except BaseException:
        pass
    try:
        if RAM3:
            await RAM3(Get(join))
            await RAM3(Get(dulu))
    except BaseException:
        pass
    try:
        if RAM4:
            await RAM4(Get(join))
            await RAM4(Get(dulu))
    except BaseException:
        pass
    try:
        if RAM5:
            await RAM5(Get(join))
            await RAM5(Get(dulu))
    except BaseException:
        pass
