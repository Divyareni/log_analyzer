from collections import Counter

def generate_report(parsed_logs):
    status_count = Counter([log['status'] for log in parsed_logs if 'status' in log])
    report = ["Status code report:"]
    for status,count in status_count.items():
        report.append(f"{status}:{count}")
    return "\n".join(report)
