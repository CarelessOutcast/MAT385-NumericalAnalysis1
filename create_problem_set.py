import shutil, re, sys

#TODO point it to the doc folder 


def main():
    expression = re.compile("^%INSERT PROBLEMS HERE%")

    #homework number
    num = int(sys.argv[1]) or 0
    if num == 0:
        print('please give a homework number: ')
        return -1
    filename = 'HW-%i.txt'%num
    # Copy the template
    template = open('homework-template.txt','rb')
    copyTemp = open(filename,'wb')
    shutil.copyfileobj(template,copyTemp)

    # closing the Template
    template.close()
    copyTemp.close()

    lines = []
    with open("problem-set.txt","r") as problem_set:
        for line in problem_set:
            # format the problem set to fit latex;
            if line.startswith("S"):
                section = line[1:].strip()
                lines.append(r"\section*{%s}"%(section))
                lines.append("\n")
            elif line.startswith("C"):
                computer = line.strip()
                lines.append(r"\section*{%s}"%(computer))
                lines.append("\n")
            else:
                number = line.strip()
                lines.append(r"\begin{problem}{%s}"%(number))
                lines.append("\n")
                lines.append(r"%Question here")
                lines.append("\n")
                lines.append(r"\end{problem}")
                lines.append("\n")
                lines.append(r"\begin{sol}")
                lines.append("\n")
                lines.append(r"%Solution here")
                lines.append("\n")
                lines.append(r"\end{sol}")
                lines.append("\n")
                lines.append("\n")

    lines.append("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")
    lines.append(r"\end{document}")

    with open(filename, 'r+') as file:
        for line in file: 
            if expression.match(line):
                break;
        for line in lines:
            file.write(line)

    # Success
    print("Successful")   


if __name__ == "__main__":
    main()
