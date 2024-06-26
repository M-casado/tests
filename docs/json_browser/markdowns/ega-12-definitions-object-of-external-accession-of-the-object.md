# Object of external accession of the object Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_external_accession
```

External accession node containing the object accession (i.e. unique identifier -  each following their respective formats) assigned by other archives (e.g. biosample, ena, ensembl...) and an optional label to add context to the reference.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## object\_external\_accession Type

`object` ([Object of external accession of the object](ega-12-definitions-object-of-external-accession-of-the-object.md))

# object\_external\_accession Properties

| Property                                                | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                              |
| :------------------------------------------------------ | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [external\_accession\_curie](#external_accession_curie) | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-object-of-external-accession-of-the-object-properties-curie-of-the-external-accession.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_external_accession/properties/external_accession_curie") |
| [accession\_label](#accession_label)                    | Multiple | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-object-of-external-accession-of-the-object-properties-label-of-the-external-accession.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_external_accession/properties/accession_label")          |

## external\_accession\_curie

Unique identifier of an external, to EGA, object. It shall follow CURIE format (`prefix`:`accession`): prefix assigned to the archive (e.g. biosample - search for yours at identifiers.org) and the unique accession of the object (e.g. SAMEA7616999).

`external_accession_curie`

* is required

* Type: `string` ([CURIE of the external accession](ega-12-definitions-object-of-external-accession-of-the-object-properties-curie-of-the-external-accession.md))

* cannot be null

* defined in: [EGA common metadata definitions](ega-12-definitions-object-of-external-accession-of-the-object-properties-curie-of-the-external-accession.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_external_accession/properties/external_accession_curie")

### external\_accession\_curie Type

`string` ([CURIE of the external accession](ega-12-definitions-object-of-external-accession-of-the-object-properties-curie-of-the-external-accession.md))

all of

* [Compact URI (CURIE) pattern](ega-12-definitions-object-of-external-accession-of-the-object-properties-curie-of-the-external-accession-allof-compact-uri-curie-pattern.md "check type definition")

### external\_accession\_curie Examples

```json
"biosample:SAMEA7616999"
```

```json
"arrayexpress:E-MEXP-1712"
```

## accession\_label

Optional label (e.g. 'taken from biosample temporarily') of the external accession, used to add extra information to the identifier.

`accession_label`

* is optional

* Type: any of the following: `string` or `number` ([Label of the external accession](ega-12-definitions-object-of-external-accession-of-the-object-properties-label-of-the-external-accession.md))

* cannot be null

* defined in: [EGA common metadata definitions](ega-12-definitions-object-of-external-accession-of-the-object-properties-label-of-the-external-accession.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_external_accession/properties/accession_label")

### accession\_label Type

any of the following: `string` or `number` ([Label of the external accession](ega-12-definitions-object-of-external-accession-of-the-object-properties-label-of-the-external-accession.md))

### accession\_label Examples

```json
"taken from biosample temporarily"
```

```json
"Ensembl's part of the accessions"
```

```json
"first"
```

```json
2
```
