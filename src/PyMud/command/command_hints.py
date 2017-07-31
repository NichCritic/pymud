
from parsimonious.expressions import *
from command.command_token_matcher import build_grammar

tok_print = ('print',)

if __name__ == "__main__":
    grammar = build_grammar(["table", "chair"], [
                            "expelliarmus", "avada kedavra"], ["move", "say"])

    stack = []
    stack.append(tok_print)
    stack.append(grammar.default_rule)

    out = ""

    while len(stack) > 0:
        #print(stack)
        
        item = stack.pop()
        if type(item) is Sequence:
            stack.append(tok_print)
            stack.extend(reversed(item.members))
        if type(item) is OneOf:
            #import pdb; pdb.set_trace()
            s = list(reversed(stack))
            p_index = s.index(tok_print)
            stack = stack[:-p_index]
            for i in reversed(item.members):
                stack.append(tok_print)
                stack.extend(reversed(s[:p_index]))
                stack.append(i)
                stack.append(out)
        if type(item) is Literal:
            #import pdb; pdb.set_trace()
            out += str(item.literal)

        if isinstance(item, str):
            out += item
        if item is tok_print:
            #print(stack)
            print(out)

            #import pdb; pdb.set_trace()
            out = ""
