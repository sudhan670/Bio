# Bio Generator

A web application that generates personalized bios based on user inputs such as career, personality traits, interests, and relationship goals. This project integrates a front-end interface and a back-end server powered by the Gemini API for bio generation.

---

## Features

- **User-Friendly Form**: Collects user input for generating custom bios.
- **Gemini API Integration**: Leverages the Gemini API to generate meaningful bios.
- **Real-Time Output**: Displays the generated bio instantly on the front-end.
- **Responsive Design**: Optimized for desktop and mobile use.

---

## Tech Stack

- **Front-End**: HTML, CSS, JavaScript (Bootstrap for styling)
- **Back-End**: Node.js, Express.js
- **API**: Gemini API
- **Dependencies**:
  - `flask` - Web server
  - `cors` - Cross-Origin Resource Sharing
  - `dotenv` - Environment variable management
  - `axios` - HTTP requests to Gemini API

---

## Installation

### Prerequisites

- Python installed
- A valid Gemini API Key

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/bio-generator.git
   cd bio-generator
   ```

2. **Install Dependencies**:
   ```bash
   cd back
   pip install dotenv cors
   ```

3. **Set Up Environment Variables**:
   Create a `.env` file in the `back` directory and add:
   ```env
   GEMINI_API_KEY=your-gemini-api-key
   ```

4. **Start the Server**:
   ```bash
   python main.py
   ```
   The server will run on `http://localhost:3000`.

5. **Open the Front-End**:
   - Open the `index.html` file in your browser.
   - Alternatively, serve it using a local server like [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer).

---

## Project Structure

```plaintext
bio-generator/
├── back/                     # Back-end folder
│   ├── main.py           # Express server file
│   ├── .gitignore       # Node.js dependencies
│   ├── requirements.txt  # Dependency lock file
│   └── .env                  # Environment variables
├── front/                    # Front-end folder
│   ├── index.html            # Main HTML file
│   ├── css/                  # CSS folder
│   │   └── style.css         # Styling for the web page
│   ├── js/                   # JavaScript folder
│   │   └── script.js         # Front-end logic
└── README.md                 # Project documentation
```

---

## Usage

1. Fill out the form with your **Career**, **Personality**, **Interests**, and **Relationship Goals**.
2. Click the **Generate Bio** button.
3. View your personalized bio displayed below the form.

---

## API Details

- **Endpoint**: `POST /generate-bio`
- **Request Body**:
  ```json
  {
    "career": "Software Developer",
    "personality": "Creative and detail-oriented",
    "interests": "Technology, Music",
    "relationshipGoals": "Building meaningful connections"
  }
  ```
- **Response**:
  ```json
  {
    "bio": "I am a Software Developer who is creative and detail-oriented. I love technology and music, and my goal is to build meaningful connections."
  }
  ```

---

## Troubleshooting

- **Failed to connect to the server**: Ensure the back-end server is running and the API URL in `script.js` is correct.
- **Environment variable not found**: Check if `.env` is properly configured and restart the server.
- **Gemini API error**: Verify your API key and ensure it has valid permissions.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Contributions

Contributions, issues, and feature requests are welcome! Feel free to fork the repository and submit pull requests.

---
