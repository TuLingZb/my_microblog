def chengke(z):
    d = {}
    d["西单"] = ["爱国","建国"]
    d["天安门"] = d["西单"].copy()
    d["天安门"].append("国庆")
    d["天安门"].remove("建国")
    d["国贸"] = d["天安门"].copy()
    d["国贸"].append("卫国")
    d["国贸"].remove("爱国")
    d["四惠"] = d["国贸"].copy()
    d["四惠"].append("建军")

    return d[z]

if __name__ == "__main__":
    z = "国贸"
    a = chengke(z)
    print(a)