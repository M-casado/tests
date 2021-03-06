# Quality scoring system Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/sequence_quality_details/properties/quality_scoring_system
```

How the quality score was computed for the data.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## quality\_scoring\_system Type

`string` ([Quality scoring system](ega-12-definitions-ega-file-object-properties-sequence-quality-details-properties-quality-scoring-system.md))

## quality\_scoring\_system Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value        | Explanation |
| :----------- | :---------- |
| `"phred"`    |             |
| `"log-odds"` |             |
