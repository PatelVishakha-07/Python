def crash_report(filepath):
    try:
        with open(filepath, "r") as f:
            c = 0
            s = 0
            for l in f:
                tno, date, rs, status = l.strip().split("|")
                
                if  status.strip() == "FAILED":
                    c += 1
                    s += float(rs.strip())
            
            return c,s
    
    except FileNotFoundError:
        print(f"{filepath} file does not exists")
    
    except:
        print("Exception")

t = crash_report("transactions.log")
print(t)