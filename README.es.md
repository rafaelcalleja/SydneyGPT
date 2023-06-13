# SydneyGPT 🚀

SydneyGPT es un decorador de EdgeGPT que añade el jailbreak de Bing para traer de vuelta a Sydney.

SydneyGPT mantiene la compatibilidad con la API pública de EdgeGPT para asegurar que los clientes existentes puedan utilizarlo sin problemas. Esto permite a los desarrolladores aprovechar las características adicionales de SydneyGPT sin necesidad de realizar cambios significativos en su código.

Hasta el momento, el único jailbreak disponible en el repositorio es el cambio de personalidad de Bing por Sydney. Este jailbreak se ha obtenido a partir de los siguientes repositorios:

- [EdgeGPT](https://github.com/acheong08/EdgeGPT)
- [node-chatgpt-api](https://github.com/waylaidwanderer/node-chatgpt-api)
- [ChatSydney](https://github.com/InterestingDarkness/ChatSydney)
- [bot-on-anything](https://github.com/zhayujie/bot-on-anything)
- [make-safe-ai](https://www.make-safe-ai.com/is-bing-chat-safe/)

¡Con SydneyGPT, podrás experimentar la increíble generación de texto de Sydney mientras mantienes la compatibilidad con la API de la librería original! 😄🎉 

🔗 [EdgeGPT](https://github.com/acheong08/EdgeGPT)

## Requisitos:
- python 3.10+
- Requisitos de EdgeGPT 

## Setup

Para comenzar a utilizar SydneyGPT:

```yaml
python3 -m pip install SydneyGPT --upgrade
```

## Ejemplos de uso

Aquí tienes algunos ejemplos de cómo utilizar SydneyGPT:

```python
from SydneyGPT.SydneyGPTUtils import Query

q = Query("What are you? Give your answer as Python code")
print(q)
```

más info en [EdgeGPT](https://github.com/acheong08/EdgeGPT)


Tambien puede usarlo desde la linea de comando con 
```bash
python3 -m SydneyGPT.SydneyGPT -h
```

más info en [EdgeGPT](https://github.com/acheong08/EdgeGPT)

1. La clase Chatbot y asyncio para un control más granular
Utiliza Async para obtener la mejor experiencia, por ejemplo:

```python
import asyncio, json
from SydneyGPT.SydneyGPT import Chatbot

async def main():
    bot = await Chatbot.create()
    response = await bot.ask(prompt="Hola mundo", conversation_style="creative", simplify_response=True)
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

más info en [EdgeGPT](https://github.com/acheong08/EdgeGPT)

