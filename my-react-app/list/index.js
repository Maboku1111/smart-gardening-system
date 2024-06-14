"use strict";

var _react = _interopRequireWildcard(require("react"));
var _client = _interopRequireDefault(require("react-dom/client"));
var _App = _interopRequireDefault(require("./components/App"));
require("bootstrap/dist/css/bootstrap.min.css");
var _jsxRuntime = require("react/jsx-runtime");
function _interopRequireDefault(e) { return e && e.__esModule ? e : { default: e }; }
function _getRequireWildcardCache(e) { if ("function" != typeof WeakMap) return null; var r = new WeakMap(), t = new WeakMap(); return (_getRequireWildcardCache = function (e) { return e ? t : r; })(e); }
function _interopRequireWildcard(e, r) { if (!r && e && e.__esModule) return e; if (null === e || "object" != typeof e && "function" != typeof e) return { default: e }; var t = _getRequireWildcardCache(r); if (t && t.has(e)) return t.get(e); var n = { __proto__: null }, a = Object.defineProperty && Object.getOwnPropertyDescriptor; for (var u in e) if ("default" !== u && {}.hasOwnProperty.call(e, u)) { var i = a ? Object.getOwnPropertyDescriptor(e, u) : null; i && (i.get || i.set) ? Object.defineProperty(n, u, i) : n[u] = e[u]; } return n.default = e, t && t.set(e, n), n; }
/* import React from "react"
import ReactDOM from "react-dom/client"
import App from "./components/App"


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>
)
*/

function AppWrapper() {
  (0, _react.useEffect)(() => {
    const root = _client.default.createRoot(document.getElementById('root'));
    root.render( /*#__PURE__*/(0, _jsxRuntime.jsx)(_react.default.StrictMode, {
      children: /*#__PURE__*/(0, _jsxRuntime.jsx)(_App.default, {})
    }));
  }, []);
  return null;
}
_client.default.render( /*#__PURE__*/(0, _jsxRuntime.jsx)(AppWrapper, {}), document.getElementById('root'));