import dns.resolver


def get_dns_records(domain, record_type):
    try:
        answers = dns.resolver.resolve(domain, record_type)

        records = []

        for answer in answers:
            records.append(str(answer))

        return records

    except Exception:
        return []
