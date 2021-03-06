"""
This is the first class defined in this API! It only cares about names.
"""


class Class1:
    """
    Description of the class Class1.

    This class does nothing in particular, it only contains a name given at initialization.

    :param name: A string, the name to be given to the Class1 instance.
    """
    
    def __init__(self, name: str):

        self.name = name

    def my_name_is(self):
        """
        Completes the sentence 'My name is ' with the `name` of the class

        This very complicated method relies on a Class1 object to make a sentence.
        
        
        :return: A string which is a sentence.
        """

        return 'My name is ' + self.name

    def guess_my_name(self, name: str):
        """
        Checks if `name` is the current Class1's name.

        If the name is correct, returns 'You guessed my name, you're a genius.'
        If not, return 'Try again!'

        :param name: A string, the name to test again Class1's name
        :return: A string indicating whether the guessed name was correct or not
        """

        answer = ''

        if self.name == name:
            answer = "You guessed my name, you're a genius"
        else:
            answer = 'Try again'

        return answer
