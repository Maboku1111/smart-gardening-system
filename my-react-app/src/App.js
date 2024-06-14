import React from 'react';
import Container from 'react-bootstrap/Container';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import AuthProvider from './components/AuthProvider';
import Dashboard from './components/Dashboard';
import SignUp from './components/signup';
import Login from './components/login';
import ForgotPassword from './components/ForgotPassword';

function App() {
    return React.createElement(
        Container,
        {
            className: "d-flex align-items-center justify-content-center",
            style: { minHeight: "100vh" }
        },
        React.createElement(
            "div",
            { className: "w-100", style: { maxWidth: '400px' } },
            React.createElement(
                Router,
                null,
                React.createElement(
                    AuthProvider,
                    null,
                    React.createElement(
                        Routes,
                        null,
                        React.createElement(Route, { exact: true, path: "/", element: React.createElement(Dashboard) }),
                        React.createElement(Route, { path: "/signup", element: React.createElement(SignUp) }),
                        React.createElement(Route, { path: "/login", element: React.createElement(Login) }),
                        React.createElement(Route, { path: "/forgot-password", element: React.createElement(ForgotPassword) })
                    )
                )
            )
        )
    );
}

export default App;
