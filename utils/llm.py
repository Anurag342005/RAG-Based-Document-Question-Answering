from groq import Groq
from config import GROQ_API_KEY, LLM_MODEL
from utils.prompt import PROMPT_TEMPLATE


class LLM:

    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)

    def generate(self, question, docs):

        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )

        prompt = PROMPT_TEMPLATE.format(
            context=context,
            question=question
        )

        response = self.client.chat.completions.create(

            model=LLM_MODEL,

            temperature=0,

            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful RAG assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]

        )

        return response.choices[0].message.content