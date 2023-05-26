import sdRDM

from typing import List, Optional
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .author import Author


@forge_signature
class GeneralInformation(sdRDM.DataModel):

    """"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("generalinformationINDEX"),
        xml="@id",
    )

    title: Optional[str] = Field(
        default=None,
        description="title of the work.",
    )

    description: Optional[str] = Field(
        default=None,
        description="describes the content of the dataset.",
    )

    authors: List[Author] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="authors of this dataset.",
    )

    def add_to_authors(
        self,
        name: Optional[str] = None,
        affiliation: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Author' to attribute authors

        Args:
            id (str): Unique identifier of the 'Author' object. Defaults to 'None'.
            name (): full name including given and family name.. Defaults to None
            affiliation (): organization the author is affiliated to.. Defaults to None
        """

        params = {
            "name": name,
            "affiliation": affiliation,
        }

        if id is not None:
            params["id"] = id

        self.authors.append(Author(**params))
