import { createBrowserRouter } from "react-router-dom";
import App from "./App";
import Login from "./components/login";
import SignUp from "./components/signup";
import Profile from "./components/profile";
import PrivateRoute from "./AuthProvider/PrivateRoute";

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    children: [
      {
        path: "/login",
        element: <Login />,
      },
      {
        path: "/sign-up",
        element: <SignUp />,
      },
      {
        path: "/profile",
        element: (
          <PrivateRoute>
            <Profile />
          </PrivateRoute>
        ),
      },
    ],
  },
]);

export default router;