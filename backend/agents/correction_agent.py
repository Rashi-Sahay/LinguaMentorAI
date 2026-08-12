from services.ollama_service import ask_ollama



class CorrectionAgent:


    def analyze(
        self,
        sentence,
        language
    ):


        prompt=f"""

You are a grammar correction teacher.


Language:
{language}


Analyze this sentence:

"{sentence}"


Return JSON only:

{{
"mistake":"",
"correction":"",
"explanation":""
}}

"""


        return ask_ollama(
            prompt,
            sentence
        )