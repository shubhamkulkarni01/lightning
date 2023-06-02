"""Root package info."""
import logging
import os

# explicitly don't set root logger's propagation and leave this to subpackages to manage
_logger = logging.getLogger(__name__)
_logger.setLevel(logging.INFO)

_console = logging.StreamHandler()
_console.setLevel(logging.INFO)

formatter = logging.Formatter("%(levelname)s: %(message)s")
_console.setFormatter(formatter)
_logger.addHandler(_console)

from lightning.__about__ import *  # noqa: E402, F401, F403
from lightning.__version__ import version as __version__  # noqa: E402, F401
from lightning.app import storage  # noqa: E402
from lightning.app.core.app import LightningApp  # noqa: E402
from lightning.app.core.flow import LightningFlow  # noqa: E402
from lightning.app.core.work import LightningWork  # noqa: E402
from lightning.app.perf import pdb  # noqa: E402
from lightning.app.utilities.packaging.build_config import BuildConfig  # noqa: E402
from lightning.app.utilities.packaging.cloud_compute import CloudCompute  # noqa: E402
from lightning.fabric.fabric import Fabric  # noqa: E402
from lightning.fabric.utilities.seed import seed_everything  # noqa: E402
from lightning.pytorch.callbacks import Callback  # noqa: E402
from lightning.pytorch.core import LightningDataModule, LightningModule  # noqa: E402
from lightning.pytorch.trainer import Trainer  # noqa: E402
from lightning.pytorch.utilities.data import S3LightningDataset, LightningDataset # noqa: E402

import lightning.app  # isort: skip # noqa: E402

lightning.app._PROJECT_ROOT = os.path.dirname(lightning.app._PROJECT_ROOT)

# Enable breakpoint within forked processes.
__builtins__["breakpoint"] = pdb.set_trace

__all__ = [
    "LightningApp",
    "LightningFlow",
    "LightningWork",
    "BuildConfig",
    "CloudCompute",
    "Trainer",
    "S3LightningDataset",
    "LightningDataset",
    "LightningDataModule",
    "LightningModule",
    "Callback",
    "seed_everything",
    "Fabric",
    "storage",
    "pdb",
]
