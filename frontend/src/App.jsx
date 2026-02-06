import React from "react";
import ChatWindow from "./components/ChatWindow";
import FileUploader from "./components/FileUploader";

export default function App() {
  return (
    <div>
      <h1>Multi-Document RAG QA</h1>
      <FileUploader />
      <ChatWindow />
    </div>
  );
}
