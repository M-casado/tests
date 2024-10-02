# Pattern of an EGA submission's ID (EGAB...) Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/EGA-submission-id-pattern
```



| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## EGA-submission-id-pattern Type

`string` ([Pattern of an EGA submission's ID (EGAB...)](ega-12-definitions-pattern-of-an-ega-submissions-id-egab.md))

## EGA-submission-id-pattern Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^EGAB[0-9]{11}$
```

[try pattern](https://regexr.com/?expression=%5EEGAB%5B0-9%5D%7B11%7D%24 "try regular expression with regexr.com")

## EGA-submission-id-pattern Examples

```json
"EGAB00001001831"
```
