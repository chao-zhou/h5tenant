import re

patten = 'tenantInQueryString \? tenantInQueryString : \(i > -1 \? location.host.substring\(0, i\) : "[^"]+"\)'
replace_template = 'tenantInQueryString ? tenantInQueryString : (i > -1 ? location.host.substring(0, i) : "{0}")'

regex = re.compile(patten)


def replace_tenant(content, tenant):
    replace = replace_template.format(tenant)
    new_content, number_of_replace = regex.subn(replace, content)
    return new_content, number_of_replace
