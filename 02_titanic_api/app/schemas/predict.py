from typing import Any, List, Optional

from pydantic import BaseModel
from classification_model.processing.validation import TitanicDataInputSchema


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    predictions: Optional[int]


class MultipleTitanicDataInputs(BaseModel):
    inputs: List[TitanicDataInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "pclass": 1,
                        "name": "Vignesh",
                        "sex": "male",
                        "age": 54.0,
                        "sibsp": 0,
                        "parch": 0,
                        "fare": 51.8625,
                        "cabin": "E46",
                        "embarked": "McCarthy"
                    }
                ]
            }
        }
