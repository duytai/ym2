## Introduction

Machine learning researchers frequently need to experiment with different parameter configurations to fine-tune their models. Managing these configurations efficiently poses a significant challenge. 
To address this, we developed **Ym2**, a configuration management framework inspired by [torchtune](https://github.com/pytorch/torchtune)

Ym2 provides:

- Declaration of custom Python classes and parameters through `yaml` configuration files
- Simple configuration overrides via command-line arguments
- Support for multiple experimental runs with different configurations
- Comprehensive experiment logging and management

## Installation
We use **Ym2** daily and continually improve and add more features
```bash
# Install the latest version
pip install ym2

# Change to sample directory
cd sample/

# Run hello world example
ym2 configs/config.yaml

# Override parameter `name`
ym2 configs/config.yaml name=X

# Execute sequentially with `name=X` and `name=Y`
ym2 configs/config.yaml name=X,Y

# Adding new parameters `x` and `y`
ym2 configs/config.yaml x=1 y=2
```
```python
from ym2 import instantiate
hello_world: DictConfig = ...

# Create a new class instance from a configuration
obj = instantiate(hello_world)

# Adding additional parameters
obj = instantiate(hello_world, x=1, y=2)
```

## Feedback
Create a new pull request

