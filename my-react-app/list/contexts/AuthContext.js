"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.AuthProvider = AuthProvider;
exports.useAuth = useAuth;
var _react = _interopRequireWildcard(require("react"));
var _FirebaseConfig = require("./FirebaseConfig");
var _jsxRuntime = require("react/jsx-runtime");
function _getRequireWildcardCache(e) { if ("function" != typeof WeakMap) return null; var r = new WeakMap(), t = new WeakMap(); return (_getRequireWildcardCache = function (e) { return e ? t : r; })(e); }
function _interopRequireWildcard(e, r) { if (!r && e && e.__esModule) return e; if (null === e || "object" != typeof e && "function" != typeof e) return { default: e }; var t = _getRequireWildcardCache(r); if (t && t.has(e)) return t.get(e); var n = { __proto__: null }, a = Object.defineProperty && Object.getOwnPropertyDescriptor; for (var u in e) if ("default" !== u && {}.hasOwnProperty.call(e, u)) { var i = a ? Object.getOwnPropertyDescriptor(e, u) : null; i && (i.get || i.set) ? Object.defineProperty(n, u, i) : n[u] = e[u]; } return n.default = e, t && t.set(e, n), n; }
const AuthContext = /*#__PURE__*/_react.default.createContext();
function useAuth() {
  return (0, _react.useContext)(AuthContext);
}
function AuthProvider(_ref) {
  let {
    children
  } = _ref;
  const [currentUser, setCurrentUser] = (0, _react.useState)();
  const [loading, setLoading] = (0, _react.useState)(true);
  function signup(email, password) {
    return _FirebaseConfig.firebaseConfig.createUserWithEmailAndPassword(email, password);
  }
  function login(email, password) {
    return _FirebaseConfig.firebaseConfig.signInWithEmailAndPassword(email, password);
  }
  function logout() {
    return _FirebaseConfig.firebaseConfig.signOut();
  }
  function resetPassword(email) {
    return _FirebaseConfig.firebaseConfig.sendPasswordResetEmail(email);
  }
  (0, _react.useEffect)(() => {
    const unsubscribe = _FirebaseConfig.firebaseConfig.onAuthStateChange(user => {
      setLoading(false);
      setCurrentUser(user);
    });
    return unsubscribe;
  }, []);
  const value = {
    currentUser,
    login,
    signup,
    logout,
    resetPassword
  };
  return /*#__PURE__*/(0, _jsxRuntime.jsx)(AuthContext.Provider, {
    value: value,
    children: !loading && children
  });
}