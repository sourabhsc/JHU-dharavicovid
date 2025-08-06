# COVID-19 Transmission Mitigation in Dense Settlements

> **Johns Hopkins CBID COVID-19 Design Challenge **  
> *A collaborative solution developed by NISER students: **Preeti**, **Tharun**, Monali, Yoshita, and **Prajakta** under Team 94*

[![LinkedIn Post](https://img.shields.io/badge/LinkedIn-Team%20Update-blue?logo=linkedin)](https://www.linkedin.com/posts/sourabh-singh-chauhan_had-a-great-time-participating-in-johns-hopkins-activity-6651265888127451136-Wdhb?utm_source=share&utm_medium=member_desktop&rcm=ACoAACgpL94BCkz83qc56N9JkclZRU7_URJRNN4)

## 🚨 Problem Overview

COVID-19 transmission poses a critical challenge in densely populated settlements where traditional social distancing is not viable. This project addresses the urgent need for alternative solutions in informal settlements where:

- **~1 billion people** worldwide live in conditions where social distancing is impossible
- Crowded living conditions and economic constraints prevent traditional mitigation strategies
- These areas can quickly become pandemic epicenters in metropolitan regions

**Target Users:**
- Low-income residents of dense urban settlements (primarily daily wage workers)
- Community health workers
- Local government agencies

## 🎯 Solution Overview

Our innovative approach shifts focus from individual family units to **collaborative multi-family networks**, leveraging:

- **Economic solidarity** through community cooperation
- **Pooled testing strategies** to maximize limited testing resources
- **Unit-based containment** as an alternative to individual isolation

### Core Innovation: Multi-Family Units

Instead of isolating individual families, we create:
- **Sub-units**: 10-15 geographically and socially connected families
- **Units**: Multiple sub-units sharing infrastructure (toilets, water sources)
- **Super-units**: Trading networks between units for economic sustainability

## 🔬 Technical Approach

### Pooled Testing Strategy

Our solution implements efficient resource allocation through:

- **Sample pooling**: Up to 30 samples tested together with a single test kit
- **Statistical optimization**: In a 500-person unit with 20 infected individuals, testing just 30 randomly selected people provides 75% detection certainty
- **Staged testing**: Positive pools trigger individual testing of all pooled samples

### Web-Based Data Platform

We've developed a comprehensive digital infrastructure:

```
├── Data Collection Portal
├── Random Sampling Algorithm
├── Test Result Management
├── Infection Heatmap Generation
└── Healthcare Worker Interface
```

**Repository**: [https://github.com/sourabhsc/dharavicovid](https://github.com/sourabhsc/dharavicovid)
**Website**: [https://dharavicovid.onrender.com](https://dharavicovid.onrender.com)

## 📍 Use Case: Dharavi Slums, Mumbai

Our pilot implementation targets Mumbai's Dharavi slums, where:
- 41% of the population lives in slum conditions
- Dense living makes traditional social distancing impossible
- Daily wage dependency requires economic continuity solutions

### Implementation Features

1. **Unit Mapping**: Geographic division based on existing social/commercial ties
2. **Resource Sharing**: Pooled finances for bulk purchasing and cottage industries
3. **Limited Mobility**: Two-day work weeks when external employment is necessary
4. **Community Industries**: Soap paper production and inter-unit trading

## ✅ Evidence & Validation

Our approach builds on proven methodologies:

- **Unit Division**: Mumbai's Worli slum already implementing similar quarantine units (March 2020)
- **Pool Testing**: Successfully used during 2014-2016 Ebola outbreak in West Africa
- **Technical Feasibility**: Literature supports pooling up to 32 samples for qRT-PCR COVID-19 testing

## 🛠 Technical Architecture

### Web Platform Components

- **Frontend**: Interactive mapping interface with Google Maps integration
- **Backend**: Data collection and analysis system
- **Database**: Anonymized test results and unit tracking
- **API**: Healthcare worker mobile interface
- **Analytics**: Real-time infection heatmaps

### Key Technologies

- Google Cloud Platform (GCP) for hosting
- Geographic Information Systems (GIS) for unit mapping
- Statistical modeling for sampling optimization
- Mobile-responsive design for field workers

## 🚧 Implementation Challenges & Solutions

### Identified Risks

1. **Inter-unit Competition**
   - **Solution**: Super-unit trading systems with community enforcement

2. **Boundary Compliance**
   - **Solution**: Community leader engagement and transparent communication

3. **Resource Allocation**
   - **Solution**: Government partnership for toilet and water infrastructure

### Technical Requirements

- Updated government database access for toilet/water supply maps
- Partnership with local NGOs (SNEHA, Rahat Covid 19, RAHI)
- Commercial partnerships (MyLab testing kits)

## 📅 Implementation Timeline

**Phase 1** (Days 1-7): Expert consultation and software development
**Phase 2** (Days 8-14): Government and NGO partnership establishment
**Phase 3** (Days 15-21): Community engagement and leader buy-in
**Phase 4** (Days 22-28): On-ground deployment and healthcare worker distribution

**Total Timeline**: 30 days from project approval to full deployment

## 💰 Resource Requirements

### Technical Infrastructure
- Google Cloud Platform hosting costs
- Government database access permissions
- Mobile devices for healthcare workers

### Human Resources
- Public health researchers with dense settlement experience
- Local community leaders
- Trained healthcare workers and volunteers
- Government liaison officers

### Funding Sources
- Johns Hopkins University COVID-19 Launchpad Grant
- CBID Global Immersion Program
- Local government health department allocations

## 📊 Project Documentation

### Available Documents
- **[Final Write-Up](/dharavicovid/docs/Final%20Write-Up.pdf)** - Complete project report with detailed methodology
- **[Technical Model](/dharavicovid/docs/Team94_Model_COVID19JHU.pdf)** - Statistical modeling and effectiveness calculations  
- **[Figures & Visualizations](/dharavicovid/docs/Figures.pptx.pdf)** - Project charts, maps, and data visualizations

## 📊 Expected Impact

- **Immediate**: Reduced transmission rates in dense settlements
- **Economic**: Sustained income through cooperative work arrangements
- **Social**: Enhanced community solidarity and long-term resilience
- **Scalable**: Model applicable to informal settlements globally

## 🤝 Partnership Network

### Current Partners
- **Johns Hopkins University** - CBID COVID-19 Design Challenge Platform
- Mumbai Municipal Corporation
- Local NGOs (SNEHA, Rahat Covid 19, RAHI)

### Team Members (NISER)
This project was developed collaboratively by:
**Preeti**, **Tharun**, **Monali**, **Yoshita**, and **Prajakta**

### Seeking Partnerships
- Government database access facilitators
- Public health research mentors
- Commercial testing kit suppliers
- Community health organizations

## 📈 Future Development

### Immediate Priorities
1. Secure government database access
2. Finalize NGO partnerships
3. Complete web platform development
4. Train community health workers

### Long-term Vision
- Expand to other metropolitan slum areas
- Integrate with existing public health systems
- Develop mobile app for residents
- Create policy framework for government adoption

## 📚 Research Foundation

This solution is grounded in peer-reviewed research and real-world applications:

- Pool testing methodologies from Ebola outbreak response
- Urban slum health intervention studies
- Economic cooperation models in resource-constrained environments
- Digital health platform effectiveness in developing countries

## 📞 Contact & Collaboration

For collaboration opportunities, technical questions, or implementation support, please reach out through:

- **GitHub Issues**: Technical development questions
- **Project Email**: Partnership and implementation inquiries
- **Research Team**: Academic collaboration and peer review

---

*This project represents a collaborative effort between public health researchers, software developers, community organizers, and local government agencies to address one of the most challenging aspects of pandemic response in urban informal settlements.*

## License

This project is developed for public health benefit and community implementation. Please see LICENSE file for usage terms and conditions.



