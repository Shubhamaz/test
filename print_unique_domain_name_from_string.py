email = 'shubham.z@gmail.com, saurabh.p54@yahoo.com, roshan.z221@live.com'

def is_valid_domain(domain):
    if domain and domain[0].count('.') == 1:
        return True
    return False

def get_domain(emails):
    result = []
    for email in emails.split(','):
        domain = email.split('@')[1:]
        if is_valid_domain(domain) and domain[0] not in result:
            result.append(domain[0])
    return result

print(get_domain(email))
