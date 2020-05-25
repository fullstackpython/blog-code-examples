import argparse
import importlib
import os
import pkgutil
import sentry_sdk
from sentry_sdk import capture_exception

# find on https://docs.sentry.io/error-reporting/quickstart/?platform=python
sentry_sdk.init(dsn=os.getenv('SENTRY_DSN'))


def import_submodules(package):
    """Import all submodules of a module, recursively, including subpackages.

    :param package: package (name or actual module)
    :type package: str | module
    :rtype: dict[str, types.ModuleType]
    """
    if isinstance(package, str):
        package = importlib.import_module(package)
    results = {}
    for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
        full_name = package.__name__ + '.' + name
        try:
            results[full_name] = importlib.import_module(full_name)
            if is_pkg:
                results.update(import_submodules(full_name))
        except ModuleNotFoundError as mnfe:
            print("module not found: {}".format(full_name))
            capture_exception(mnfe)
        except Exception as general_exception:
            print(general_exception)
            capture_exception(general_exception)
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("package")
    args = parser.parse_args()

    package_to_load = args.package
    results = import_submodules(package_to_load)
    for r in results:
        print(str(r))
