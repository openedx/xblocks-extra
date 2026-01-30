# xblocks-extra

A collection of XBlocks for the Open edX platform.

## Purpose

This repository contains XBlocks that are not installed by default in the Open edX platform but can be added as needed. XBlocks added here **preserve their original package paths** for drop-in replacement when migrating from standalone packages.

## Installation

```bash
pip install xblocks-extra
```

Or install specific xblocks by adding to your requirements:

```
xblocks-extra
```

## Development

### Prerequisites

- Python 3.12+
- Django 4.2 or 5.2

### Setup

```bash
# Clone the repository
git clone https://github.com/openedx/xblocks-extra.git
cd xblocks-extra

# Install in development mode
pip install -e ".[dev]"
```

### Running Tests

```bash
make test
```

### Linting

```bash
make lint
make format  # Auto-fix formatting issues
```

## Contributing

Contributions are welcome! Please read our [contributing guidelines](https://openedx.org/contributor-guidelines) before submitting a pull request.

## License

This project is licensed under the AGPL-3.0 License - see the [LICENSE](LICENSE) file for details.
