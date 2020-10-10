## Build PISA

```sh
cd pisa/
mkdir build/
cd build/
cmake ..
make sample_inverted_index compress_inverted_index create_wand_data thresholds
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
