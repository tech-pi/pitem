# This file is generated via pitem, DO NOT EDIT
import attrs


@attr.s
class ScanItem:
    id: attrs.ib(type=int)
    begin_position: attrs.ib(type=float)
    end_position: attrs.ib(type=float)
    is_denoise: attrs.ib(type=float, validator=is_in_range(0.000000, 1.000000))

