# Inception Document
---
## 1. Team Members and Distribution
ID	Name	Role
2023532043	刘慕	Knowledge Engineer
2023532074	王硕 Domain Expert
2023534045	马世旋	Data Scientist


## 2. Context

### 2.1. Domain of Interest
The Knowledge and Data Integration (KDI) project provides users with disease-centric medical dietary solutions in the medical field. We take into account the characteristics of various diseases, their interrelationships, treatment options, food information and user information. Establish a certain scale of medical diet knowledge map with diseases as the center, and use the knowledge map to complete automatic search and analysis services. This relatively complete knowledge map can greatly help patients with related diseases who are not familiar with dietary precautions and recommended diets, their families and doctors and nurses to speed up the search for appropriate recipes and efficiency.

### 2.2. Personas
In this project, the knowledge graph is used regardless of the user group (age, gender, occupation). They can be old people, children, middle-aged people or office workers or students.

### 2.3. Scenarios
In the program, users can search for foods to eat, recommend recipes and avoid foods based on their single or multiple medical conditions.
For example, a patient with thoracic vertebral fracture was judged to belong to the fracture department by knowledge map, and calcium was suggested to be added. The related food field was searched by domain knowledge, and snakehead fish was recommended.

## 3. Purpose
### 3.1. Raw Competency Questions

The patient is looking up the recommended diet and foods for his condition.
+ CQ1: What recipe does fracture patient recommend?
+ CQ2:What should old asthma patient notice on diet?

### 3.2. Kernel Competency Questions

+ CQ1: Adult, Fracture patient, Recipe
+ CQ2:Old, Asthma patient, Notice,Diet

### 3.3. Analysed Competency Questions

+ CQ1

  **common:** Person, Disease Diagnosis,Recipe
  **core:**Fracture, Illness
  **contextual:** Adult

+ CQ2

  **common:** Person, Disease Diagnosis, Diet
  **core:** Asthma,Notice
  **contextual:** Elderly People

## 4. Resource Classification (*with Availability*)

### 4.1. Knowledge Resources
http://www.openkg.cn/

### 4.2. Data Resources
https://www.fancai.com/
http://jib.xywy.com/

## 5. Additional Remarks

Our KDI project is actually divided into three phases. In the first stage, information extraction is carried out to extract entities, attributes and relationships between entities from medical data sources and food data sources, and on this basis, ontology knowledge expression is formed. The second stage is knowledge integration. After new knowledge is acquired from the first stage, it needs to be integrated to eliminate contradictions and ambiguities. For example, some diseases may have multiple expressions. The third part is knowledge processing. For the new knowledge that has been fused, the qualified part shall be added to the knowledge base after quality assessment (part shall be screened manually, referring to the network information) to ensure the quality of the knowledge base. After the new data is added, knowledge reasoning is carried out to expand existing knowledge and obtain new knowledge.
Through three stages, the question and answer system of disease-centered medical diet solution knowledge graph was constructed.

