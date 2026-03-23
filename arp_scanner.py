import subprocess

def arp_scan():
    try:
        result = subprocess.run(
            ["arp", "-a"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        print("\n=== ARP Table ===")
        print(result.stdout)
    
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    arp_scan()