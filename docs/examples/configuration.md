---
title: Configuration
---

## Generate JSON configuration file

To generate a JSON configuration file, run the following command:

```sh
splitme-ai --config.generate
```

A JSON configuration file will be generated in the current directory, named `.splitme.yaml`. This file contains all the configuration options available for the tool.

You can also specify the output file name and path by providing the `--config.file` option:

```sh
splitme-ai --config.generate --config.file .splitme-config.yml
```

## Load JSON configuration file
