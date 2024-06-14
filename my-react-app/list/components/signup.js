"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.default = SignUp;
var _react = _interopRequireWildcard(require("react"));
var _reactBootstrap = require("react-bootstrap");
var _AuthContext = require("../contexts/AuthContext");
var _reactRouterDom = require("react-router-dom");
var _jsxRuntime = require("react/jsx-runtime");
function _getRequireWildcardCache(e) { if ("function" != typeof WeakMap) return null; var r = new WeakMap(), t = new WeakMap(); return (_getRequireWildcardCache = function (e) { return e ? t : r; })(e); }
function _interopRequireWildcard(e, r) { if (!r && e && e.__esModule) return e; if (null === e || "object" != typeof e && "function" != typeof e) return { default: e }; var t = _getRequireWildcardCache(r); if (t && t.has(e)) return t.get(e); var n = { __proto__: null }, a = Object.defineProperty && Object.getOwnPropertyDescriptor; for (var u in e) if ("default" !== u && {}.hasOwnProperty.call(e, u)) { var i = a ? Object.getOwnPropertyDescriptor(e, u) : null; i && (i.get || i.set) ? Object.defineProperty(n, u, i) : n[u] = e[u]; } return n.default = e, t && t.set(e, n), n; }
function SignUp() {
  const emailRef = (0, _react.useRef)();
  const passwordRef = (0, _react.useRef)();
  const passwordConfirmRef = (0, _react.useRef)();
  const {
    signup
  } = (0, _AuthContext.useAuth)();
  const {
    currentUser
  } = (0, _react.useState)();
  const [error, setError] = (0, _react.useState)('');
  const [loading, setLoading] = (0, _react.useState)(false);
  const history = (0, _reactRouterDom.Navigate)();
  async function handleSubmit(e) {
    e.preventDefault();
    if (passwordRef.current.value === passwordConfirmRef.current.value) {
      return setError('Passwords do not match');
    }
    try {
      setError('');
      setLoading('true');
      await signup(emailRef.current.value, passwordRef.current.value);
      history.push("/");
    } catch {
      setError('Failed to create an account');
    }
    setLoading('false');
    signup(emailRef.current.value, passwordRef.current.value);
  }
  return /*#__PURE__*/(0, _jsxRuntime.jsxs)(_jsxRuntime.Fragment, {
    children: [/*#__PURE__*/(0, _jsxRuntime.jsx)(_reactBootstrap.Card, {
      children: /*#__PURE__*/(0, _jsxRuntime.jsxs)(_reactBootstrap.Card.Body, {
        children: [/*#__PURE__*/(0, _jsxRuntime.jsx)("h2", {
          className: "text-center mb-4",
          children: "Sign Up"
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
          }), /*#__PURE__*/(0, _jsxRuntime.jsxs)(_reactBootstrap.Form.Group, {
            id: "password-confirm",
            children: [/*#__PURE__*/(0, _jsxRuntime.jsx)(_reactBootstrap.Form.Label, {
              children: "Password Confirmation"
            }), /*#__PURE__*/(0, _jsxRuntime.jsx)(_reactBootstrap.Form.Control, {
              type: "password",
              ref: passwordConfirmRef,
              required: true
            })]
          }), /*#__PURE__*/(0, _jsxRuntime.jsx)(_reactBootstrap.Button, {
            disabled: loading,
            className: "w-100",
            type: "Submit",
            children: "Sign Up"
          })]
        })]
      })
    }), /*#__PURE__*/(0, _jsxRuntime.jsxs)("div", {
      className: "w-100 text-center mt-2",
      children: ["Already have an account? ", /*#__PURE__*/(0, _jsxRuntime.jsx)(_reactRouterDom.Link, {
        to: "/login",
        children: "Log In"
      })]
    })]
  });
}