
print("Code Begin")

home_url = 'https://parivahan.gov.in/rcdlstatus/'
post_url = 'https://parivahan.gov.in/rcdlstatus/?pur_cd=101'

DLNumber = 'DL-0420110149646'
DOB = '09-02-1978'

CookieRequest = 'requests.get(url=home_url)'

soup =" Beautiful Soup'(CookieRequest.text, 'html.parser')"
print("View State")
ViewState = "soup.select('input[name='State X1']"
print(ViewState)

button = "soup.find"("button",{"type": "submit"})
print(button['id'])

data = {
    'javax.faces.partial.ajax':'true',
    'javax.faces.source': button['id'],
    'javax.faces.partial.execute':'@all',
    'javax.faces.partial.render': 'form_rcdl:pnl_show form_rcdl:pg_show form_rcdl:rcdl_pnl',
    button['id']:button['id'],
    'form_rcdl':'form_rcdl',
    'form_rcdl:tf_dlNO': DLNumber,
    'form_rcdl:tf_dob': DOB,
    'javax.faces.ViewState': viewstate,
}

r = requests.post(url=post_url, data=data, cookies=CookieRequest)

soup = BeautifulSoup(r.text, 'html.parser')
table = SoupStrainer('tr')
soup = BeautifulSoup(soup.get_text(), 'html.parser', parse_only=table)
print(soup.get_text())



