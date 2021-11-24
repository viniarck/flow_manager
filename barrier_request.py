from pyof.v0x01.controller2switch.barrier_request import BarrierRequest as BReq10
from pyof.v0x04.controller2switch.barrier_request import BarrierRequest as BReq13


def new_barrier_request(version, **kwargs):
    """Instantiate a barrier request given an OF version."""
    barrier_requests = {0x01: BReq10(**kwargs), 0x04: BReq13(**kwargs)}
    return barrier_requests[version]
