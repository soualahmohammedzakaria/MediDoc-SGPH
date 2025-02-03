# MediDoc - Digital Patient Record (DPI) — SGPH

This repository contains the **SGPH API** for the Digital Patient Record (DPI) management system. The goal of the platform is to consolidate and centralize patient data—such as medical history, treatments, test results, and prescriptions—into a single, easily accessible digital file. By improving communication between healthcare professionals, this system helps streamline workflows and provides more consistent care for patients.

## Table of Contents
1. [Project Overview](#project-overview)  
2. [Key Features](#key-features)  
3. [Tech Stack](#tech-stack)  
4. [Getting Started](#getting-started)
5. [Installation](#installation)
6. [Running the Application](#running-the-application)
10. [Further Reading & References](#further-reading--references)  

---

## Project Overview

The **Digital Patient Record (DPI)** is designed to make patient data management as efficient and transparent as possible. By using the DPI, healthcare professionals (doctors, nurses, pharmacists, lab technicians, etc.) can readily access, update, and share patient information. This reduces administrative overhead, minimizes paperwork, and ensures that medical data is synchronized across the entire organization.

### Why MediDoc?
- **Better Patient Care**: Provides quick access to patient history and treatment records.
- **Improved Coordination**: Enables different departments to share updates, results, and prescriptions in real time.
- **Reduced Errors**: Minimizes duplicated tests, missing information, and prescription errors.
  

---

## Key Features

1. **Patient Admission**  
   - Create a digital record with identification details and basic administrative data.
2. **Medical Consultations**  
   - Quickly retrieve a patient’s file by SSN or by scanning a QR code.
3. **Diagnosis & Prescription**  
   - Record visit summaries, prescribe medications, and order additional tests.
4. **Nursing Care**  
   - Track nursing interventions, from administering medications to monitoring patient conditions.
5. **Pharmacy Management**  
   - Access the in-house Hospital Pharmacy Management System (HPMS) to verify and dispense prescriptions.
6. **Lab & Imaging**  
   - Input test results and upload imaging directly into the system.
7. **Patient Self-Service**  
   - Allow patients to view their records, request medical certificates, and access a summary of hospital fees.

---

## Tech Stack

- **Framework**: [Django](https://www.djangoproject.com/) (Python-based)
- **Language**: [Python](https://www.python.org/)
- **Build & Tooling**: [Pipenv](https://pipenv.pypa.io/)

---

# Getting Started

## Prerequisites
1. **Python** (version 3.8 or higher)  
   - [Download Python](https://www.python.org/downloads/)
2. **Pipenv**  
   Install Pipenv globally:
   ```bash
   pip install pipenv
   ```

---

## Installation
1. **Clone the Repository**  
   ```bash
   git clone https://github.com/soualahmohammedzakaria/MediDoc-SGPH.git
   cd MediDoc-SGPH
   ```
2. **Set Up Virtual Environment**  
   Create and activate a virtual environment using Pipenv:
   ```bash
   pipenv install
   pipenv shell
   ```

---

## Running the Application

Start the development server:
```bash
python manage.py runserver 8080
```

Open your browser and navigate to:  
**[http://127.0.0.1:8080/](http://127.0.0.1:8080/)**

---

## Further Reading & References

- [MediDoc Frontend](https://github.com/soualahmohammedzakaria/MediDoc)
- [MediDoc Backend](https://github.com/soualahmohammedzakaria/MediDoc-Backend)
- [Django Documentation](https://docs.djangoproject.com/en/stable/)  
- [Pipenv Documentation](https://pipenv.pypa.io/en/latest/)  

---

**Thank you for checking out the Digital Patient Record (DPI) MediDoc — SGPH project.** If you have any questions, suggestions, or feedback, feel free to open an issue or submit a pull request.

*Maintained by the MediDoc Team.*
