from SydneyGPT import SydneyGPTBot
import EdgeGPT.EdgeGPT as EdgeGPT_module
from EdgeGPT.EdgeUtils import Query as BaseQuery

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


class Query(BaseQuery):
    pass

