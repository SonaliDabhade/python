import subprocess    
    
with open("output.txt", "wb") as f:    
    subprocess.check_call(["java", "Main"], stdout=f)    