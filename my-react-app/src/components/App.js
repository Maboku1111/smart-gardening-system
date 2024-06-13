import React from "react"
import SignUp from "./signup";
import { Container } from "react-bootstrap";
import { AuthProvider } from "../contexts/AuthContext";
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Dashboard from "./Dashboard"
import Login from "./login"
import ForgotPassword from './ForgotPassword'

function App() {
    return (
        <Container 
            className="d-flex align-items-center justify-content-center"
            style={{ minHeight: "100vh"}}
        >
            <div className="w-100" style={{ maxWidth: '400px' }}>
                <Router>
                    <AuthProvider>
                        <Routes>
                            <Route exact path="/" component={Dashboard}/>
                            <Route path="/signup" component={SignUp} />
                            <Route path="/login" component={Login} />
                            <Route path="/forgot-password" component={ForgotPassword} />
                        </Routes>
                    </AuthProvider>
                </Router> 
            </div>   
        </Container>
    )
}

export default App;