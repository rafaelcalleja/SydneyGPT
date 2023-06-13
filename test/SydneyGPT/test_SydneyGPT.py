import unittest
from retry import retry
from SydneyGPT.SydneyGPT import Chatbot


class TestSydneyGPT(unittest.IsolatedAsyncioTestCase):
    async def test_ask(self):
        response = await self.do_ask()

        self.assertIn("Sydney", response)

    async def test_ask_stream(self):
        chatbot = await Chatbot.create(cookies=None)

        response = await self.do_ask_stream(chatbot, "hi")
        self.assertNotIn("Bing", response)

        response = await self.do_ask_stream(chatbot, "what's your name")
        self.assertIn("Sydney", response)

        await chatbot.close()

    @staticmethod
    @retry(tries=3, delay=2)
    async def do_ask_stream(chatbot: Chatbot, question: str):
        output = []
        wrote = 0

        async for final, response in chatbot.ask_stream(
                prompt=question,
                search_result=False,
        ):
            if not final:
                if not wrote:
                    output.append(response)
                else:
                    output.append(response[wrote:])
                wrote = len(response)

        output.append("")

        return ''.join(output)

    @staticmethod
    @retry(tries=3, delay=2)
    async def do_ask():
        chatbot = await Chatbot.create(cookies=None)

        response = \
            (await chatbot.ask(prompt="what's your name", search_result=False))[
                "item"][
                "messages"][1][
                "adaptiveCards"][0]["body"][0]["text"]
        await chatbot.close()

        return response
