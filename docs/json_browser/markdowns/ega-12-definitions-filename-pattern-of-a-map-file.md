# Filename pattern of a MAP file Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/map-file-filename-pattern
```

This object exists to hold the filename pattern that a 'MAP' filetype\_id would have, for it to be referenced elsewhere within this (or other) JSON schema.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## map-file-filename-pattern Type

`string` ([Filename pattern of a MAP file](ega-12-definitions-filename-pattern-of-a-map-file.md))

## map-file-filename-pattern Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^.+\.map(\.(gz|zip|rar|arj|tar|7z|bz2))?(\.gpg)?$
```

[try pattern](https://regexr.com/?expression=%5E.%2B%5C.map\(%5C.\(gz%7Czip%7Crar%7Carj%7Ctar%7C7z%7Cbz2\)\)%3F\(%5C.gpg\)%3F%24 "try regular expression with regexr.com")

## map-file-filename-pattern Examples

```json
"my_file1.map.gpg"
```
