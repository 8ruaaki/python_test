def function(name):
  print("こんにちは、私の名前は" + name + "です！")

function("Haruaki")
##こんにちは、私の名前はHaruakiです！

def print_hi(name):
    print(f'Hi,{name}')

if __name__ == '__main__':
    my_name = input("your name?")
    print_hi(my_name)
