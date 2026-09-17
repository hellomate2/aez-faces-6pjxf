# AEZ Faces

A Quizlet-style study app for learning the AEZ roster — 58 brothers across seven pledge classes.

**Live:** https://hellomate2.github.io/aez-faces-6pjxf/

## Modes
- **Flashcards** — photo → name, flip either direction, got/missed, arrow keys
- **Learn** — adaptive rounds that pull your weakest names first; multiple choice → find-the-photo → type it out as each face levels up
- **Match** — timed pair-up board (6/8/12 pairs), best time saved per pledge class
- **Test** — graded, configurable length and question types, review at the end
- **Roster** — searchable grid with mastery flags

Alpha Theta records carry hometown, high school, birthday, fun fact and IG; Learn and Test drill those alongside the faces. Phone numbers and LinkedIn URLs from the source deck are deliberately not included.

Progress is stored per browser in `localStorage`. Not indexed by search engines.

## Build
Page is generated from `template.html` + `roster.json`:

```bash
python3 build.py   # -> index.html
```
