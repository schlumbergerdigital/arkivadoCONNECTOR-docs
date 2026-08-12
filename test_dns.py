import dns.resolver

def dns_resolver(dom_name,type="A",nameservers=['88.198.229.192','213.133.100.98','193.47.99.5']):

    adresses = []
    dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
    dns.resolver.default_resolver.nameservers = nameservers
    try:
        answers = dns.resolver.query(dom_name, "A")
        for answer in answers:
            adresses.append(answer)
    except:
         pass 

    return adresses