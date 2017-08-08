# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from scrapy.item import Item, Field


class job_item (Item):    
    titre = Field()
    site_provenance = Field()
    lien = Field()
    texte = Field()
    nom_compagnie = Field()
    date_dernier_poste = Field()
    position = Field()

class company_item(Item):
    nom_compagnie = Field()
    position_compagnie = Field()
    poste_liste = Field()
    date_dernier_poste = Field()
    date_premier_poste = Field()
    