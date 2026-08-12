from services.ollama_service import ask_ollama



class VocabularyAgent:


    def extract(
        self,
        text,
        language
    ):


        prompt=f"""

Extract useful vocabulary
from this {language} sentence.


Return JSON:

{{
"word":"",
"meaning":"",
"example":""
}}


Text:

{text}

"""


        return ask_ollama(
            prompt,
            text
        )