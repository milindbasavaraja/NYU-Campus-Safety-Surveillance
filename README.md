# NYU Campus Safety Surveillance
 
**NYU Campus Safety Surveillance**, a system that will ideally have access to video feeds of all CCTV cameras in and around the
campus. Whenever a weapon or unauthorized personnel is found inside the campus premises, the system will send out appropriate 
action emails to concerned campus security personnel.

### Proposed Architecture
This architecture relies heavily on **AWS Kinesis Video and Data streams**. As of November 2021, this product has an on-demand 
auto-scaling feature as well which can take any amount of data, from any number of sources, and scale up and down as needed.

![](https://github.com/milindbasavaraja/NYU-Campus-Safety-Surveillance/blob/main/assets/CurrentArchitecture.png)
