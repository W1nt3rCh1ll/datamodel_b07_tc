import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .unit import Unit


@forge_signature
class Parameter(sdRDM.DataModel):

    """"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("parameterINDEX"),
        xml="@id",
    )

    value: Optional[float] = Field(
        default=None,
        description="values.",
    )

    unit: Optional[Unit] = Field(
        default=None,
        description="unit of the values.",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel_b07_tc.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="cfa50a71b09fa2d5fb0c474c7a62a01f2acacf98"
    )
