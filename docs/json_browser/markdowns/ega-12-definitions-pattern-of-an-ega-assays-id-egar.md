# Pattern of an EGA assay's ID (EGAR...) Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/EGA-assay-id-pattern
```



| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## EGA-assay-id-pattern Type

`string` ([Pattern of an EGA assay's ID (EGAR...)](ega-12-definitions-pattern-of-an-ega-assays-id-egar.md))

## EGA-assay-id-pattern Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^EGAR[0-9]{11}$
```

[try pattern](https://regexr.com/?expression=%5EEGAR%5B0-9%5D%7B11%7D%24 "try regular expression with regexr.com")

## EGA-assay-id-pattern Examples

```json
"EGAR00001314547"
```
