import streamlit

import streamlit as st
import streamlit.components.v1 as components

# flowise chatbot
components.html(
  <flowise-fullchatbot></flowise-fullchatbot>
<script type="module">
    import Chatbot from "https://cdn.jsdelivr.net/npm/flowise-embed/dist/web.js"
    Chatbot.initFull({
        chatflowid: "2da51f59-dc6b-45f7-a032-66598b1af915",
        apiHost: "https://kognitio.onrender.com",
    })
</script>
)
