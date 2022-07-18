import ast


class StackElement:
    def __init__(self, functionName, params):
        self.key = functionName
        self.val = params


# right is the top of the stack
stack = []


class ExpressionVisitor(ast.NodeVisitor):
    def visit_Call(self, node):

        if node.func.id not in ["join", "concatenate", "pickRandom"]:
            raise Exception("Unsupported Method Invocation")
        elif node.func.id == "join" and len(node.args) < 3:
            raise Exception("Minimum of 3 parameters necessary for join()")
        elif node.func.id == "concatenate" and len(node.args) < 1:
            raise Exception("Minimum 1 parameter necessary for concatenate()")
        elif node.func.id == "pickRandom" and len(node.args) < 1:
            raise Exception("Minimum of 1 parameter necessary for pickRandom()")

        args = []
        for i in node.args:
            if isinstance(i, ast.Constant):
                args.append(i.value)

        # arg-list will only have constants, not function calls

        stack.append(StackElement(node.func.id, args))
        self.generic_visit(node)


def getTokenizedStack(expr):
    # print(ast.dump(ast.parse(expr)))
    ExpressionVisitor().visit(ast.parse(expr))

    return stack
