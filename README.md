# ml4pd_models

Repo/package of ML models to be used by ML4PD. Currently, each compositions number has a separate set of models for a type of unit op. Each set of models contains 4 models - classifier, regressor for flowrates, regressor for duty, regressor for temperature. Potential major changes to this repo that would break ml4pd compatibility:

1. The #/type of features might change, rendering pipelines built into ml4pd incompatible.
2. More sophisticated models are used so that 1 set of models will work for an indeterminate number of compositions.
3. More sophisticated models are used so that each set of models contains only 2 models - 1 classifier and 1 regressor.

To add new models for units, create a directory with name `f"{unit}_models"`, then add __init__.py in that directory along with model files. To deploy, add `include ml4pd_models/{unit}_models/*` in MANIFEST.in.