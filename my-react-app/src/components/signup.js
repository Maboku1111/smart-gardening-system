import { useContext, useState } from "react";
import { AuthContext } from "./AuthProvider";
import { updateProfile } from "firebase/auth";
import { useNavigate } from "react-router-dom";

const SignUp = () => {
  const { createUser, user, loading } = useContext(AuthContext);
  const [selectedImage, setSelectedImage] = useState(null);
  const navigate = useNavigate();

  // If authentication is still loading, display a loading indicator
  if (loading) {
    return (
      <span className="loading loading-dots loading-lg flex item-center mx-auto"></span>
    );
  }

  // If the user is already authenticated, redirect to the home page
  if (user) {
    navigate("/");
  }

  // Handle form submission for user registration
  const handleFormSubmit = (e) => {
    e.preventDefault();
    const name = e.target.name.value;
    const email = e.target.email.value;
    const password = e.target.password.value;
    createUser(email, password)
      .then((result) => {
        // Update user profile with display name
        updateProfile(result.user, {
          displayName: name,
        });
        navigate("/");
        console.log(result);
      })
      .catch((error) => {
        console.log(error);
      });
    e.target.reset();
  };

  // Handle image upload (not shown in the code, but you can add it)

  // Render the sign-up form
  return (
    <div>
      <div className="min-h-screen bg-base-200">
        <div className="hero-content flex-col">
          <div className="card flex-shrink-0 w-full max-w-sm shadow-2xl bg-base-100">
            <div className="card-body">
              <form onSubmit={handleFormSubmit}>
                <div className="form-control">
                  <label className="label">
                    <span className="label-text">Name</span>
                  </label>
                  <input
                    type="text"
                    name="name"
                    placeholder="Name"
                    className="input input-bordered"
                  />
                </div>
                <div className="form-control">
                  <label className="label">
                    <span className="label-text">Email</span>
                  </label>
                  <input
                    type="email"
                    name="email"
                    placeholder="Email"
                    className="input input-bordered"
                  />
                </div>
                <div className="form-control">
                  <label className="label">
                    <span className="label-text">Password</span>
                  </label>
                  <input
                    type="password"
                    name="password"
                    placeholder="Password"
                    className="input input-bordered"
                  />
                </div>
                <div className="form-control mt-6">
                  <button className="btn btn-primary">Sign Up</button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default SignUp;