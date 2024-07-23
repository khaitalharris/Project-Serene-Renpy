init python:
    from typing import cast, Union

    from renpy.python import RevertableList

    def string_to_list(given_text: Union[str, list[str]]) -> list[str]:
        """Turn a string into a list containing that string.

        Each list item represents a paragraph.
        If a string is given, convert it to a list,
        assuming a string with no list == one paragraph.

        Args:
            given_text: The string to transform.

        Return:
            list[str]
        """
    # If the text is already in a list, just return it.
        if type(given_text) in (RevertableList, list):
            return cast(list[str], given_text)

        return [cast(str, given_text)]

    my_encyclopaedia = Encyclopaedia()
    ShowMenu(my_encyclopaedia.list_screen, my_encyclopaedia)

    about_zeus = EncEntry(
    parent=my_encyclopaedia,
    name="Zeus",
    text=[
        "Zeus is the sky and thunder god in ancient Greek religion, who ruled as king of the gods of Mount Olympus."
        " His name is cognate with the first element of his Roman equivalent Jupiter."
        " His mythologies and powers are similar, though not identical, to those of Indo-European deities such as Indra, Jupiter, Perun, Thor, and Odin."
    ],
    image="scrolling_cave",
    viewed_persistent=True,
    locked_persistent=True,
    )
    about_zeus = EncEntry(
    parent=my_encyclopaedia,
    name="Odin",
    
    text=[
        "Odin is the sky and thunder god in ancient Greek religion, who ruled as king of the gods of Mount Olympus."
        " His name is cognate with the first element of his Roman equivalent Jupiter."
        " His mythologies and powers are similar, though not identical, to those of Indo-European deities such as Indra, Jupiter, Perun, Thor, and Odin."
    ],
    image="Mage",
    viewed_persistent=True,
    locked_persistent=False,
)


