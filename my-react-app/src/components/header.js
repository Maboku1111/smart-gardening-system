import { useContext } from "react";
import { Link, NavLink, useNavigate } from "react-router-dom";
import { AuthContext } from "./AuthProvider";

const Header = () => {
  // Access the user, logOut, and loading state from the AuthContext
  const { user, logOut, loading } = useContext(AuthContext);

  // Use the useNavigate hook to programmatically navigate between pages
  const navigate = useNavigate();

  // Handle user logout
  const handleSignOut = () => {
    logOut()
      .then(() => {
        console.log("User logged out successfully");
        navigate("/login"); // Redirect to the login page after logout
      })
      .catch((error) => console.error(error));
  };

  // Define navigation links based on user authentication status
  const navLinks = (
    <>
      <li>
        <NavLink to="/">Home</NavLink>
      </li>
      {!user && (
        <>
          <li>
            <NavLink to="/login">Login</NavLink>
          </li>
          <li>
            <NavLink to="/sign-up">Sign-Up</NavLink>
          </li>
        </>
      )}
    </>
  );

  // Render loading indicator if authentication state is still loading
  return loading ? (
    <span className="loading loading-dots loading-lg flex item-center mx-auto"></span>
  ) : (
    <div>
      {/* Render the navigation bar */}
      <div className="navbar bg-base-100">
        <div className="navbar-start">
          {/* Dropdown menu for mobile devices */}
          <div className="dropdown">
            <label tabIndex={0} className="btn btn-ghost lg:hidden">
              {/* Hamburger icon */}
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="h-5 w-5"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2"
                  d="M4 6h16M4 12h8m-8 6h16"
                />
              </svg>
            </label>
            {/* Dropdown content with navigation links */}
            <ul
              tabIndex={0}
              className="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52"
            >
              {navLinks}
            </ul>
          </div>
          {/* Application title */}
          <a className="btn btn-ghost normal-case text-xl">Firebase Auth</a>
        </div>
        <div className="navbar-center hidden lg:flex">
          {/* Horizontal navigation menu for larger screens */}
          <ul className="menu menu-horizontal px-1">{navLinks}</ul>
        </div>
        <div className="navbar-end">
          {/* Display user information and logout button if authenticated */}
          {user && <a className="btn">{user.displayName}</a>}
          {user && (
            <div className="dropdown dropdown-end">
              <label tabIndex={0} className="btn btn-ghost btn-circle avatar">
                {/* User profile picture */}
                <div className="w-10 rounded-full">
                  <img src="/images/stock/photo-1534528741775-53994a69daeb.jpg" />
                </div>
              </label>
              {/* Dropdown content for user profile */}
              <ul
                tabIndex={0}
                className="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52"
              >
                <li>
                  <Link to="/profile">
                    {/* Profile link */}
                    <span className="justify-between">Profile</span>
                  </Link>
                </li>
                <li>
                  <a onClick={handleSignOut}>Logout</a>
                  {/* Logout button */}
                </li>
              </ul>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default Header;
