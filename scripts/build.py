import os, contextlib
import subprocess

from pathlib import Path

CL_DIR = "C:/Program Files (x86)/Microsoft Visual Studio 9.0/VC/bin/"
CL_DIR = Path(CL_DIR).resolve()


@contextlib.contextmanager
def CD(dir: str):
    old_dir = os.getcwd()
    os.chdir(dir)
    yield
    os.chdir(old_dir)


def vs2008_set_env():
    with CD(CL_DIR):
        output = subprocess.getoutput('cmd /c "vcvars32.bat&set"')
        for line in output.split("\n"):
            if "=" in line:
                key, val = line.split("=")
                os.putenv(key, val)


if __name__ == "__main__":
    vs2008_set_env()
    project_dir = Path(__file__).resolve().parent.parent
    with CD(project_dir):
        subprocess.run(
            "vcbuild piapprox.vcproj Debug /Platform:win32 /Rebuild".split(), check=True
        )
