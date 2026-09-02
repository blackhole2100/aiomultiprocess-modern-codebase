# Copyright 2022 K O
# Licensed under the MIT license

import logging
import sys

from .core import CoreTest
from .perf import PerfTest
from .pool import PoolTest
from .scheduler import SchedulerTest

logging.basicConfig(level=logging.INFO, stream=sys.stderr)
