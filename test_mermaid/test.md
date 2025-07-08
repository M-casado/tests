````mermaid
---
config:
  theme: neutral
  look: neo
  layout: dagre
---
flowchart TB
 subgraph subGraph0["<b>CEGA Model</b>"]
    direction TB
        SAMPLE((("Sample")))
        EXPERIMENT["Experiment"]
        RUN["Run"]
        ANALYSIS["Analysis"]
        DF_C1["Datafile"]
        DF_C2["Datafile"]
        DF_C3["Datafile"]
        DF_C4["Datafile"]
  end
 subgraph subGraph1["<b>FEGA Model</b>"]
    direction TB
        BIOMATERIAL["Biomaterial"]
        SEQ_PROTOCOL["Sequencing protocol"]
        SEQ_PROC["Sequencing process"]
        RAW1["Datafile"]
        RAW2["Datafile"]
        ALIGN_PROTOCOL["Alignment protocol"]
        ALIGN_PROC["Alignment process"]
        ALN1["Datafile"]
        ALN2["Datafile"]
  end
    SAMPLE --> EXPERIMENT & ANALYSIS
    EXPERIMENT --> RUN
    RUN --> DF_C1 & DF_C2
    ANALYSIS --> DF_C3 & DF_C4
    BIOMATERIAL --> SEQ_PROC
    SEQ_PROTOCOL --> SEQ_PROC
    SEQ_PROC L_SEQ_PROC_RAW1_0@==> RAW1
    SEQ_PROC --> RAW2
    RAW1 --> ALIGN_PROC
    RAW2 --> ALIGN_PROC
    ALIGN_PROTOCOL --> ALIGN_PROC
    ALIGN_PROC --> ALN1 & ALN2
    DF_C1@{ shape: doc}
    DF_C2@{ shape: doc}
    DF_C3@{ shape: doc}
    DF_C4@{ shape: doc}
    BIOMATERIAL@{ shape: dbl-circ}
    RAW1@{ shape: doc}
    RAW2@{ shape: doc}
    ALN1@{ shape: doc}
    ALN2@{ shape: doc}
     SAMPLE:::biomaterial
     EXPERIMENT:::process
     RUN:::process
     ANALYSIS:::process
     DF_C1:::datafile
     DF_C2:::datafile
     DF_C3:::datafile
     DF_C4:::datafile
     BIOMATERIAL:::biomaterial
     SEQ_PROTOCOL:::protocol
     SEQ_PROC:::process
     RAW1:::datafile
     RAW2:::datafile
     ALIGN_PROTOCOL:::protocol
     ALIGN_PROC:::process
     ALN1:::datafile
     ALN2:::datafile
    classDef biomaterial fill:#B3D9FF,stroke:#4C8BF5,stroke-width:1px
    classDef process    fill:#FFE5CC,stroke:#F5A45D,stroke-width:1px
    classDef datafile   fill:#D5E8D4,stroke:#6FB96C,stroke-width:1px
    classDef protocol fill:#FFE5CC, stroke:#F5A45D, stroke-width:1px, fill:#feeedf, background-color:#feeedf, stroke-dasharray: 1
    L_SEQ_PROC_RAW1_0@{ animation: fast }
````
