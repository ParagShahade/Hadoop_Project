
#!/usr/bin/python
# Your task is to make sure that this mapper code does not fail on corrupt data lines,
# but instead just ignores them and continues working
import sys
import pandas

def mapper():
    # read standard input line by line
    data=pandas.read_csv("Project.csv")
    for line in data.index:
        # strip off extra whitespace, split on tab and put the data in an array
        price = (data['Price'][line]).replace(",","")
        country = data['Country'][line]
        product = data['Product'][line]

 # Now print out the data that will be passed to the reducer
        print(price,country,product)

def main():

	mapper()


if __name__ == "__main__":
    main()
