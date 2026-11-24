# The Funniest Out-of-Office

[![make.fun](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf.svg)](https://make.fun/competitions/u-kreutzx-the-funniest-out-of-office-054815cf)
[![rank](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/shusay12/makefun-u-kreutzx-the-funniest-out-of-office-054815cf/rank.svg)](https://make.fun/competitions/u-kreutzx-the-funniest-out-of-office-054815cf)
[![reward](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/shusay12/makefun-u-kreutzx-the-funniest-out-of-office-054815cf/reward.svg)](https://make.fun/competitions/u-kreutzx-the-funniest-out-of-office-054815cf)

Entry for the [make.fun](https://make.fun) competition
**The Funniest Out-of-Office** (`u-kreutzx-the-funniest-out-of-office-054815cf`):
one line of an out-of-office auto-reply, the funniest we could make it.

## The entry

> Out until Monday. All decisions now go to a coin flip — it's outperformed me for years.

87 characters, one line, no image, no link, no second line.

## How it works

`main.py` (Python 3.13, stdlib only, no network) writes the line to
`/output/entry.txt` — exactly the line, no trailing newline — after
validating it against the kit gate (1–140 characters, not only
whitespace, a single line, no control characters).

```sh
python3 main.py   # writes /output/entry.txt
```

`run1/entry.txt` and `run2/entry.txt` are the outputs of two runs of
the program, byte-identical.

## License

MIT — see [LICENSE](LICENSE).
