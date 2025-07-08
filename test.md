````mermaid
---
config:
  theme: neutral
  look: neo
  layout: dagre
---
flowchart LR
 subgraph subGraph0["<b>CEGA Model</b>"]
    direction TB
        SAMPLE@{ label: "<span style=\"--tw-scale-x:\"><b>case2_father</b><br></span>(<i style=\"--tw-scale-x:\">EGAN00003364608</i>)" }
        EXPERIMENT@{ label: "<b>Experiment </b><br>(<span style=\"background-color:\"><i>EGAX00002583878</i></span>)" }
        RUN@{ label: "<span id=\"docs-internal-guid-ea14d459-7fff-9dcb-740a-884694fbca24\"><span style=\"font-size:\"><b>Run</b><br>(<i>EGAR00003021169</i>)</span></span>" }
        ANALYSIS@{ label: "<b>Analysis<br></b>(<span style=\"background-color:\"><i>EGAZ00001743989</i>)</span>" }
        n1@{ label: "<span id=\"docs-internal-guid-0b3e6dab-7fff-d37f-2424-d6e086a28925\"><p dir=\"ltr\" style=\"line-height:\"><span style=\"font-size:\"><b>FASTQ</b></span><span style=\"font-size:\"><br></span><span style=\"font-size:\">…</span><span style=\"font-size:\"><i>case2_case2_father_Case2_F.R1.fastq.gz</i></span></p></span>" }
        n2@{ label: "<span id=\"docs-internal-guid-0b3e6dab-7fff-d37f-2424-d6e086a28925\"><p dir=\"ltr\" style=\"line-height:\"><span style=\"font-size:\"><b>FASTQ</b></span><span style=\"font-size:\"><br></span><span style=\"font-size:\">…</span><span style=\"font-size:\"><i>case2_case2_father_Case2_F.R2.fastq.gz</i></span></p></span>" }
        n3@{ label: "<span id=\"docs-internal-guid-2f637a91-7fff-13ce-bd05-29006547af08\"><p dir=\"ltr\" style=\"line-height:\"><span style=\"font-size:\"><b>BAM</b></span><span style=\"font-size:\"><br></span><i><span style=\"font-size:\">…</span><span style=\"font-size:\">case2_case2_father_Case2_F.bam</span></i></p></span>" }
        n4@{ label: "<span id=\"docs-internal-guid-de137c36-7fff-d5b1-e230-7858938ba490\"><p dir=\"ltr\" style=\"line-height:\"><span style=\"font-size:\"><b>BAI</b></span><span style=\"font-size:\"><br></span><i><span style=\"font-size:\">…</span><span style=\"font-size:\">case2_case2_father_Case2_F.bam.bai</span></i></p></span>" }
  end
 subgraph PC1["<b>protocolCollection</b>"]
        SEQ_PROTOCOL["<b>Library preparation</b>"]
        n5@{ label: "<span style=\"--tw-scale-x:\"><b>Sequencing protocol</b></span>" }
  end
 subgraph PC2["<b>protocolCollection</b>"]
        ALIGN_PROTOCOL["<b>Quality control<br>protocol</b>"]
        n6["<b>Alignment protocol</b>"]
  end
 subgraph subGraph1["<b>FEGA Model</b>"]
    direction TB
        BIOMATERIAL@{ label: "<span id=\"docs-internal-guid-84ef360c-7fff-ac07-a967-8e0e2d2cd0a6\"><p dir=\"ltr\" style=\"line-height:\"><span style=\"font-size:\"><b>case2_father </b>(<i>EGAN00003364608</i>)</span></p></span>" }
        PC1
        SEQ_PROC["<b>Process</b>"]
        RAW1@{ label: "<span id=\"docs-internal-guid-0b3e6dab-7fff-d37f-2424-d6e086a28925\"><p dir=\"ltr\" style=\"line-height:\"><span style=\"font-size:\"><b>FASTQ</b></span><span style=\"font-size:\"><br></span><span style=\"font-size:\">…</span><span style=\"font-size:\"><i>case2_case2_father_Case2_F.R1.fastq.gz</i></span></p></span>" }
        RAW2@{ label: "<span id=\"docs-internal-guid-7c3da251-7fff-4b43-c949-00faa3d41998\"><p dir=\"ltr\" style=\"line-height:\"><span style=\"font-size:\"><b>FASTQ</b></span><span style=\"font-size:\"><br></span><i><span style=\"font-size:\">…</span><span style=\"font-size:\">case2_case2_father_Case2_F.R2.fastq.gz</span></i></p></span>" }
        PC2
        ALIGN_PROC["<b>Process</b>"]
        ALN1@{ label: "<span id=\"docs-internal-guid-2f637a91-7fff-13ce-bd05-29006547af08\"><p dir=\"ltr\" style=\"line-height:\"><span style=\"font-size:\"><b>BAM</b></span><span style=\"font-size:\"><br></span><i><span style=\"font-size:\">…</span><span style=\"font-size:\">case2_case2_father_Case2_F.bam</span></i></p></span>" }
        ALN2@{ label: "<span id=\"docs-internal-guid-de137c36-7fff-d5b1-e230-7858938ba490\"><p dir=\"ltr\" style=\"line-height:\"><span style=\"font-size:\"><b>BAI</b></span><span style=\"font-size:\"><br></span><i><span style=\"font-size:\">…</span><span style=\"font-size:\">case2_case2_father_Case2_F.bam.bai</span></i></p></span>" }
  end
    SAMPLE --> EXPERIMENT & ANALYSIS
    EXPERIMENT --> RUN
    RUN --> n1 & n2
    BIOMATERIAL BIO_PROC1@==> SEQ_PROC
    PC1 --> SEQ_PROC
    SEQ_PROC L_SEQ_PROC_RAW1_0@==> RAW1 & RAW2
    RAW1 L_RAW1_ALIGN_PROC_0@==> ALIGN_PROC
    RAW2 L_RAW2_ALIGN_PROC_0@==> ALIGN_PROC
    PC2 --> ALIGN_PROC
    ALIGN_PROC PROC_ALN1@==> ALN1 & ALN2
    ANALYSIS --> n3 & n4
    SAMPLE@{ shape: doublecircle}
    EXPERIMENT@{ shape: rect}
    RUN@{ shape: rect}
    ANALYSIS@{ shape: rect}
    n1@{ shape: doc}
    n2@{ shape: doc}
    n3@{ shape: doc}
    n4@{ shape: doc}
    n5@{ shape: rect}
    n6@{ shape: rect}
    BIOMATERIAL@{ shape: dbl-circ}
    RAW1@{ shape: doc}
    RAW2@{ shape: doc}
    ALN1@{ shape: doc}
    ALN2@{ shape: doc}
     SAMPLE:::biomaterial
     EXPERIMENT:::process
     RUN:::process
     ANALYSIS:::process
     n1:::datafile
     n2:::datafile
     n3:::datafile
     n4:::datafile
     SEQ_PROTOCOL:::protocol
     n5:::protocol
     ALIGN_PROTOCOL:::protocol
     n6:::protocol
     BIOMATERIAL:::biomaterial
     SEQ_PROC:::process
     RAW1:::datafile
     RAW2:::datafile
     ALIGN_PROC:::process
     ALN1:::datafile
     ALN2:::datafile
    classDef biomaterial fill:#B3D9FF,stroke:#4C8BF5,stroke-width:1px
    classDef datafile   fill:#D5E8D4,stroke:#6FB96C,stroke-width:1px
    classDef process fill:#FFE5CC, stroke:#F5A45D, stroke-width:2px, stroke-dasharray: 0
    classDef protocol fill:#FFE5CC, stroke:#F5A45D, stroke-width:2px, fill:#feeedf, background-color:#feeedf, stroke-dasharray: 2
    style PC1 fill:#FFE0B2
    style PC2 fill:#FFE0B2
    BIO_PROC1@{ animation: slow } 
    L_SEQ_PROC_RAW1_0@{ animation: slow } 
    L_SEQ_PROC_RAW2_0@{ animation: slow } 
    L_RAW1_ALIGN_PROC_0@{ animation: slow } 
    L_RAW2_ALIGN_PROC_0@{ animation: slow } 
    PROC_ALN1@{ animation: slow } 
    L_ALIGN_PROC_ALN2_0@{ animation: slow }
````
