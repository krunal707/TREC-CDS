# Query Generation file for TREC CDS 2014
#It will be generating a query for Indri which can run through IndriRunQuery
mesh_terms_summary = {'Amenorrhea','Animals', 'Dilatation', 'High-Energy Shock Waves', 'Hydatidiform Mole', 'Leiomyoma', 'Moles', 'Pregnancy', 'Pregnancy Tests', 'Ultrasonography', 'Uterine Neoplasms'}  # add terms from the MeSHOnDemand
mesh_rel_terms = {'Amenorrhea':['Postpartum Amenorrhea'], 'Animals':['Metazoa', 'Animalia'], 'Dilatation':['Dilation'], 'High-Energy Shock Waves':[], 'Hydatidiform Mole':['Hydatid Mole', 'Hydatidiform Mole', 'Complete', 'Hydatidiform Mole', 'Partial', 'Molar Pregnancy', 'Pregnancy, Molar'], 'Leiomyoma':['Fibroid', 'Fibroid Tumor', 'Fibroid Uterus', 'Fibroids, Uterine', 'Fibroma, Uterine', 'Fibromyoma', 'Leiomyoma, Uterine'], 'Mole':[] , 'Pregnancy':[] , 'Pregnancy Test':[], 'Ultrasonography':['Computer Echotomography', 'Diagnosis, Ultrasonic', 'Computer. Sonography, Medical', 'Ultrasonic Tomography'], 'Uterine Neoplasms':['Cancer of Uterus', 'Neoplasms, Uterine', 'Uterus Neoplasms']}  # add the entry terms for the terms from mesh_terms_summary
mesh_terms_description = {}
query1 = "#combine("   


def generate_termquery(term):
    if term in ['Humans','Male','Female']:
        return ''
    query = ''
    if "," in term:
        query+= " #uw2("
        new_terms = term.split(',')
        for nt in new_terms:
            query+=generate_termquery(nt)
        query+=")"
    elif " " in term:
        query+= " #1("
        query+=term
        query+=")"
    else:
        query+= " "
        query+=term
    return query
    
for term in mesh_terms_summary:
    if term in mesh_rel_terms.keys():
        rel_terms = mesh_rel_terms[term]
        if not rel_terms:
           query1+=generate_termquery(term)
        else:
            query1 += ' {'
            query1 +=generate_termquery(term)
            for rel_term in rel_terms:
                query1+=generate_termquery(rel_term)
            query1+=" }"
    else:
        query1+= " "
        query1+=term
query1+=" )"
print query1