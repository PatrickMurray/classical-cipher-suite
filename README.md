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
pip3 install -r pip3-requirements.txt
```


### Code Checks

#### Linting

```bash
pylint
```


#### Test Cases

```bash
python3 -m pytest
```
