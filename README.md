# Minimal Kedro Pipeline

This repo represents the minimal amount of structure to build a kedro pipeline that can be shared accross projects.

## Installation

```
pip install git+https://github.com/WaylonWalker/mini-kedro-pipeline
```

## Caveats

No this is not a runnable pipeline, kedro still wants a full conf directory to setup credentials, logging, and catalog.  This is a sharable pipeline that can be used accross many different projects.


## Usage

Once installed this proeject can be added to your standard `hooks.py` file.

``` python
# hooks.py

import mini_kedro_project as mkp

class ProjectHooks:
    @hook_impl
    def register_pipelines(self) -> Dict[str, Pipeline]:
        """Register the project's pipeline.

        Returns:
            A mapping from a pipeline name to a ``Pipeline`` object.

        """

        return {"__default__": Pipeline([]), "mkp": mkp.pipeline}

```

