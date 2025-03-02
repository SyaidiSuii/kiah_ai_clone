import { useState } from "react";
import axios from "axios";

function App() {
  const [text, setText] = useState("");
  const [error, setError] = useState("");

  const handleUpload = async (event) => {
    const file = event.target.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append("image", file);

    try {
      const response = await axios.post(
        "https://kiah-ai-clone.onrender.com/upload", // Ganti dengan backend URL jika online
        formData,
        { headers: { "Content-Type": "multipart/form-data" } }
      );
      setText(response.data.extracted_text);
      setError(""); // Reset error jika berhasil
    } catch (error) {
      console.error("Error uploading file", error);
      setError("Failed to extract text. Please try again.");
    }
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gray-100">
      <h1 className="text-3xl font-bold text-blue-600">Upload an Image</h1>
      <input
        type="file"
        onChange={handleUpload}
        className="mt-4 p-2 border border-gray-300 rounded"
        accept="image/*"
      />
      {text && <p className="mt-4 text-lg text-gray-700">{text}</p>}
      {error && <p className="mt-4 text-lg text-red-600">{error}</p>}
    </div>
  );
}

export default App;
