# Sequence quality details Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/sequence_quality_details
```

Sequencing quality scores measure the probability that a base is called (i.e. sequenced) incorrectly. New sequencing technologies assign a quality score to each of the bases in the sequence.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## sequence\_quality\_details Type

`object` ([Sequence quality details](ega-12-definitions-ega-file-object-properties-sequence-quality-details.md))

# sequence\_quality\_details Properties

| Property                                            | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                  |
| :-------------------------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [quality\_scoring\_system](#quality_scoring_system) | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-sequence-quality-details-properties-quality-scoring-system.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/sequence_quality_details/properties/quality_scoring_system") |
| [quality\_encoding](#quality_encoding)              | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-sequence-quality-details-properties-quality-encoding-format.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/sequence_quality_details/properties/quality_encoding")      |
| [ascii\_offset](#ascii_offset)                      | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-sequence-quality-details-properties-ascii-offset.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/sequence_quality_details/properties/ascii_offset")                     |

## quality\_scoring\_system

How the quality score was computed for the data.

`quality_scoring_system`

* is required

* Type: `string` ([Quality scoring system](ega-12-definitions-ega-file-object-properties-sequence-quality-details-properties-quality-scoring-system.md))

* cannot be null

* defined in: [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-sequence-quality-details-properties-quality-scoring-system.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/sequence_quality_details/properties/quality_scoring_system")

### quality\_scoring\_system Type

`string` ([Quality scoring system](ega-12-definitions-ega-file-object-properties-sequence-quality-details-properties-quality-scoring-system.md))

### quality\_scoring\_system Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value        | Explanation |
| :----------- | :---------- |
| `"phred"`    |             |
| `"log-odds"` |             |

## quality\_encoding

Encoding system used to represent the quality score.

`quality_encoding`

* is optional

* Type: `string` ([Quality encoding format](ega-12-definitions-ega-file-object-properties-sequence-quality-details-properties-quality-encoding-format.md))

* cannot be null

* defined in: [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-sequence-quality-details-properties-quality-encoding-format.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/sequence_quality_details/properties/quality_encoding")

### quality\_encoding Type

`string` ([Quality encoding format](ega-12-definitions-ega-file-object-properties-sequence-quality-details-properties-quality-encoding-format.md))

### quality\_encoding Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value           | Explanation |
| :-------------- | :---------- |
| `"ascii"`       |             |
| `"decimal"`     |             |
| `"hexadecimal"` |             |

## ascii\_offset

Character used in representing the minimum quality value.  Helps specify how to decode text rendering of quality data.

`ascii_offset`

* is optional

* Type: `string` ([ASCII offset](ega-12-definitions-ega-file-object-properties-sequence-quality-details-properties-ascii-offset.md))

* cannot be null

* defined in: [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-sequence-quality-details-properties-ascii-offset.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/sequence_quality_details/properties/ascii_offset")

### ascii\_offset Type

`string` ([ASCII offset](ega-12-definitions-ega-file-object-properties-sequence-quality-details-properties-ascii-offset.md))

### ascii\_offset Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value | Explanation |
| :---- | :---------- |
| `"!"` |             |
| `"@"` |             |
