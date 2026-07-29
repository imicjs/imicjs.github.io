#!/bin/sh
set -eu

# Hugo's native Tailwind pipeline requires the executable to resolve directly
# to the Node entrypoint. pnpm's shell shim is not accepted by Hugo 0.162.
if [ -f node_modules/@tailwindcss/cli/dist/index.mjs ]; then
  rm -f node_modules/.bin/tailwindcss
  ln -s ../@tailwindcss/cli/dist/index.mjs node_modules/.bin/tailwindcss
fi
