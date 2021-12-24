# Commands to test

### Smaller < Larger
````
for doc in $(ls larger_smaller/DOC*); do ajv --strict=false --spec=draft2019 --data -s larger_smaller/SCHEMA.larger_smaller.json  -d $doc; done
````

### MD5s being equal
````
for doc in $(ls MD5s_being_equal/DOC*); do ajv --strict=false --spec=draft2019 --data -s MD5s_being_equal/SCHEMA.MD5s_being_equal.json -d $doc; done
````

### MD5s being different
````
for doc in $(ls MD5s_being_different/DOC*); do ajv --strict=false --spec=draft2019 --data -s MD5s_being_different/SCHEMA.MD5s_being_different.json -d $doc; done
````