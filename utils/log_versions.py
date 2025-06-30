import sys
import platform
import pkg_resources

def log_versions():
    print("Python:", sys.version)
    print("Platform:", platform.platform())
    for dist in pkg_resources.working_set:
        print(f"{dist.project_name}=={dist.version}")
