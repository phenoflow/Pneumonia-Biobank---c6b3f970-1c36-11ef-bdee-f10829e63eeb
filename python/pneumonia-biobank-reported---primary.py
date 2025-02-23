# Eleftheria Vasileiou, Chukwuma Iwundu, Alex Williams, Clare MacRae, 2024.

import sys, csv, re

codes = [{"code":"131445","system":"ukbiobank"},{"code":"131451","system":"ukbiobank"},{"code":"131455","system":"ukbiobank"},{"code":"131444","system":"ukbiobank"},{"code":"131449","system":"ukbiobank"},{"code":"131447","system":"ukbiobank"},{"code":"131448","system":"ukbiobank"},{"code":"131456","system":"ukbiobank"},{"code":"131457","system":"ukbiobank"},{"code":"131453","system":"ukbiobank"},{"code":"131454","system":"ukbiobank"},{"code":"131452","system":"ukbiobank"},{"code":"131450","system":"ukbiobank"},{"code":"131446","system":"ukbiobank"},{"code":"131454","system":"ukbiobank"},{"code":"131452","system":"ukbiobank"},{"code":"131456","system":"ukbiobank"},{"code":"131451","system":"ukbiobank"},{"code":"131447","system":"ukbiobank"},{"code":"131453","system":"ukbiobank"},{"code":"131457","system":"ukbiobank"},{"code":"131455","system":"ukbiobank"},{"code":"131449","system":"ukbiobank"},{"code":"131445","system":"ukbiobank"},{"code":"131446","system":"ukbiobank"},{"code":"131444","system":"ukbiobank"},{"code":"131448","system":"ukbiobank"},{"code":"131450","system":"ukbiobank"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('pneumonia-biobank-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["pneumonia-biobank-reported---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["pneumonia-biobank-reported---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["pneumonia-biobank-reported---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
