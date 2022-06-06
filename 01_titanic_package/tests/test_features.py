from classification_model.config.core import config
from classification_model.processing.features import ExtractLetterTransformer


def test_temporal_variable_transformer(sample_input_data):
    print(sample_input_data.shape)
    sample_input_data = sample_input_data[config.model_config.features]
    # Given
    transformer = ExtractLetterTransformer(
        variables=config.model_config.variable_to_get_first_letter
    )
    assert sample_input_data["cabin"].iat[0] == "B5"

    # When
    subject = transformer.fit_transform(sample_input_data)
    print("transformed")

    # Then
    assert subject["cabin"].iat[0] == "B"
