export const presets = ['@babel/preset-env', '@babel/preset-react'];
export const plugins = [
    '@babel/plugin-proposal-private-property-in-object',
    ['@babel/plugin-transform-react-jsx', { runtime: 'automatic' }]
    // other plugins...
];
  
