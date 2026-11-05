from .basic import OPERATIONS as BASIC_OPS
from .advanced import OPERATIONS as ADVANCED_OPS
from .memory import Memory

ALL_OPERATIONS = {
    **BASIC_OPS,
    **ADVANCED_OPS,
}
