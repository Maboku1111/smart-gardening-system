/* import React from "react"
import ReactDOM from "react-dom/client"
import App from "./components/App"


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>
)
*/
import React, { useEffect } from 'react';
import ReactDOM from 'react-dom/client';
import App from './components/App';
import 'bootstrap/dist/css/bootstrap.min.css';

function AppWrapper() {
  useEffect(() => {
    const root = ReactDOM.createRoot(document.getElementById('root'));
    root.render(
      <React.StrictMode>
        <App />
      </React.StrictMode>
    );
  }, []);

  return null;
}

ReactDOM.render(<AppWrapper />, document.getElementById('root'));
