import React, { useEffect, useState, useCallback } from "react";
import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import { load_image, train_model, streaming_call } from "./services/restapi";
import Home from "pages/home";
import Layout from "pages/layout";
import About from "pages/about";
import NoMatch from "pages/nomatch";
import { config } from "configs";
import useWebSocket from "react-use-websocket";

function App() {
  const [websocket_greeting, setWebsocketGreeting] = useState("");
  const { sendMessage } = useWebSocket(config["websocketApiBaseUrl"], {
    onOpen: () => console.log("opened"),
    onMessage: (evt) => setWebsocketGreeting(evt.data),
    //Will attempt to reconnect on all close events, such as server shutting down
    shouldReconnect: (closeEvent) => true,
  });

  const [logs, setLogs] = useState("");
  const clickHandlerLoadImage = useCallback(() => load_image(), []);
  const clickHandlerStartTraining = useCallback(() => train_model('print("hello world")'), []);

  const code = 'print("hello world")'
  var source = new EventSource(config["restApiBaseUrl"] + `api/v1/trainer/train_model?code=${code}`);
  // source.onmessage = function(event){
  //   setLogs(event.data);
  // }
  // var xhr = new XMLHttpRequest();
  // xhr.open('GET', '{{ config["restApiBaseUrl"] + `api/v1/hello/streaming_call?code=${code}` }}', true);
  // xhr.send();
  // setInterval(function() {
  //   setLogs(xhr.responseText);
  // }, 500);
  
  const style = { backgroundColor: "#c3d7de" };
  return (
    <div className="App">
      <header className="App-header" style={style}>
        <div>{websocket_greeting}</div>
        <div>
          <button onClick={clickHandlerLoadImage}>
            load cifar_10 datasets
          </button>
          <br/>
          <button onClick={clickHandlerStartTraining}>
            start training
          </button>
        </div>
        <div>123: {logs}</div>

        {
          <BrowserRouter>
            <Routes>
              <Route path="/" element={<Layout />}>
                <Route index element={<Home />} />
                <Route path="about" element={<About />} />
                <Route path="*" element={<NoMatch />} />
              </Route>
            </Routes>
          </BrowserRouter>
        }
      </header>
    </div>
  );
}

export default App;
