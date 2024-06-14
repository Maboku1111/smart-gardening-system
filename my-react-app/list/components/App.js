"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.default = void 0;
var _react = _interopRequireDefault(require("react"));
var _Container = _interopRequireDefault(require("react-bootstrap/Container"));
var _reactRouterDom = require("react-router-dom");
var _AuthProvider = _interopRequireDefault(require("./AuthProvider"));
var _Dashboard = _interopRequireDefault(require("./Dashboard"));
var _signup = _interopRequireDefault(require("./signup"));
var _login = _interopRequireDefault(require("./login"));
var _ForgotPassword = _interopRequireDefault(require("./ForgotPassword"));
function _interopRequireDefault(e) { return e && e.__esModule ? e : { default: e }; }
function App() {
  return /*#__PURE__*/_react.default.createElement(_Container.default, {
    className: "d-flex align-items-center justify-content-center",
    style: {
      minHeight: "100vh"
    }
  }, /*#__PURE__*/_react.default.createElement("div", {
    className: "w-100",
    style: {
      maxWidth: '400px'
    }
  }, /*#__PURE__*/_react.default.createElement(_reactRouterDom.BrowserRouter, null, /*#__PURE__*/_react.default.createElement(_AuthProvider.default, null, /*#__PURE__*/_react.default.createElement(_reactRouterDom.Routes, null, /*#__PURE__*/_react.default.createElement(_reactRouterDom.Route, {
    exact: true,
    path: "/",
    element: /*#__PURE__*/_react.default.createElement(_Dashboard.default)
  }), /*#__PURE__*/_react.default.createElement(_reactRouterDom.Route, {
    path: "/signup",
    element: /*#__PURE__*/_react.default.createElement(_signup.default)
  }), /*#__PURE__*/_react.default.createElement(_reactRouterDom.Route, {
    path: "/login",
    element: /*#__PURE__*/_react.default.createElement(_login.default)
  }), /*#__PURE__*/_react.default.createElement(_reactRouterDom.Route, {
    path: "/forgot-password",
    element: /*#__PURE__*/_react.default.createElement(_ForgotPassword.default)
  }))))));
}
var _default = exports.default = App;