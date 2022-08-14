#!/usr/local/bin/python3
import jinja2
import cgi
import mysql.connector
# This line tells the template loader where to search for template files
templateLoader = jinja2.FileSystemLoader( searchpath="./templates" )
# This creates your environment and loads a specific template
env = jinja2.Environment(loader=templateLoader)
template = env.get_template('template.html')

form = cgi.FieldStorage()
term_cdna = form.getvalue('search_cdna')
term_prot = form.getvalue('search_prot')
term_lega = form.getvalue('search_lega')
term_rs = form.getvalue('search_rs')
clinical_sig = form.getvalue("significance")
display = form.getvalue("display")


conn = mysql.connector.connect(user='cyuan23', password='password', host='localhost', database='cyuan23')
curs = conn.cursor()

qry = ""
count = 0
results = []
i = 1
if term_cdna != None:
    qry = "SELECT * FROM cftr_variant WHERE variant_cDNA_name LIKE %s ORDER BY alleles_in_CFTR2 DESC, percent_pancreatic_insufficient DESC;"
    curs.execute(qry, ("%" + term_cdna + "%", ))
    
    for (variant_cDNA_name, variant_protein_name, variant_legacy_name, rs_ID, alleles_in_CFTR2, allele_frequency_in_CFTR2, percent_pancreatic_insufficient, variant_clinical_consequence) in curs:
        results.append([str(i), variant_cDNA_name, variant_protein_name, variant_legacy_name, rs_ID, alleles_in_CFTR2, allele_frequency_in_CFTR2, percent_pancreatic_insufficient, variant_clinical_consequence])
        count += 1
        i += 1

elif term_prot != None:
    qry = "SELECT * FROM cftr_variant WHERE variant_protein_name LIKE %s ORDER BY alleles_in_CFTR2 DESC, percent_pancreatic_insufficient DESC;"
    curs.execute(qry, ("%" + term_prot + "%", ))
    
    for (variant_cDNA_name, variant_protein_name, variant_legacy_name, rs_ID, alleles_in_CFTR2, allele_frequency_in_CFTR2, percent_pancreatic_insufficient, variant_clinical_consequence) in curs:
        results.append([str(i), variant_cDNA_name, variant_protein_name, variant_legacy_name, rs_ID, alleles_in_CFTR2, allele_frequency_in_CFTR2, percent_pancreatic_insufficient, variant_clinical_consequence])
        count += 1
        i += 1

elif term_lega != None:
    qry = "SELECT * FROM cftr_variant WHERE variant_legacy_name LIKE %s ORDER BY alleles_in_CFTR2 DESC, percent_pancreatic_insufficient DESC;"
    curs.execute(qry, ("%" + term_lega + "%", ))
    
    for (variant_cDNA_name, variant_protein_name, variant_legacy_name, rs_ID, alleles_in_CFTR2, allele_frequency_in_CFTR2, percent_pancreatic_insufficient, variant_clinical_consequence) in curs:
        results.append([str(i), variant_cDNA_name, variant_protein_name, variant_legacy_name, rs_ID, alleles_in_CFTR2, allele_frequency_in_CFTR2, percent_pancreatic_insufficient, variant_clinical_consequence])
        count += 1
        i += 1

elif term_rs != None:
    qry = "SELECT * FROM cftr_variant WHERE rs_ID LIKE %s ORDER BY alleles_in_CFTR2 DESC, percent_pancreatic_insufficient DESC;"
    curs.execute(qry, ("%" + term_rs + "%", ))
    
    for (variant_cDNA_name, variant_protein_name, variant_legacy_name, rs_ID, alleles_in_CFTR2, allele_frequency_in_CFTR2, percent_pancreatic_insufficient, variant_clinical_consequence) in curs:
        results.append([str(i), variant_cDNA_name, variant_protein_name, variant_legacy_name, rs_ID, alleles_in_CFTR2, allele_frequency_in_CFTR2, percent_pancreatic_insufficient, variant_clinical_consequence])
        count += 1
        i += 1

else:
    if clinical_sig == "cf":
        qry = "SELECT * FROM cftr_variant WHERE variant_clinical_consequence = 'CF-causing' ORDER BY alleles_in_CFTR2 DESC, percent_pancreatic_insufficient DESC;"
        curs.execute(qry)

        for (variant_cDNA_name, variant_protein_name, variant_legacy_name, rs_ID, alleles_in_CFTR2, allele_frequency_in_CFTR2, percent_pancreatic_insufficient, variant_clinical_consequence) in curs:
            results.append([str(i), variant_cDNA_name, variant_protein_name, variant_legacy_name, rs_ID, alleles_in_CFTR2, allele_frequency_in_CFTR2, percent_pancreatic_insufficient, variant_clinical_consequence])
            count += 1
            i += 1

    elif clinical_sig == "non_cf":
        qry = "SELECT * FROM cftr_variant WHERE variant_clinical_consequence = 'Non CF-causing' ORDER BY alleles_in_CFTR2 DESC, percent_pancreatic_insufficient DESC;"
        curs.execute(qry)

        for (variant_cDNA_name, variant_protein_name, variant_legacy_name, rs_ID, alleles_in_CFTR2, allele_frequency_in_CFTR2, percent_pancreatic_insufficient, variant_clinical_consequence) in curs:
            results.append([str(i), variant_cDNA_name, variant_protein_name, variant_legacy_name, rs_ID, alleles_in_CFTR2, allele_frequency_in_CFTR2, percent_pancreatic_insufficient, variant_clinical_consequence])
            count += 1
            i += 1

    elif clinical_sig == "varying":
        qry = "SELECT * FROM cftr_variant WHERE variant_clinical_consequence = 'Varying clinical consequence' ORDER BY alleles_in_CFTR2 DESC, percent_pancreatic_insufficient DESC;"
        curs.execute(qry)

        for (variant_cDNA_name, variant_protein_name, variant_legacy_name, rs_ID, alleles_in_CFTR2, allele_frequency_in_CFTR2, percent_pancreatic_insufficient, variant_clinical_consequence) in curs:
            results.append([str(i), variant_cDNA_name, variant_protein_name, variant_legacy_name, rs_ID, alleles_in_CFTR2, allele_frequency_in_CFTR2, percent_pancreatic_insufficient, variant_clinical_consequence])
            count += 1
            i += 1

    elif clinical_sig == "unknown":
        qry = "SELECT * FROM cftr_variant WHERE variant_clinical_consequence = 'Unknown significance' ORDER BY alleles_in_CFTR2 DESC, percent_pancreatic_insufficient DESC;"
        curs.execute(qry)

        for (variant_cDNA_name, variant_protein_name, variant_legacy_name, rs_ID, alleles_in_CFTR2, allele_frequency_in_CFTR2, percent_pancreatic_insufficient, variant_clinical_consequence) in curs:
            results.append([str(i), variant_cDNA_name, variant_protein_name, variant_legacy_name, rs_ID, alleles_in_CFTR2, allele_frequency_in_CFTR2, percent_pancreatic_insufficient, variant_clinical_consequence])
            count += 1
            i += 1
    elif clinical_sig == "any":
        qry = "SELECT * FROM cftr_variant ORDER BY alleles_in_CFTR2 DESC, percent_pancreatic_insufficient DESC;"
        curs.execute(qry)

        for (variant_cDNA_name, variant_protein_name, variant_legacy_name, rs_ID, alleles_in_CFTR2, allele_frequency_in_CFTR2, percent_pancreatic_insufficient, variant_clinical_consequence) in curs:
            results.append([str(i), variant_cDNA_name, variant_protein_name, variant_legacy_name, rs_ID, alleles_in_CFTR2, allele_frequency_in_CFTR2, percent_pancreatic_insufficient, variant_clinical_consequence])
            count += 1
            i += 1

if display == "ten":
    results = results[:10]

curs.close()
conn.close()

print("Content-Type: text/html\n\n")
print(template.render(count=count, res_list = results))
