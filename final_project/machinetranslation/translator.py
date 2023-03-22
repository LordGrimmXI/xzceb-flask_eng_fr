
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


def frenchToEnglish(frenchText):
    if frenchText is None:
        return ""
    # Set up authentication
    authenticator = IAMAuthenticator('7wAYuwlNpcPlmTahsP_kMttb-A4HDcNBny3MjiUjsOR_')
    language_translator = LanguageTranslatorV3(
        version='2023-03-22',
        authenticator=authenticator
    )
    language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/ce4cb711-e30d-4ccc-bca8-91774982e9a8')

    # Translate text
    translation = language_translator.translate(
        text=frenchText,
        model_id='fr-en'
    ).get_result()

    # Parse JSON response to get translation
    translation_text = translation['translations'][0]['translation']

    return translation_text

def englishToFrench(englishText):
    if englishText is None:
        return ""
    # Set up authentication
    authenticator = IAMAuthenticator('7wAYuwlNpcPlmTahsP_kMttb-A4HDcNBny3MjiUjsOR_')
    language_translator = LanguageTranslatorV3(
        version='2023-03-22',
        authenticator=authenticator
    )
    language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/ce4cb711-e30d-4ccc-bca8-91774982e9a8')

    # Translate text
    translation = language_translator.translate(
        text=englishText,
        model_id='en-fr'
    ).get_result()

    # Parse JSON response to get translation
    translation_text = translation['translations'][0]['translation']

    return translation_text
