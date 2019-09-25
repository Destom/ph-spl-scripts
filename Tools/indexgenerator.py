print ("hello world")

for i in range(1,151):
    print(f'''[Nmber_test_{i}]
coldPath = $SPLUNK_DB/number_test_{i}/colddb
enableDataIntegrityControl = 0
enableTsidxReduction = 0
homePath = $SPLUNK_DB/number_test_{i}/db
maxTotalDataSizeMB = 512000
thawedPath = $SPLUNK_DB/number_test_{i}/thaweddb
''')
