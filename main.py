from log_parser import parse_log_line
from report_generator import generate_report

def main():
    parsed_logs = []

    with open("logs/sample.log") as f:
        for line in f:
            parsed = parse_log_line(line)
            if parsed:
                parsed_logs.append(parsed)
    print("parsed logs is", parsed_logs)
    report = generate_report(parsed_logs)
    print(report)
if __name__ == "__main__":
    main()
