## Introduction

Machine learning researchers frequently need to experiment with different parameter configurations to fine-tune their models. Managing these configurations efficiently poses a significant challenge. 
To address this, we developed **Ym2**, a configuration management framework inspired by [torchtune](https://github.com/pytorch/torchtune)

Ym2 provides:

- Declaration of custom Python classes and parameters through `yaml` configuration files
- Simple configuration overrides via command-line arguments
- Support for multiple experimental runs with different configurations
- Comprehensive experiment logging and management

## Examples
- [Hello World Example](sample/)
