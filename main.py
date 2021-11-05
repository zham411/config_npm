name: Node.js
Package
on:
release:
types: [created]
jobs:
build:
runs - on: ubuntu - latest
steps:
- uses: actions / checkout @ v2
# Setup .npmrc file to publish to npm
- uses: actions / setup - node @ v1
with:
    node - version: '12.x'
    registry - url: 'https://registry.npmjs.org'
- run: npm
install
- run: npm
publish
env:
NODE_AUTH_TOKEN: ${{secrets.NPM_TOKEN}}

// registry.npmjs.org /: _authToken =${NODE_AUTH_TOKEN}
registry = https: // registry.npmjs.org /
always - auth = true
