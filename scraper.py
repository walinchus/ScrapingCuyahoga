import scraperwiki
import lxml.html
import mechanize

def scrape_table(root):
    #grab all table rows <tr> in table class="tblSearchResults"
    rows = root.cssselect("table.caseCourtTable tr")
    #create an ID number set at 0 - will add 1 every time we store a record (below)
    idno = 0
    #create a record to hold the data
    record = {}
    #for each row, loop through this
    for row in rows:
        #create a list of all cells <td> in that row
        table_cells = row.cssselect("td")
        if table_cells: 
        #if there is a cell, record the contents in our dataset, the first cell [0] in 'recipient' and so on
            record['Case Number'] = table_cells[0].text_content()
            record['Date Filed'] = table_cells[1].text_content()
            #this line adds 1 to the ID no. we set at 0 earlier
            #idno=idno+1
            #record['ID'] = idno 
            record['Caption'] = table_cells[2].text_content()
            record['Found Party'] = table_cells[3].text_content()
            table_cellsurls = table_cells[0].cssselect("a")
            #grab the href=" attribute of the first <a ... and store
            record['URL'] = table_cellsurls[0].attrib.get('href')
                # Print out the data we've gathered
            print record, '------------'
            # Save the record to the datastore - 'ID' is our unique key - 
            scraperwiki.sqlite.save(["Case Number"], record)



br = mechanize.Browser()
#br.set_all_readonly(False)    # allow everything to be written to
br.set_handle_robots(False)   # ignore robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders = [('User-agent', 'Firefox')]   	      	# [('User-agent', 'Firefox')]
br.open("https://cpdocket.cp.cuyahogacounty.us/Search.aspx")
#for f in br.forms():
    #print f
for form in br.forms():
    print "Form name:", form.name
    print form

'''formcount=0
for frm in br.forms():  
    if frm.attrs[class] == "search-form":
        break
        formcount=formcount+1
        br.select_form(nr=formcount)
#br.select_form('form')
        br.form[ 'db' ] = ['garfield',]
#Get the search results
        br.submit()'''

'''#br.select_form(nr=0)
#print br.form
br.form = list(br.forms())[0] 
br['db'] = ['garfield']
br['dcct'] = ['32']
br['lname'] = str('JONES')
#br['mname'] = str(['Middle name'])
#br['fname'] = str(['WILLIAM'])
print br
response = br.submit()
html = response.read()
print html
root = lxml.html.fromstring(html)
scrape_table(root)
'''
