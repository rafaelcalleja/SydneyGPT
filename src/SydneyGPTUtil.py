from SydneyGPT import SydneyGPTBot
import EdgeGPT.EdgeGPT as EdgeGPT_module
from EdgeGPT.EdgeUtils import Query

create_method = EdgeGPT_module.Chatbot.create


async def new_create(*args, **kwargs):
    monkey_create = EdgeGPT_module.Chatbot.create
    try:
        EdgeGPT_module.Chatbot.create = create_method
        gpt_bot_create = SydneyGPTBot.create(*args, **kwargs)
        return await gpt_bot_create
    finally:
        EdgeGPT_module.Chatbot.create = monkey_create


EdgeGPT_module.Chatbot.create = staticmethod(new_create)


class SydneyQuery(Query):
    async def send_to_bing(self, *args, **kwargs) -> str:
        return await super().send_to_bing(*args, **kwargs)
