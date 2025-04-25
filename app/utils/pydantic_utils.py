from pydantic import BaseModel


def create_model(
    model_name: str,
    **field_definitions: dict[str, tuple[type, str]]
) -> type:
    """
    Create a Pydantic model dynamically with the given field definitions.

    Args:
        model_name (str): The name of the model.
        **field_definitions (dict[str, tuple[type, str]]): Field definitions where the key is the field name,
            and the value is a tuple containing the field type and a description.

    Returns:
        type: A Pydantic model class.
    """
    return type(
        model_name,
        (BaseModel,),
        field_definitions
    )