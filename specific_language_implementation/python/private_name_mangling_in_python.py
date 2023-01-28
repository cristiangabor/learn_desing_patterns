# Python almost does not offer any protection mechanism for private methods and attributes
# The exception comes for methods where they are declared with double-underscore prefix.
# The process of renaming methods and attributes with a double-underscore is called
# private name mangling

class Main:

    def __init__(self):
        self.__boya()
        
    def __boya(self):
        print("Boya!")

class SubclassMain(Main):
    
    def __boya(self):
        print("Boya mama!")


SubclassMain()

# Problem: Child __boya method does not get called when child object is called
# Explanation: The point of using double-underscore name convention is to prevent
# subclasses from accidentally overriding the method

class SubclassSecondMain(Main):

    # Rule of overrding ( _ + parent class name + __ + method name)
    def _Main__boya(self):
        print("Time for more boyaa!")


# This is a serious desing flaw if you have to override a double-underscore method
# To overcome this you have to prefixt ( _ +) the method name with single-undersore
# followed by Parent classname and the double-underscored method name you want to 
# override. 

SubclassSecondMain()



"""
This work comes from analysis of SOLID Principles. 

# Liskov Substituion Principle 
# Requirement of a subclass - A subclass shouldn't change values of 
private fields of the superclass

During my analisys of this requirement from this principles I've found
out that where some programming languages offers ways to bypass this rule
through different internal language mechanisms (like the reflecation mechanism in Java),
other languages does not offer at all protection from overrding private fields of the superclass.
"""