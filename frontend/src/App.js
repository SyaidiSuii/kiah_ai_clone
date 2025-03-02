import { useState } from "react";
import axios from "axios";

function App() {
  const [text, setText] = useState("");

  const handleUpload = async (event) => {
    const file = event.target.files[0];
    const formData = new FormData();
    formData.append("image", file);

    try {
      const response = await axios.post(
        "https://kiah-ai-backend.onrender.com/upload",
        formData
      );
      setText(response.data.extracted_text);
    } catch (error) {
      console.error("Error uploading file", error);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gray-100">
      <h1 className="text-3xl font-bold text-blue-600">Upload an Image</h1>
      <input
        type="file"
        onChange={handleUpload}
        className="mt-4 p-2 border border-gray-300 rounded"
      />
      <p className="mt-4 text-lg">{text}</p>
    </div>
  );
}

export default App;
