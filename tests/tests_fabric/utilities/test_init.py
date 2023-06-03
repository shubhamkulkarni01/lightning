# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import torch.nn

from lightning.fabric.utilities import _EmptyInit
from tests_fabric.helpers.runif import RunIf


# standalone because we need memory metrics isolated from other processes
@RunIf(min_cuda_gpus=1, standalone=True)
def test_empty_init_memory_allocation():
    """Test that no memory gets allocated when using the `_EmptyInit()` context manager."""
    with _EmptyInit(enabled=True):
        torch.nn.Linear(100, 100, device="cuda")
    assert torch.cuda.memory_allocated() == 0
    torch.cuda.synchronize()

    with _EmptyInit(enabled=False):
        torch.nn.Linear(100, 100, device="cuda")
    assert torch.cuda.max_memory_allocated() > 0
