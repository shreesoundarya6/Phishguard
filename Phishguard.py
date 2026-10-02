from urllib.parse import urlparse
print("========== PHISHGUARD ==========")
url = input("Enter the website URL: ")
if not url.startswith(("http://", "https://")):
    url = "http://" + url
domain = urlparse(url).netloc.lower()
if url.startswith("https://"):
    print("HTTPS is used")
else:
    print(" HTTP is used")
words = ["login", "verify", "password", "bank", "account"]
for word in words:
    if word in domain:
        print(" Suspicious word found:", word)
if "@" in url:
    print("@ symbol is found")
else:
    print(" @ symbol is not used")
if len(url) > 80:
    print("URL is too long")
else:
    print("URL length is normal")
if domain.count(".") > 3:
    print("Too many subdomains")
else:
    print(" Subdomain count is normal")

print("\n========== SCAN COMPLETE ==========")
