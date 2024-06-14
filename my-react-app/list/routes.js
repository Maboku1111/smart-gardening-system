"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.default = void 0;
var _reactRouterDom = require("react-router-dom");
var _App = _interopRequireDefault(require("./App"));
var _login = _interopRequireDefault(require("./components/login"));
var _signup = _interopRequireDefault(require("./components/signup"));
var _profile = _interopRequireDefault(require("./components/profile"));
var _PrivateRoute = _interopRequireDefault(require("./AuthProvider/PrivateRoute"));
var _jsxRuntime = require("react/jsx-runtime");
function _interopRequireDefault(e) { return e && e.__esModule ? e : { default: e }; }
const router = (0, _reactRouterDom.createBrowserRouter)([{
  path: "/",
  element: /*#__PURE__*/(0, _jsxRuntime.jsx)(_App.default, {}),
  children: [{
    path: "/login",
    element: /*#__PURE__*/(0, _jsxRuntime.jsx)(_login.default, {})
  }, {
    path: "/sign-up",
    element: /*#__PURE__*/(0, _jsxRuntime.jsx)(_signup.default, {})
  }, {
    path: "/profile",
    element: /*#__PURE__*/(0, _jsxRuntime.jsx)(_PrivateRoute.default, {
      children: /*#__PURE__*/(0, _jsxRuntime.jsx)(_profile.default, {})
    })
  }]
}]);
var _default = exports.default = router;