module.exports = {
    presets: ['@babel/preset-env', '@babel/preset-react'],
    plugins: [
        ['@babel/plugin-transform-react-jsx', { runtime: 'automatic' }],
        '@babel/plugin-syntax-jsx'
      // other plugins...
    ],
};





