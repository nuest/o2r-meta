[![Build Status](https://travis-ci.org/o2r-project/o2r-meta.svg?branch=master)](https://travis-ci.org/o2r-project/o2r-meta)

# o2r meta

This is a collection of mircro services for the o2r-platform.


## metaextract

metaextract.py is a very basic try to automate metadata extraction from Rmd and R scripts.

Required packages: ```PyYAML```, ```dicttoxml```, ```guess_language-spirit```

Usage:

    python metaextract.py -i INPUT_DIR -o OUTPUT_DIR -m MODUS [-s]


+ use ```xml``` or ```json``` as ```MODUS```.
+ use optional ```-s``` to output to screen.

Example:

    python metaextract.py -i"tests" -o"tests" -m"json" [-s]


+ use ```docker build``` command with the ```extract``` directory of this repository as the build context to build the Docker image.

Example:

    docker build -t o2r-meta extract
    docker run --rm -v $(pwd)/extract/tests:/meta o2r-meta -i /meta -o /meta/extracts -m json
    docker run --rm -v $(pwd)/extract/tests:/meta o2r-meta -i /meta -o /meta/extracts -m xml
    docker run --rm -v $(pwd)/extract/tests:/meta o2r-meta -i /meta -o /meta/extracts -m json -s

---


## metabroker

metabroker.py is a translator for raw metadata from the o2r project and common metadata schemas such as DataCite etc.
Translation instructions are read from ```crosswalk.csv```.


Required package: ```dicttoxml```

Usage:

    python metabroker.py -i INPUT_DIR -o OUTPUT_DIR

+ the script parses all json files in the input directory that begin with "meta_" (possible outputs of metaextract.py)

Example:

    python metabroker.py -i"tests" -o"tests"

---

## schema

+ o2r metadata schema with example and documentation. Currently an adaption of the codemeta json schema for software metadata.

---

## metavalidate

metavalidate.py is a simple validator for json schemas

Required package: ```json-spec```

Usage:

    python metavalidate.py -s SCHEMA_PATH -c CANDIDATE_PATH

+ use relative paths.

Example:

    python metavalidate.py -s"../schema/json/o2r-meta-schema.json" -c"../schema/json/example1-valid.json"

---

## License

o2r-meta is licensed under Apache License, Version 2.0, see file LICENSE.

Copyright (C) 2016 - o2r project.