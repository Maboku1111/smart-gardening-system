"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.default = Login;
var _react = _interopRequireWildcard(require("react"));
var _reactBootstrap = require("react-bootstrap");
var _AuthContext = require("../contexts/AuthContext");
var _reactRouterDom = require("react-router-dom");
var _signup = _interopRequireDefault(require("./signup"));
var _jsxRuntime = require("react/jsx-runtime");
function _interopRequireDefault(e) { return e && e.__esModule ? e : { default: e }; }
function _getRequireWildcardCache(e) { if ("function" != typeof WeakMap) return null; var r = new WeakMap(), t = new WeakMap(); return (_getRequireWildcardCache = function (e) { return e ? t : r; })(e); }
function _interopRequireWildcard(e, r) { if (!r && e && e.__esModule) return e; if (null === e || "object" != typeof e && "function" != typeof e) return { default: e }; var t = _getRequireWildcardCache(r); if (t && t.has(e)) return t.get(e); var n = { __proto__: null }, a = Object.defineProperty && Object.getOwnPropertyDescriptor; for (var u in e) if ("default" !== u && {}.hasOwnProperty.call(e, u)) { var i = a ? Object.getOwnPropertyDescriptor(e, u) : null; i && (i.get || i.set) ? Object.defineProperty(n, u, i) : n[u] = e[u]; } return n.default = e, t && t.set(e, n), n; }
function Login() {
  const emailRef = (0, _react.useRef)();
  const passwordRef = (0, _react.useRef)();
  const {
    login
  } = (0, _AuthContext.useAuth)();
  const {
    currentUser
  } = (0, _react.useState)();
  const [error, setError] = (0, _react.useState)('');
  const [loading, setLoading] = (0, _react.useState)(false);
  const history = (0, _reactRouterDom.useNavigate)();
  async function handleSubmit(e) {
    e.preventDefault();
    try {
      setError('');
      setLoading('true');
      await login(emailRef.current.value, passwordRef.current.value);
      history.push("/");
    } catch {
      setError('Failed to sign in');
    }
    setLoading('false');
    (0, _signup.default)(emailRef.current.value, passwordRef.current.value);
  }
  return /*#__PURE__*/(0, _jsxRuntime.jsxs)(_jsxRuntime.Fragment, {
    children: [/*#__PURE__*/(0, _jsxRuntime.jsx)(_reactBootstrap.Card, {
      children: /*#__PURE__*/(0, _jsxRuntime.jsxs)(_reactBootstrap.Card.Body, {
        children: [/*#__PURE__*/(0, _jsxRuntime.jsx)("h2", {
          className: "text-center mb-4",
          children: "Log In"
        }), currentUser.email, error && /*#__PURE__*/(0, _jsxRuntime.jsx)(_reactBootstrap.Alert, {
          variant: "danger",
          children: error
        }), /*#__PURE__*/(0, _jsxRuntime.jsxs)(_reactBootstrap.Form, {
          onSubmit: handleSubmit,
          children: [/*#__PURE__*/(0, _jsxRuntime.jsxs)(_reactBootstrap.Form.Group, {
            id: "email",
            children: [/*#__PURE__*/(0, _jsxRuntime.jsx)(_reactBootstrap.Form.Label, {
              children: "Email"
            }), /*#__PURE__*/(0, _jsxRuntime.jsx)(_reactBootstrap.Form.Control, {
              type: "email",
              ref: emailRef,
              required: true
            })]
          }), /*#__PURE__*/(0, _jsxRuntime.jsxs)(_reactBootstrap.Form.Group, {
            id: "password",
            children: [/*#__PURE__*/(0, _jsxRuntime.jsx)(_reactBootstrap.Form.Label, {
              children: "Password"
            }), /*#__PURE__*/(0, _jsxRuntime.jsx)(_reactBootstrap.Form.Control, {
              type: "password",
              ref: passwordRef,
              required: true
            })]
          }), /*#__PURE__*/(0, _jsxRuntime.jsx)(_reactBootstrap.Button, {
            disabled: loading,
            className: "w-100",
            type: "Submit",
            children: "Log In"
          })]
        }), /*#__PURE__*/(0, _jsxRuntime.jsx)("div", {
          className: "w-100 text-center mt-3",
          children: /*#__PURE__*/(0, _jsxRuntime.jsx)(_reactRouterDom.Link, {
            to: "/forgot-password",
            children: "Forgot Password?"
          })
        })]
      })
    }), /*#__PURE__*/(0, _jsxRuntime.jsxs)("div", {
      className: "w-100 text-center mt-2",
      children: ["Need an accout? ", /*#__PURE__*/(0, _jsxRuntime.jsx)(_reactRouterDom.Link, {
        to: "/signup",
        children: "Sign Up"
      })]
    })]
  });
}