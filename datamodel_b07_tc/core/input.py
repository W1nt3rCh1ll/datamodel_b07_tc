import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .reactantrole import ReactantRole
from .chemical import Chemical
from .stoichiometry import Stoichiometry


@forge_signature
class Input(sdRDM.DataModel):
    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("inputINDEX"),
        xml="@id",
    )

    component: List[Chemical] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="component of the output fluid.",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel_b07_tc.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="c7407c28baaf7f0667ca7e50953202a7c1ae7ff5"
    )

    def add_to_component(
        self,
        name: List[str] = ListPlus(),
        formula: Optional[str] = None,
        pureness: Optional[float] = None,
        supplier: Optional[str] = None,
        stoichiometry: Optional[Stoichiometry] = None,
        state_of_matter: Optional[str] = None,
        reactant_role: Optional[ReactantRole] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Chemical' to attribute component

        Args:
            id (str): Unique identifier of the 'Chemical' object. Defaults to 'None'.
            name (): IUPAC name of the compound.. Defaults to ListPlus()
            formula (): molecular formula of the compound.. Defaults to None
            pureness (): pureness of the compound in percent.. Defaults to None
            supplier (): name of the supplier of the compound.. Defaults to None
            stoichiometry (): stoichiometric information like equivalents, mass, amount of substance, volume. Defaults to None
            state_of_matter (): s for solid, l for liquid and g for gaseous. Defaults to None
            reactant_role (): Role that a reactand plays in a chemical reaction or  in a process.. Defaults to None
        """

        params = {
            "name": name,
            "formula": formula,
            "pureness": pureness,
            "supplier": supplier,
            "stoichiometry": stoichiometry,
            "state_of_matter": state_of_matter,
            "reactant_role": reactant_role,
        }

        if id is not None:
            params["id"] = id

        self.component.append(Chemical(**params))

        return self.component[-1]
