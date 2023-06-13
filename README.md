# SydneyGPT 🚀

SydneyGPT is an EdgeGPT decorator that adds the Bing jailbreak to bring Sydney back.

SydneyGPT maintains compatibility with the public EdgeGPT API to ensure that existing clients can use it seamlessly. This allows developers to take advantage of the additional features of SydneyGPT without the need for significant changes to their code.

Currently, the only available jailbreak in the repository is the personality swap from Bing to Sydney. This jailbreak has been obtained from the following repositories:

- [EdgeGPT](https://github.com/acheong08/EdgeGPT)
- [node-chatgpt-api](https://github.com/waylaidwanderer/node-chatgpt-api)
- [ChatSydney](https://github.com/InterestingDarkness/ChatSydney)
- [bot-on-anything](https://github.com/zhayujie/bot-on-anything)
- [make-safe-ai](https://www.make-safe-ai.com/is-bing-chat-safe/)

With SydneyGPT, you'll be able to experience Sydney's incredible text generation while maintaining compatibility with the original library's API! 😄🎉

🔗 [EdgeGPT](https://github.com/acheong08/EdgeGPT)

## Requirements:
- python 3.10+
- EdgeGPT Requirements

## Setup

To start using SydneyGPT:

```yaml
python3 -m pip install SydneyGPT --upgrade
```

## Usage Examples

Here are some examples of how to use SydneyGPT:

```python
from SydneyGPT.SydneyGPTUtils import Query

q = Query("What are you? Give your answer as Python code")
print(q)
```

More information available on [EdgeGPT](https://github.com/acheong08/EdgeGPT)


You can also use it from the command line with:

```bash
python3 -m SydneyGPT.SydneyGPT -h
```

More information available on [EdgeGPT](https://github.com/acheong08/EdgeGPT)

1. The Chatbot class and asyncio for finer control
Use Async for the best experience, for example:

```python
import asyncio, json
from SydneyGPT.SydneyGPT import Chatbot

async def main():
    bot = await Chatbot.create()
    response = await bot.ask(prompt="Hello world", conversation_style="creative", simplify_response=True)
    print(json.dumps(response, indent=2))
    """
    {
        "text": str
        "author": str
        "sources": list[dict]
        "sources_text": str
        "suggestions": list[str]
        "messages_left": int
    }
    """
    await bot.close()

if __name__ == "__main__":
    asyncio.run(main())
```

More information available on [EdgeGPT](https://github.com/acheong08/EdgeGPT)

