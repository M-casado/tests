# Asserting sequencer technology controlled vocabulary (CV) Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/assay_technology_descriptor/oneOf/1
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## 1 Type

unknown ([Asserting sequencer technology controlled vocabulary (CV)](ega-12-definitions-assay-technology-oneof-asserting-sequencer-technology-controlled-vocabulary-cv.md))

# 1 Properties

| Property                                                  | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| :-------------------------------------------------------- | :------------ | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [assay\_instrument](#assay_instrument)                    | Not specified | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-assay-technology-oneof-asserting-sequencer-technology-controlled-vocabulary-cv-properties-assay_instrument.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/assay_technology_descriptor/oneOf/1/properties/assay_instrument")                                                                                                        |
| [assay\_instrument\_platform](#assay_instrument_platform) | `string`      | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-assay-technology-oneof-asserting-sequencer-technology-controlled-vocabulary-cv-properties-ega-controlled-vocabulary-cv-for-sequencing-instrument-platforms.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/controlled_vocabulary_schemas/EGA.cv.instrument_platforms_sequencing.json#/definitions/assay_technology_descriptor/oneOf/1/properties/assay_instrument_platform") |

## assay\_instrument



`assay_instrument`

* is optional

* Type: unknown

* cannot be null

* defined in: [EGA common metadata definitions](ega-12-definitions-assay-technology-oneof-asserting-sequencer-technology-controlled-vocabulary-cv-properties-assay_instrument.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/assay_technology_descriptor/oneOf/1/properties/assay_instrument")

### assay\_instrument Type

unknown

### assay\_instrument Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value         | Explanation |
| :------------ | :---------- |
| `"sequencer"` |             |

## assay\_instrument\_platform

Controlled Vocabulary (CV) list for the sequencing instrument platforms. Commonly consisting in the manufacturers name (e.g. Illumina) and the instrument model (e.g. HiSeq 2000). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema) proposing its addition.

`assay_instrument_platform`

* is optional

* Type: `string` ([EGA Controlled Vocabulary (CV) for sequencing instrument platforms](ega-12-definitions-assay-technology-oneof-asserting-sequencer-technology-controlled-vocabulary-cv-properties-ega-controlled-vocabulary-cv-for-sequencing-instrument-platforms.md))

* cannot be null

* defined in: [EGA common metadata definitions](ega-12-definitions-assay-technology-oneof-asserting-sequencer-technology-controlled-vocabulary-cv-properties-ega-controlled-vocabulary-cv-for-sequencing-instrument-platforms.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/controlled_vocabulary_schemas/EGA.cv.instrument_platforms_sequencing.json#/definitions/assay_technology_descriptor/oneOf/1/properties/assay_instrument_platform")

### assay\_instrument\_platform Type

`string` ([EGA Controlled Vocabulary (CV) for sequencing instrument platforms](ega-12-definitions-assay-technology-oneof-asserting-sequencer-technology-controlled-vocabulary-cv-properties-ega-controlled-vocabulary-cv-for-sequencing-instrument-platforms.md))

### assay\_instrument\_platform Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                                   | Explanation |
| :-------------------------------------- | :---------- |
| `"HiSeq X Five"`                        |             |
| `"HiSeq X Ten"`                         |             |
| `"Illumina Genome Analyzer"`            |             |
| `"Illumina Genome Analyzer II"`         |             |
| `"Illumina Genome Analyzer IIx"`        |             |
| `"Illumina HiScanSQ"`                   |             |
| `"Illumina HiSeq 1000"`                 |             |
| `"Illumina HiSeq 1500"`                 |             |
| `"Illumina HiSeq 2000"`                 |             |
| `"Illumina HiSeq 2500"`                 |             |
| `"Illumina HiSeq 3000"`                 |             |
| `"Illumina HiSeq 4000"`                 |             |
| `"Illumina HiSeq X"`                    |             |
| `"Illumina iSeq 100"`                   |             |
| `"Illumina MiSeq"`                      |             |
| `"Illumina MiniSeq"`                    |             |
| `"Illumina NovaSeq 6000"`               |             |
| `"NextSeq 500"`                         |             |
| `"NextSeq 550"`                         |             |
| `"NextSeq 1000"`                        |             |
| `"NextSeq 2000"`                        |             |
| `"Helicos HeliScope"`                   |             |
| `"AB SOLiD System"`                     |             |
| `"AB SOLiD System 2.0"`                 |             |
| `"AB SOLiD System 3.0"`                 |             |
| `"AB SOLiD 3 Plus System"`              |             |
| `"AB SOLiD 4 System"`                   |             |
| `"AB SOLiD 4hq System"`                 |             |
| `"AB SOLiD PI System"`                  |             |
| `"AB 5500 Genetic Analyzer"`            |             |
| `"AB 5500xl Genetic Analyzer"`          |             |
| `"AB 5500xl-W Genetic Analysis System"` |             |
| `"Complete Genomics"`                   |             |
| `"BGISEQ-50"`                           |             |
| `"BGISEQ-500"`                          |             |
| `"MGISEQ-2000RS"`                       |             |
| `"PacBio RS"`                           |             |
| `"PacBio RS II"`                        |             |
| `"Sequel"`                              |             |
| `"Sequel II"`                           |             |
| `"Ion Torrent PGM"`                     |             |
| `"Ion Torrent Proton"`                  |             |
| `"Ion Torrent S5"`                      |             |
| `"Ion Torrent S5 XL"`                   |             |
| `"Ion Torrent Genexus"`                 |             |
| `"Ion GeneStudio S5"`                   |             |
| `"Ion GeneStudio S5 Prime"`             |             |
| `"Ion GeneStudio S5 Plus"`              |             |
| `"AB 3730xL Genetic Analyzer"`          |             |
| `"AB 3730 Genetic Analyzer"`            |             |
| `"AB 3500xL Genetic Analyzer"`          |             |
| `"AB 3500 Genetic Analyzer"`            |             |
| `"AB 3130xL Genetic Analyzer"`          |             |
| `"AB 3130 Genetic Analyzer"`            |             |
| `"AB 310 Genetic Analyzer"`             |             |
| `"DNBSEQ-T7"`                           |             |
| `"DNBSEQ-G400"`                         |             |
| `"DNBSEQ-G50"`                          |             |
| `"DNBSEQ-G400 FAST"`                    |             |
| `"MinION"`                              |             |
| `"GridION"`                             |             |
| `"PromethION"`                          |             |
