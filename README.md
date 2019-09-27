# Classical Cipher Suite (CCS)

The goal of this repository is to be a playground for the experimentation of
classical cryptographic ciphers.


## Development

### Local Environment

#### Virtual Environment

##### Activation

```bash
virtualenv --python python3 venv
source venv/bin/activate
```

##### Deactivation

```bash
deactivate
```


#### Dependencies

```bash
pip3 install -r requirements.txt
```

#### Development Installation

```bash
pip3 install -e .
```


### Code Checks

#### Linting

```bash
pylint ccs
```


#### Test Cases

```bash
pytest
```
