import subprocess

def check_nmap():
    try:
        subprocess.run(["nmap", "-v"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except:
        return False

def run_nmap(target):
    try:
        result = subprocess.run(
            ["nmap", target],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        print("\n=== Nmap Results ===")
        print(result.stdout)
    
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    print("=== Nmap Scanner ===")
    
    if not check_nmap():
        print("Nmap is not installed!")
    else:
        target = input("Enter target IP: ")
        run_nmap(target)