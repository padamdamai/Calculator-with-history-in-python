import ast  #Abstract Syntax Tree
import operator
import os


#   __file__   path of the current file .py file
#  os.path.dirname folder containing the file

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HISTORY_FILE = os.path.join(BASE_DIR,'user_history.txt')

#define supported operators
operators = {
    ast.Add : operator.add,
    ast.Mult : operator.mul,
    ast.Sub : operator.sub,
    ast.Div : operator.truediv
}

def show_history():
    try:
        with open(HISTORY_FILE,'r') as f :
            content = f.read()
            if content.strip() == "":
                print("File is empty so no history found\n")
                return 0
            else :
                print(content.strip())
                return 1
    except FileNotFoundError:
        print("No file found\n")
        return -1

def clear_history():
    with open(HISTORY_FILE,'w') as f:
        print("History clearaed successfully\n")
        pass

def safe_eval(expression):
    def eval_node(node):
        # Base case :node is a number
        if isinstance(node,ast.Constant):
            return node.value
        # Base case : node is a binary operation
        elif isinstance(node,ast.BinOp):
            return operators[type(node.op)](
                eval_node(node.left),
                eval_node(node.right)
            )
        else:
            raise ValueError('Invalid expression\n')
        

    return eval_node(ast.parse(expression,mode='eval').body) # parse expression into AST and evaluate from the root


while True:
    user_expresison = input("\nEnter the operation :").strip()
    if user_expresison == "" :
        print('Invalid input\n')
        continue
    try:
        result = safe_eval(user_expresison)
        print(f"{user_expresison} : {result} \n ")
        with open(HISTORY_FILE,'a') as f:
            f.write(f"{user_expresison} : {result}\n")
        
        print("\n 1.Continue Calculation \n 2.Show History \n 3.Clear History \n 4.Exit")
        user_choice = input("\nEnter your choice (1/2/3/4) :").strip()
        if user_choice == "2":
            show_history()
        elif user_choice == "1":
            continue
        elif user_choice == "3":
            clear_history()
        elif user_choice == "4":
            print("Exiting the calculator .Goodbye\n")
            break 
        else:
            print("invalid choice\n")

    except Exception as e :
        print(f"Error:{e}")
