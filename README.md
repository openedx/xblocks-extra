# xblocks-extra

A collection of XBlocks for the Open edX platform.

## Purpose

This repository serves as the consolidated home for several previously standalone XBlock packages, brought together to streamline maintenance and simplify dependency management. These XBlocks are not installed by default in the Open edX platform but can be added as needed. Each XBlock **preserves its original package path** to serve as a drop-in replacement when migrating from the standalone packages.

The following XBlocks have been migrated here from their respective repositories:

- [AudioXBlock](src/audio/README.md) migrated [from](https://github.com/openedx-unsupported/AudioXBlock)
- [FeedbackXBlock](src/feedback/README.rst) migrated [from](https://github.com/openedx/FeedbackXBlock)
- [xblock-image-modal](src/imagemodal/README.rst) migrated [from](https://github.com/openedx-unsupported/xblock-image-modal)
- [xblock-qualtrics-survey](src/qualtricssurvey/README.rst) migrated [from](https://github.com/openedx-unsupported/xblock-qualtrics-survey)
- [xblock-sql-grader](src/sql_grader/README.rst) migrated [from](https://github.com/openedx/xblock-sql-grader)
- [xblock-submit-and-compare](src/submit_and_compare/README.md) migrated [from](https://github.com/openedx-unsupported/xblock-submit-and-compare)


## Installation

```bash
pip install xblocks-extra
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
