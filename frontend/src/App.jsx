import { useState } from "react";
import axios from "axios";
import "./App.css";


function App() {

  const [profile, setProfile] = useState(null);

  const [message, setMessage] = useState("");

  const [chat, setChat] = useState([]);

  const [correction, setCorrection] = useState(null);


  async function sendMessage() {

    if (!message.trim()) return;


    const userMessage = message;


    setChat(prev => [
      ...prev,
      {
        role: "user",
        text: userMessage
      }
    ]);


    setMessage("");


    try {

      const response = await axios.post(
        "http://127.0.0.1:8000/chat",
        {

          target_language:
          profile.target_language,

          native_language:
          profile.native_language,

          level:
          profile.level,

          interests:
          profile.interests,

          message:
          userMessage

        }
      );


      setChat(prev => [
        ...prev,
        {
          role:"assistant",
          text:
          response.data.reply
        }
      ]);


      setCorrection(
        response.data.red_pen
      );


    }

    catch(error){

      console.log(error);

      setChat(prev=>[
        ...prev,
        {
          role:"assistant",
          text:
          "Backend connection error."
        }
      ]);

    }

  }



  if(!profile){

    return (

      <div className="setup">

        <h1>
          LinguaMentor AI
        </h1>


        <h3>
          Choose your learning profile
        </h3>


        <button

        onClick={()=>

          setProfile({

            target_language:"German",

            native_language:"English",

            level:"A2",

            interests:[
              "travel",
              "food"
            ]

          })

        }

        >

        Start German A2 Tutor

        </button>


      </div>

    )

  }



  return (

    <div className="app">


      <h1>
        🇩🇪 German Tutor AI
      </h1>



      <div className="chat-box">


      {

      chat.map(
        (item,index)=>(

          <div
          key={index}
          className={item.role}
          >

          <b>
          {item.role}
          :
          </b>

          <p>
          {item.text}
          </p>

          </div>

        )
      )

      }


      </div>



      {
        correction &&

        <div className="redpen">

          <h3>
          ✎ Teacher Note
          </h3>

          <p>
          ❌ {correction.mistake}
          </p>

          <p>
          ✅ {correction.correction}
          </p>

          <p>
          {correction.explanation}
          </p>


        </div>
      }



      <div className="input-area">


      <input

      value={message}

      onChange={
        e=>setMessage(e.target.value)
      }

      placeholder=
      "Write in German..."

      />


      <button
      onClick={sendMessage}
      >

      Send

      </button>


      </div>



    </div>

  )

}


export default App;