import shutil, re, sys
from bs4 import BeautifulSoup

#TODO point it to the doc folder 

#global buffer for latex
latex = []

def main():
    expression = re.compile("^%INSERT PROBLEMS HERE%")

    #Create copy of Homwork Assignment Template
    if len(sys.argv) < 2:
        print("Usage: python3 create_problem_set.py [num_of_problem_set]")
        return;
    try: 
        num = int(sys.argv[1])
    except:
        print("Please give a valid number")
        return

    if num > 10 or num < 0:
        print("Invalid index error")
        return;

    filename = './doc/HW-%i/HW-%i.tex'%(num,num)
    create_copy(filename)

    #Get dictionary of all problems
    #FIXME file location is incorrect
    homework_html_location = f"../Homework {num}/Homework {num}.html"
    dic = dict_items(homework_html_location)
    
    #Buffer to hold latex 
    for key,value in dic.items():
        latex.append(r"\section*{%s}"%(key))
        latex.append("\n")
        for i in range(len(value)):
            if len(value[i]) > 2:
                append_problem(f"{value[i][0]}{value[i][1]}")
                append_problem(f"{value[i][0]}{value[i][2]}")
            else:
                append_problem(value[i])


    # Adding ending of document to latex
    latex.append("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")
    latex.append(r"\end{document}")

    with open(filename, 'r+') as file:
        for line in file: 
            if expression.match(line):
                break;
        for line in latex:
            file.write(line)

    # Success
    print("Successful")   


def create_copy(filename):
    # Copy the template
    template = open('doc/homework-template.txt','rb')
    try:
        copyTemp = open(filename,'wb')
    except:
        print(f"{filename} could not be processed")
        return
    shutil.copyfileobj(template,copyTemp)

    # closing the Template
    template.close()
    copyTemp.close()


def append_problem(problem):
        latex.append(r"\begin{problem}{%s}"%(problem))
        latex.append("\n")
        latex.append(r"%Question here")
        latex.append("\n")
        latex.append(r"\end{problem}")
        latex.append("\n")
        latex.append(r"\begin{sol}")
        latex.append("\n")
        latex.append(r"%Solution here")
        latex.append("\n")
        latex.append(r"\end{sol}")
        latex.append("\n")
        latex.append("\n")

def dict_items(filename):

    if filename == None:
        filename = "Homework 1/Homework 1.html"
    # feed the soup
    with open(filename,'r') as file:
        content = file.read();
        soup = BeautifulSoup(content,"html.parser")

    secs = 2 #number of sections
    # regex to find problem questions
    section_num = re.compile(r"(?<=(Section ))\d.\d:")
    question_num = re.compile(r"(?<=,|>)\s?(\d\w*)")
    
    #store section nums 
    section_nums = []

    #store problem nums
    section_elements = []

    #Dictionary of problems and sections
    dic = {}

    # Gather the selection numbers
    for section in soup.find_all(string=section_num, limit=secs):
        section_nums.append(str(section).strip())

    #IXME can't limit it to 2 for future
    # it just so happens that what I want is first two
    for p in soup('p', limit=secs): 
        section_elements.append(str(p).strip())

    for i in range(len(section_elements)):
        dic[section_nums[i]] = question_num.findall(section_elements[i])
    
    return dic

if __name__ == "__main__":
    main()
