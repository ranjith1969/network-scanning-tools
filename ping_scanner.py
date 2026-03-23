import subprocess
import platform

def ping_host(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    
    try:
        result = subprocess.run(
            ["ping", param, "4", host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        if result.returncode == 0:
            print("\nHost:", host)
            print("Status: Reachable")
        else:
            print("\nHost:", host)
            print("Status: Not reachable")
    
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    print("=== Ping Scanner ===")
    host = input("Enter IP or hostname: ")
    ping_host(host)