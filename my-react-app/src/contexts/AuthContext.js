import React, { useContext, useState , useEffect } from 'react'
import { firebaseConfig } from "./FirebaseConfig"


const AuthContext = React.createContext()

export function useAuth() {
    return useContext(AuthContext)
}

export function AuthProvider({ children }) {
    const [currentUser, setCurrentUser] = useState()
    const [loading, setLoading] = useState(true)

    function signup(email, password) {
        return firebaseConfig.createUserWithEmailAndPassword(email, password)
    }

    function login(email, password) {
        return firebaseConfig.signInWithEmailAndPassword(email, password)
    }

    function logout() {
        return firebaseConfig.signOut()
    }

    function resetPassword(email) {
        return firebaseConfig.sendPasswordResetEmail(email)
    }

    useEffect(() => {
        const unsubscribe = firebaseConfig.onAuthStateChange(user => {
            setLoading(false)
            setCurrentUser(user)
        })

        return unsubscribe
    }, [])

    const value = {
        currentUser,
        login,
        signup,
        logout,
        resetPassword
    }


    return (
        <AuthContext.Provider value={value}>
            {!loading && children}
        </AuthContext.Provider>
    )
}