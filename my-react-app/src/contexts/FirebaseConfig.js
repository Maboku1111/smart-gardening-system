import { initializeApp } from "firebase/app"
import { getAuth } from "firebase/auth"


export const firebaseConfig = {
    "apiKey": "AIzaSyBJi0XzIAxdsaH6bKWPhBE6ACqwRXIm0Sc",
    "authDomain": "smart-gardening-system-auth.firebaseapp.com",
    "projectId": "smart-gardening-system-auth",
    "storageBucket": "smart-gardening-system-auth.appspot.com",
    "messagingSenderId": "530898876849",
    "appId": "1:530898876849:web:b725967beaec299f2f2590",
    "measurementId": "G-PZNQJEDB8B"
}

const app = initializeApp(firebaseConfig)
const auth = getAuth(app)

export default auth;