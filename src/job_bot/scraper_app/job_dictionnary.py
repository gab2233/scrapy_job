# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
server_id ={
'username':'PYTHONHOL',
'password':'welcome'
}
jobboom = {
'name':'jobboom',
'url_start':'http://www.jobboom.com/fr/emploi_k-1',
'job_tag':'div.job_item_video',
'job_title':'div.job_item_video::attr(title)',
'job_link_tag':'div.job_item_video::attr(data-url)',
'boss_tag':'p.employeur>span::text',
'next_page_tag':'a.pagination_next::attr(href)'
}

indeed = {
'name':'indeed',
'url_start':'https://emplois.ca.indeed.com/emplois?q=&l=QC',
'job_tag':'td#resultsCol div.row',
'job_title':'a::attr(title)',
'job_link_tag':'a::attr(href)',
'boss_tag':'td#resultsCol  span.company::text',
'next_page_tag':'div.pagination a:last-child::attr(href)'




}
y = {
'name':'',
'url_start':'',
'job_tag':'',
'job_title':'',
'job_link_tag':'',
'boss_tag':'',
'next_page_tag':''




}




