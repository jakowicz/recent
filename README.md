# recent

This tool will read your system account's ~/.zsh_history file and process it, displaying which commands you more frequently run for the program you specify.

## Prerequisities

- Python (2 or 3)

## Installation

First you need to install by brew tap, then install the package.

```
brew tap jakowicz/tap
brew install recent
```

## Usage

Run the recent.py command (I'm going to remove .py in the next release), pass one argument, which is the program you would like to show the recent history of. So for your recent popular "gpg" commands, you would run:

```
recent.py gpg
```

## License

MIT License

Copyright (c) 2018 jakowicz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
