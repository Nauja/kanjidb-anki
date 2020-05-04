# KanjiDB-Anki

[![PyPI version](https://badge.fury.io/py/kanjidb-anki.svg)](https://badge.fury.io/py/kanjidb-anki)
[![Build Status](https://travis-ci.org/Nauja/kanjidb-anki.png?branch=master)](https://travis-ci.org/Nauja/kanjidb-anki)
[![Test Coverage](https://codeclimate.com/github/Nauja/kanjidb-anki/badges/coverage.svg)](https://codeclimate.com/github/Nauja/kanjidb-anki/coverage)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Nauja/kanjidb-anki/issues)

Collection of Anki plugins for [KanjiDB](https://github.com/Nauja/kanjidb).

# Install

Using pip:

```bash
> pip install kanjidb-anki
```

# Generate Anki decks

Create the following `config.yml` file:

```yaml
run:
- kanjistream:
    encoding: utf8
    separator: ";"
    in:
    - kanjis.txt
    out: kanjis
- kanjidic2:
    kd2_file: kanjidic2.xml
    in: kanjis
    out: db
- ankideck:
    in: db
    generate: kanjis
    out: ankideck.apkg
    deck_id: 1
    title: Generated Deck
```

Steps are:
  * `kanjistream`: read kanjis separated by `;` character from `kanjis.txt` file.
  * `kanjidic2`: create a JSON dict with kanjis data from Kanjidic2 XML file.
  * `ankideck`: generate an Anki deck.

Create a file called `kanjis.txt` that will contain kanjis to include in deck:

```
一;二;三
```

Now run following command:

```bash
> python -m kanjidb config.yml
```

This will generate an Anki deck containing all kanjis listed in `kanjis.txt`.
