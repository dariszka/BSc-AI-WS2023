import re

def extract_emails(text: str) -> list[str]:
    username = '[A-Za-z0-9._%+-]+'
    subdomain = '[A-Za-z0-9.-]+'
    top_level_domain = '[A-Za-z]{2,}'
    pattern = rf'(?:\s|^)({username}@{subdomain}\.{top_level_domain})'
 
    match_list = re.findall(pattern, text)
    return match_list


# t = """
# Here are some email addresses:
# john.doe@example.com, alice_smith123@gmail.com, ABC+@a-b-c.aBc,
# contact@company.org, and info@sub.domain.co.uk.
# Some invalid email addresses are:
# john@, @example.com, user@domain, us/er@email.com,
# invalid@domain.f and invalid.email@invalid@domain.com.
# """
# print(extract_emails(t))
