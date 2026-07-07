def crash_report(filepath):
    crp = 0
    c = 0
    s = 0
    
    try:
        with open(filepath, "r") as f:            
            for l in f:
                try:
                    tno, date, rs, status = l.strip().split("|")
                    
                    if  status.strip() == "FAILED":
                        c += 1
                        s += float(rs.strip())
                        
                except ValueError:
                    crp += 1
                    continue
    
    except FileNotFoundError:
        print(f"{filepath} file does not exists")
    
    except:
        print("Exception")

    return c,s, crp

t = crash_report("transactions.log")
print(t)