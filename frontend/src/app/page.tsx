"use client";

/* eslint-disable @typescript-eslint/no-explicit-any */
import { useState, useEffect } from "react";

export default function Home() {
  const [isRecording, setIsRecording] = useState(false);
  const [recognizedText, setRecognizedText] = useState("");

  const startRecording = async () => {
    try {
      const response = await fetch("http://localhost:5000/start", {
        method: "POST",
      });
      const data = await response.json();
      console.log(data.status);
      setIsRecording(true);
    } catch (error) {
      console.error("Error starting recording:", error);
    }
  };

  const stopRecording = async () => {
    try {
      const response = await fetch("http://localhost:5000/stop", {
        method: "POST",
      });
      const data = await response.json();
      console.log(data.status);
      setIsRecording(false);
    } catch (error) {
      console.error("Error stopping recording:", error);
    }
  };

  const fetchText = async () => {
    try {
      const response = await fetch("http://localhost:5000/text");
      const data = await response.json();
      setRecognizedText(data.text);
    } catch (error) {
      console.error("Error fetching text:", error);
    }
  };

  useEffect(() => {
    let interval: any;
    if (isRecording) {
      interval = setInterval(fetchText, 1000); // Fetch text every second while recording
    }
    return () => clearInterval(interval);
  }, [isRecording]);

  const toggleRecording = () => {
    if (isRecording) {
      stopRecording();
    } else {
      startRecording();
    }
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Real-time Speech Recognition</h1>
      <div className="mb-4">
        <button
          className={`px-4 py-2 rounded ${
            isRecording ? "bg-red-500" : "bg-green-500"
          } text-white`}
          onClick={toggleRecording}
        >
          {isRecording ? "Stop Recording" : "Start Recording"}
        </button>
      </div>
      <div className="border p-4 h-64 overflow-auto">
        <h2 className="text-xl font-semibold mb-2">Recognized Text:</h2>
        <p>{recognizedText}</p>
      </div>
    </div>
  );
}
