Coding style
============

We (mostly) follow the style guide from the the `Django project`_. Unless otherwise specified, follow this guide.
Please read this guide, use it, and feel free to point out if existing code does not comply with the style guide.

.. _Django project: https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/

Examples
^^^^^^^^

* Max line length is 119 characters
* Indentation is 4 spaces::

    for protein in proteins:
       print(protein)

* Comments start with a # and a single space::
    
    # this is a comment

* Docstrings use """::
    
    """This is a docstring"""

*   Use lower case letters and underscores for variable and function names, upper case letters and underscores for
    constants, and InitialCaps for class names::

        this_is_a_variable = True

        THIS_IS_A_CONSTANT = True

        def this_is_a_function():
           pass

        class ThisIsAClass:
           __init__(self):
              pass

* Class definitions are followed by 2 blank lines::
    
    class ThisIsAClass:
       __init__(self):
          pass


    class ...

*   Import statements are grouped in three categories(django, project, and other), separated by one blank line, and
    followed by 2 blank lines::
    
        from django.conf import settings

        from protein.models import Protein

        import yaml


        class ...

Keep your code clean
^^^^^^^^^^^^^^^^^^^^

Before committing, review the changes you have made (using git diff or a GUI like `SourceTree`_) and make sure the code
you are committing is working, and relevant. Never commit lines of code that are commented out (comments are for, well,
comments), or print statements that you used for debugging.

.. _SourceTree: https://www.sourcetreeapp.com
