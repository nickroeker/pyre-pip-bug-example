# pyre-pip-bug-example

This is to report on a bug filed with Pyre, intended to help reproduce the bug.

Please run `./repro.sh` on Linux, or mimic its steps on your local operating
system:

* Create a virtual environment and activate it
* Install for development with `pip install -e .` (this will fetch pyre-check too)
* `pyre init`
* Type-check the package: `pyre --preserve-pythonpath --source-directory my_package check`
