### Start the app

- bundle exec jekyll serve

Navigate to http://localhost:4000

A development server will run at http://localhost:4000/

Note: auto-regeneration is enabled by default. Use `--no-watch` to disable.

# LiveReload

- jekyll serve --livereload

LiveReload refreshes your browser after a change.

### Basic usage

- jekyll build

The current folder will be generated into ./_site

- jekyll build --destination <destination>

The current folder will be generated into <destination>

jekyll build --watch
# => The current folder will be generated into ./_site,
#    watched for changes, and regenerated automatically.
