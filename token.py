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
# Setup .npmrc file to publish to GitHub Packages
- uses: actions / setup - node @ v1
with:
    node - version: '12.x'
    registry - url: 'https://npm.pkg.github.com'
    # Defaults to the user or organization that owns the workflow file
    scope: '@octocat'
- run: npm
install
- run: npm
publish
env:
NODE_AUTH_TOKEN: ${{secrets.GITHUB_TOKEN}}

// npm.pkg.github.com /: _authToken =${NODE_AUTH_TOKEN}