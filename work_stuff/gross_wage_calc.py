#wage
name1_wage = <>
name2_wage = <>
name3_wage = <>
name4_wage = <>

#overtime wage
name1_ot = (name1_wage/2) + name1_wage
name2_ot = (name2_wage/2) + name2_wage
name3_ot = (name3_wage/2) + name3_wage
name4_ot = (name4_wage/2) + name4_wage


def wage_calc(hours, wage, ot_wage):
    if hours <= 40:
        wage_total  = hours * wage
        return wage_total 
    else:
        overtime = hours - 40 
        ot_total = overtime * ot_wage
        wage_total = 40 * wage
        total_wage = wage_total + ot_total
        return total_wage


def main():
    
    name1_hrs = float(input("Enter name1 hours: "))
    name2_hrs = float(input("Enter name2 hours: ")) 
    name3_hrs = float(input("Enter name3 hours: "))
    name4_hrs = float(input("Enter name4 hours: "))
    print("\n")
    
    name1 = wage_calc(name1_hrs, name1_wage, name1_ot)
    name2 = wage_calc(name2_hrs, name2_wage, name2_ot)
    name3 = wage_calc(name3_hrs, name3_wage, name3_ot)
    name4 = wage_calc(name4_hrs, name4_wage, name4_ot)

    print("Name1: ", name1)
    print("Name2: ", name2)
    print("Name3: ", name3)
    print("Name4: ", name4)
    print("\n")



    print("Total Amount: ", (name1 +  name2 +  name3 + name4))



if __name__ == "__main__":
    main()
