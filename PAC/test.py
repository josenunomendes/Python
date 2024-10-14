def main():
    val = input("tabuada\n")
    lim_sup = input("limite superior\n")
    lim_inf = input("limite inferior\n")

    try:
        val = int(val)
        lim_sup = int(lim_sup)
        lim_inf = int(lim_inf)

    except ValueError:
        print("Error")
        exit()

    if lim_inf <= val <= lim_sup and lim_inf <= lim_sup:
        for i in range(lim_inf, lim_sup + 1):
            print(val, "*", i, "=", val * i)
        
    else:
        print("Error")

if __name__ == "__main__":
    main()