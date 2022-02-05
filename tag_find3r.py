import requests 
import BeautifulSoup as  BS
import optparse

f="target.html"

###########
# NEXT STEP : REFACTORING CODE AND COMMENT IT :)
# Manage The Caractere Like &\##
###########

# Obtenir les options de l'utilisateur 
def get_args():
    parser=optparse.OptionParser()
    parser.add_option("-u","--url",dest="url",help="Set the target")
    return parser.parse_args()

      
# Ecriture de la description dans un fichier
def writer(data):
    with open("keywords.txt","a") as r:
         r.write(data+"\n")
     
                          
# Obtenir le code HTML
def get_code(url):
    return requests.get(url).content

def goodkey(list):
    return list.split(",")
    
# Recherche de la description dans le code HTML puis ecriture dans un fichier 
def bs_search(payload,string):
    bs=BS.BeautifulSoup(string)
    dt=bs.findAll(payload)
    for d in dt:
        name=d.get("name")
        ctn=d.get("content")
        if name=="keywords":
            key_list=goodkey(ctn)
            for key in key_list:
                writer(key)                
            print("\n[+] Stealing Tag Successfull ")
            
# Lancement du Steal T4g          
def start_descr(url):
    data=get_code(url)
    bs_search("meta",data)
    

(option,argument)=get_args()
start_descr(option.url)