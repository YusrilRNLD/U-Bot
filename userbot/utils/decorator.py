# Credits: @mrconfused
# Recode by @mrismanaziz
# FROM RAM - UBOT <https://github.com/ramadhani892/RAM-UBOT>

import inspect
import re
from pathlib import Path

from telethon import events

from userbot import (
    BL_CHAT,
    CMD_HANDLER,
    CMD_LIST,
    LOAD_PLUG,
    RAM2,
    RAM3,
    RAM4,
    RAM5,
    SUDO_HANDLER,
    SUDO_USERS,
    bot,
    tgbot,
)


def ram_cmd(
    pattern: str = None,
    allow_sudo: bool = True,
    disable_edited: bool = False,
    forword=False,
    command: str = None,
    **args,
):
    args["func"] = lambda e: e.via_bot_id is None
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")

    if "disable_edited" in args:
        del args["disable_edited"]

    args["blacklist_chats"] = True
    black_list_chats = list(BL_CHAT)
    if len(black_list_chats) > 0:
        args["chats"] = black_list_chats

    if pattern is not None:
        global ram_reg
        global sudo_reg
        if (
            pattern.startswith(r"\#")
            or not pattern.startswith(r"\#")
            and pattern.startswith(r"^")
        ):
            ram_reg = sudo_reg = re.compile(pattern)
        else:
            ram_ = "\\" + CMD_HANDLER
            sudo_ = "\\" + SUDO_HANDLER
            ram_reg = re.compile(ram_ + pattern)
            sudo_reg = re.compile(sudo_ + pattern)
            if command is not None:
                cmd1 = ram_ + command
                cmd2 = sudo_ + command
            else:
                cmd1 = (
                    (ram_ + pattern).replace("$", "").replace("\\", "").replace("^", "")
                )
                cmd2 = (
                    (sudo_ + pattern)
                    .replace("$", "")
                    .replace("\\", "")
                    .replace("^", "")
                )
            try:
                CMD_LIST[file_test].append(cmd1)
            except BaseException:
                CMD_LIST.update({file_test: [cmd1]})

    def decorator(func):
        if bot:
            if not disable_edited:
                bot.add_event_handler(
                    func, events.MessageEdited(**args, outgoing=True, pattern=ram_reg)
                )
            bot.add_event_handler(
                func, events.NewMessage(**args, outgoing=True, pattern=ram_reg)
            )
        if bot:
            if allow_sudo:
                if not disable_edited:
                    bot.add_event_handler(
                        func,
                        events.MessageEdited(
                            **args, from_users=list(SUDO_USERS), pattern=sudo_reg
                        ),
                    )
                bot.add_event_handler(
                    func,
                    events.NewMessage(
                        **args, from_users=list(SUDO_USERS), pattern=sudo_reg
                    ),
                )
        if RAM2:
            if not disable_edited:
                RAM2.add_event_handler(
                    func, events.MessageEdited(**args, outgoing=True, pattern=ram_reg)
                )
            RAM2.add_event_handler(
                func, events.NewMessage(**args, outgoing=True, pattern=ram_reg)
            )
        if RAM3:
            if not disable_edited:
                RAM3.add_event_handler(
                    func, events.MessageEdited(**args, outgoing=True, pattern=ram_reg)
                )
            RAM3.add_event_handler(
                func, events.NewMessage(**args, outgoing=True, pattern=ram_reg)
            )
        if RAM4:
            if not disable_edited:
                RAM4.add_event_handler(
                    func, events.MessageEdited(**args, outgoing=True, pattern=ram_reg)
                )
            RAM4.add_event_handler(
                func, events.NewMessage(**args, outgoing=True, pattern=ram_reg)
            )
        if RAM5:
            if not disable_edited:
                RAM5.add_event_handler(
                    func, events.MessageEdited(**args, outgoing=True, pattern=ram_reg)
                )
            RAM5.add_event_handler(
                func, events.NewMessage(**args, outgoing=True, pattern=ram_reg)
            )
        try:
            LOAD_PLUG[file_test].append(func)
        except Exception:
            LOAD_PLUG.update({file_test: [func]})
        return func

    return decorator


def ram_handler(
    **args,
):
    def decorator(func):
        if bot:
            bot.add_event_handler(func, events.NewMessage(**args))
        if RAM2:
            RAM2.add_event_handler(func, events.NewMessage(**args))
        if RAM3:
            RAM3.add_event_handler(func, events.NewMessage(**args))
        if RAM4:
            RAM4.add_event_handler(func, events.NewMessage(**args))
        if RAM5:
            RAM5.add_event_handler(func, events.NewMessage(**args))
        return func

    return decorator


def asst_cmd(**args):
    pattern = args.get("pattern", None)
    r_pattern = r"^[/!]"
    if pattern is not None and not pattern.startswith("(?i)"):
        args["pattern"] = "(?i)" + pattern
    args["pattern"] = pattern.replace("^/", r_pattern, 1)

    def decorator(func):
        if tgbot:
            tgbot.add_event_handler(func, events.NewMessage(**args))
        return func

    return decorator


def chataction(**args):
    def decorator(func):
        if bot:
            bot.add_event_handler(func, events.ChatAction(**args))
        if RAM2:
            RAM2.add_event_handler(func, events.ChatAction(**args))
        if RAM3:
            RAM3.add_event_handler(func, events.ChatAction(**args))
        if RAM4:
            RAM4.add_event_handler(func, events.ChatAction(**args))
        if RAM5:
            RAM5.add_event_handler(func, events.ChatAction(**args))
        return func

    return decorator


def callback(**args):
    def decorator(func):
        if tgbot:
            tgbot.add_event_handler(func, events.CallbackQuery(**args))
        return func

    return decorator
