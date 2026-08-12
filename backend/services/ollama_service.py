import ollama



MODEL="qwen2.5"



def ask_ollama(
        system_prompt,
        message
):


    response = ollama.chat(

        model=MODEL,

        messages=[

            {
                "role":
                "system",

                "content":
                system_prompt
            },


            {
                "role":
                "user",

                "content":
                message
            }

        ]

    )


    return (
        response
        ["message"]
        ["content"]
    )