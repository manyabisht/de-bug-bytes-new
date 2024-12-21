// src/index.js

import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';  // Optional: If you have global styles
import App from './app';  // Import your main App component

// Render the App component into the root div in your public/index.html
ReactDOM.render(
  <React.StrictMode>
    <App />  {/* Render your App component here */}
  </React.StrictMode>,
  document.getElementById('root')  // This matches the id in the index.html file
);
