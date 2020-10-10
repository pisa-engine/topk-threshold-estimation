## Build PISA

```sh
cd pisa/
mkdir build/
cd build/
cmake ..
make sample_inverted_index compress_inverted_index create_wand_data thresholds lexicon
```

**We assume you already have a canonical inverted index, if not please check the [official documentation](https://pisa.readthedocs.io/)** 

## Sample the index
```sh
./bin/sample_inverted_index           \
        -c /path/to/GOV2.url.inv      \
        -o /path/to/GOV2.url.0.05.inv \
        -r 0.05                       \
        -t random_docids              \
        --terms-to-drop /path/to/GOV2.0.05.dropped_terms
```
## Compress the sampled index
```sh
./bin/compress_inverted_index         \
        -e block_simdbp               \
        -c /path/to/GOV2.url.0.05.inv \
        -o /path/to//GOV2.url.0.05.block_simdbp
```

## Create Metadata
```sh
./bin/create_wand_data                     \
        -c /path/to/GOV2.url.0.05.inv      \
        -o /path/to/GOV2.url.0.05.bm25.bmw \
        -s bm25                            \
        -b 128                             \
        --terms-to-drop /path/to/GOV2.0.05.dropped_terms
```

## Drop terms in lexicon and re-build

```sh
python script/drop_terms.py \
        -d /path/to/GOV2.0.05.dropped_terms \
        -t /path/to/GOV2.fwd.terms \
        -o /path/to/GOV2.fwd.0.05.terms
```

```sh
cd pisa/build/
./bin/lexicon build                  \
        /path/to/GOV2.fwd.0.05.terms \
        /path/to/GOV2.fwd.0.05.termlex
```

## Compute thresholds

```sh
./bin/thresholds                               \
        -e block_simdbp                        \
        -i /path/to/GOV2.url.0.05.block_simdbp \
        -w /path/to/GOV2.url.0.05.bm25.bmw     \
        -q  /path/to/queries.txt               \
        -s bm25                                \
        -k 4                                   \
        --terms /path/to/GOV2.fwd.0.05.termlex \
        --stemmer porter2 > ./gov2.0.05.top4.thresholds
```
