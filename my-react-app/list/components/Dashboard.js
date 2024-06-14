"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.default = Dashboard;
var _react = _interopRequireWildcard(require("react"));
var _reactBootstrap = require("react-bootstrap");
var _AuthContext = require("../contexts/AuthContext");
var _reactRouterDom = require("react-router-dom");
var _jsxRuntime = require("react/jsx-runtime");
function _getRequireWildcardCache(e) { if ("function" != typeof WeakMap) return null; var r = new WeakMap(), t = new WeakMap(); return (_getRequireWildcardCache = function (e) { return e ? t : r; })(e); }
function _interopRequireWildcard(e, r) { if (!r && e && e.__esModule) return e; if (null === e || "object" != typeof e && "function" != typeof e) return { default: e }; var t = _getRequireWildcardCache(r); if (t && t.has(e)) return t.get(e); var n = { __proto__: null }, a = Object.defineProperty && Object.getOwnPropertyDescriptor; for (var u in e) if ("default" !== u && {}.hasOwnProperty.call(e, u)) { var i = a ? Object.getOwnPropertyDescriptor(e, u) : null; i && (i.get || i.set) ? Object.defineProperty(n, u, i) : n[u] = e[u]; } return n.default = e, t && t.set(e, n), n; }
function Dashboard() {
  const [error, setError] = (0, _react.useState)("");
  const {
    currentUser,
    logout
  } = (0, _AuthContext.useAuth)();
  const history = (0, _reactRouterDom.useNavigate)();
  async function handleLogout() {
    setError('');
    try {
      await logout();
      history.push('/login');
    } catch {
      setError('Failed to log out');
    }
  }
  return /*#__PURE__*/(0, _jsxRuntime.jsxs)(_jsxRuntime.Fragment, {
    children: [/*#__PURE__*/(0, _jsxRuntime.jsx)(_reactBootstrap.Card, {
      children: /*#__PURE__*/(0, _jsxRuntime.jsxs)(_reactBootstrap.Card.Body, {
        children: [/*#__PURE__*/(0, _jsxRuntime.jsx)("h2", {
          className: "text-center mb-4",
          children: "Profile"
        }), error && /*#__PURE__*/(0, _jsxRuntime.jsx)(_reactBootstrap.Alert, {
          variant: "danger",
          children: error
        }), /*#__PURE__*/(0, _jsxRuntime.jsx)("strong", {
          children: "Email:"
        }), " ", currentUser.email, /*#__PURE__*/(0, _jsxRuntime.jsx)(_reactRouterDom.Link, {
          to: "/update-profile",
          className: "btn btn-primary w-100 nt-3",
          children: "Update Profile"
        })]
      })
    }), /*#__PURE__*/(0, _jsxRuntime.jsx)("div", {
      className: "w-100 text-center nt-2",
      children: /*#__PURE__*/(0, _jsxRuntime.jsx)(_reactBootstrap.Button, {
        variant: "link",
        onClick: handleLogout,
        children: "Log Out"
      })
    })]
  });
}