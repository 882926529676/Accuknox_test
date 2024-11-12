


import re
from collections import Counter

LOG_FILE_PATH = "access.log"

LOG_PATTERN = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[.*?\] "GET (.*?) HTTP.*?" (\d{3})')

def parse_log_file(file_path):
    ips = []
    pages = []
    errors_404 = 0
    
    with open(file_path, 'r') as log_file:
        for line in log_file:
            match = LOG_PATTERN.search(line)
            if match:
                ip, page, status = match.groups()
                ips.append(ip)
                pages.append(page)
                if status == "404":
                    errors_404 += 1
    return ips, pages, errors_404

def generate_report(ips, pages, errors_404):
    ip_count = Counter(ips)
    page_count = Counter(pages)
    
    top_ips = ip_count.most_common(5)
    top_pages = page_count.most_common(5)

    print("\n--- Web Server Log Analysis Report ---")
    print(f"Total 404 Errors: {errors_404}\n")
    
    print("Top 5 IP Addresses:")
    for ip, count in top_ips:
        print(f"{ip}: {count} requests")
    
    print("\nTop 5 Requested Pages:")
    for page, count in top_pages:
        print(f"{page}: {count} requests")

def main():
    ips, pages, errors_404 = parse_log_file(LOG_FILE_PATH)
    generate_report(ips, pages, errors_404)

if __name__ == "__main__":
    main()
