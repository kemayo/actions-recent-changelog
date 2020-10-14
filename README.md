# actions-recent-changelog
A GitHub Action for generating a "recent changes" file from a larger manually-curated changelog

## Behavior
The action expects to be provided with a markdown file. It will extract the first `##` subheading and all lines between it and the next `##` subheading or the end of the file. These lines will be written as-is to the provided output file.

Coincidentally, this will work with the [keepachangelog](https://keepachangelog.com/en/1.0.0/) format. It doesn't require that your changelog be compliant with the full specification, however.

## Usage
```YAML
    - uses: kemayo/actions-recent-changelog@v1
      with:
        input: CHANGELOG.md
        output: RECENT_CHANGES.md
```
