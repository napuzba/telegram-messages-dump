from .ExporterContext import ExporterContext
from telethon.tl.custom.message import Message

class Exporter(object):
    def format(self, msg: Message, context : ExporterContext ) -> str:
        """ Formatter method. Takes raw msg and converts it to a *one-line* string.
            :param msg: Raw message object :class:`telethon.tl.types.Message` and derivatives.
                        https://core.telegram.org/type/Message
            :returns: *one-line* string containing one message data.
        """

    def begin_final_file(self, resulting_file, context: ExporterContext ) -> None:
        """ Hook executes at the beginning of writing a resulting file.
            (After BOM is written in case of --addbom)
        """
        pass