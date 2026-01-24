'''Write a program that reads a Python file and counts
number of functions
number of classes
number of comment lines.'''
def analyze_python_file(filename):
    function_count=0
    class_count=0
    comment_count=0
    with open("mixed.txt","r") as file:
        for line in file:
            line=line.strip()
            if line.startswith("def"):
                function_count+=1
            elif line.startswith("class"):
                class_count+=1
            elif line.startswith("#"):
                comment_count+=1
    print(f"No. of def_function:{function_count}")
    print(f"No. of class:{class_count}")
    print(f"No. of comment:{comment_count}")
analyze_python_file("38_problem.py")