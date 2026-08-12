from services.ollama_service import ask_ollama



class TutorAgent:


    def __init__(
            self,
            target_language,
            native_language,
            level,
            interests
    ):


        self.target_language=target_language

        self.native_language=native_language

        self.level=level

        self.interests=interests



    def chat(
            self,
            message
    ):


        prompt=f"""

You are a professional
{self.target_language} teacher.


Student:

Native language:
{self.native_language}


Level:
{self.level}


Interests:
{self.interests}



Rules:

- Speak mostly {self.target_language}
- Adapt grammar to student level
- Ask questions
- Encourage conversation
- Do not explain mistakes now
- Another agent will correct errors


"""


        return ask_ollama(
            prompt,
            message
        )