# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import cx_Oracle
import time
import job_dictionnary

class jobPipeline(object):
    
    def __init__(self):
        #Initializes database connection 

        

        
        try:
            self.con = cx_Oracle.connect(job_dictionnary.server_id['username'], job_dictionnary.server_id['password'], cx_Oracle.makedsn('localhost', 1521, 'xe'))
        except :
            print("Connection to the database failed")
        self.con.autocommit = True
        self.cur = self.con.cursor()
        self.cur.bindarraysize = 1
        self.cur.setinputsizes(100, 50,100,200,100,10,100)

    def process_item(self, item, spider):
        
        cur = self.cur
        
        #populating list to get acces to items
        output = []
        output.append(item['titre'])
        output.append(item['site_provenance'])
        output.append(item['lien'])
        output.append(item['texte'])
        output.append(item['nom_compagnie'])
        output.append(item['date_dernier_poste'])
        
        output_company = []
        output_company.append(item['nom_compagnie'])
        output_company.append(item['position'])
        output_company.append(item['titre'])
        output_company.append(item['date_dernier_poste'])
        output_company.append(item['date_dernier_poste'])
        #try to insert new annonce if fail update existing annonce and also 
        #update the stat for the website
        try:
            cur.execute('insert into Annonce values (:1,:2,:3,:4,:5,:6)', output)
            
        except cx_Oracle.DatabaseError as exc:
            error, = exc.args
            time_local = output[5]
            titre = output[0]
            link = output[2]
            if error.code == 1:
                
                cur.execute('UPDATE Annonce SET date_dernier_poste = :x WHERE title = :y and lien = :z ', {'x':time_local,'y':titre,'z':link})
                cur.callproc('update_stat',('Stat_jobboom',2))
            else:
                cur.callproc('update_stat',('Stat_jobboom',3))
                print("Oracle-Error-Message:", error.message)
                print('Annonce : ',titre,' got rejected')
        #try to insert a company in the compagnie table if it already exist update the liste_poste
        try:
            cur.execute('insert into Compagnie values (:1,:2,:3,:4,:5)', output_company)
            #commit
        except cx_Oracle.DatabaseError as exc:
            error, = exc.args
            nom_company = output_company[0]
            position = item['position']
            time_local = output[5]
            annonce = output_company[2]
            if error.code == 1:
                cur.execute('SELECT poste_liste FROM Compagnie WHERE nom_compagnie = :y and position_compagnie = :z ',{'y':nom_company,'z':position})
                liste_annonnces = cur.fetchone()
                if annonce in liste_annonnces: 
                    cur.execute('UPDATE Compagnie SET date_dernier_poste = :x WHERE nom_compagnie = :y and position_compagnie = :z ', {'x':time_local,'y':nom_company,'z':position})
                else:
                    new_list = ' '.join(liste_annonnces) + ' ; ' + annonce
                    cur.execute('UPDATE Compagnie SET date_dernier_poste = :x,poste_liste = :a WHERE nom_compagnie = :y and position_compagnie = :z ', {'x':time_local,'a':new_list,'y':nom_company,'z':position})
            else:
                
                
                print("Oracle-Error-Message:", error.message)

        return item
    def close_spider(self, spider):
        self.cur.close()
        self.con.close()
