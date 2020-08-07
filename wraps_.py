# def bag(a,b):
#     def wraps(f):
#         print("f",f.__name__)
#         # f()
#         print("a+b",a+b)
#         return a+b
#     return wraps
#
# @bag(2,3)
# def dep():
#     print("dep")


class Po():
    def __init__(self):
        self.l = []
        pass

    def r(self, name):
        def wraps(f):
            print(name)
            # print("weq")
            # self.l.append(name)
            return f
        return wraps


p = Po()


@p.r("12")
def lo():
    print("sad")



def get_dict_list(list):
    dict = {}
    for i in list:
        if dict.get(len(i)):
            if i not in dict.get(len(i)):
                dict[len(i)].append(i)
            continue
        dict[len(i)] = [i]
    return dict


if __name__ == "__main__":
    a = [[1,2],[2,3],[3,3,3,4,5],[33,56,89,1001]]
    c = get_dict_list(a)
    print(c)
    print(globals())
