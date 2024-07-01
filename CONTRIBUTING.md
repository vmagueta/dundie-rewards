# Contributing to Dundie Project

Summary of project

## Guidelines

- Backwards compatibility.
- Multiplatform.
- Python 3 only.

## Code of Conduct

- Be gentle.

## How to contribute

### Fork repository

- Click fork buttom on [github repository](https://github.com/vmagueta/dundie-rewards)

### Clone to local dev environment

```bash
git clone https://github.com/vmagueta/dundie-rewards
...
```

### Prepare virtual env

```bash
cd dundie-rewards
make virtualenv
make install
```

### Coding style

- This projects follows PEP8.

### Run tests

```bash
make test
# or
make watch
```

### Commit rules

- We follow conventional commit messages. ex: `[bugfix] reason #issue`
- We required signed commits.

### Pull Request Rulls

- We required all tests to be passing.
