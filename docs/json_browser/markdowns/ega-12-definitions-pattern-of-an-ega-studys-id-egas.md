# Pattern of an EGA study's ID (EGAS...) Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.study.json#/properties/object_id/allOf/1/properties/ega_accession
```



| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                 |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.study.json\*](../../../schemas/EGA.study.json "open original schema") |

## ega\_accession Type

`string` ([Pattern of an EGA study's ID (EGAS...)](ega-12-definitions-pattern-of-an-ega-studys-id-egas.md))

## ega\_accession Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^EGAS[0-9]{11}$
```

[try pattern](https://regexr.com/?expression=%5EEGAS%5B0-9%5D%7B11%7D%24 "try regular expression with regexr.com")

## ega\_accession Examples

```json
"EGAS00001004508"
```
