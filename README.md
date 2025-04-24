# GymBeam Custom Module for Odoo 16

## Overview

This is a custom Odoo 16 module (gymbeam_custom) developed as part of the GymBeam Python Developer case study. The module extends the functionality of the Odoo HR system by adding custom fields, validations, and features to the Employee and Applicant models. It includes features like custom employee fields, email sending functionality, unique employee number validation, and an API endpoint for creating applicants.

The module is designed to work with Odoo 16 Community Edition and requires the hr (Employees) and hr_recruitment (Recruitment) modules as dependencies.

## Features

- Adds custom fields to the Employee form (i_love_gb, employee_contacts, salary, tax, total_salary, special_phone).
- Ensures employee numbers are unique across Employees and Applicants.
- Provides an API endpoint for creating applicants from JSON data.
- Implements email sending functionality via a wizard.

## Prerequisites

- Odoo 16 Community Edition installed.
- Docker and docker-compose for running Odoo (optional but recommended).
- The hr and hr_recruitment modules must be installed in Odoo.

## Installation
1. Clone or copy the module:
 - Place the gymbeam_custom folder into your Odoo addons directory (e.g., ./addons/gymbeam_custom if using the provided docker-compose.yml).
2. Set up Odoo with Docker (if not already done):
- Use the provided docker-compose.yml to set up Odoo and PostgreSQL:
  ```bash
  docker-compose up -d

- Access Odoo at http://localhost:8069 and create a new database.

3. Install dependencies:

- In Odoo, go to the "Apps" menu.
- Install the "Employees" (hr) and "Recruitment" (hr_recruitment) modules.

4. Install the module:

- Activate Developer Mode in Odoo (Settings > Activate the developer mode).
- Go to "Apps", remove the "Apps" filter, and search for "GymBeam Custom Module".
- Click "Install".

5. Verify installation:

- Go to the "Employees" menu and open any employee record to see the new fields (I love GymBeam, Special Phone, etc.).

## Usage

- Custom Fields: Create or edit an employee to use the new fields like I love GymBeam, Salary, Tax, and Special Phone.
- Unique Employee Number: The employee_number field ensures uniqueness across employees and applicants.
- API Endpoint: Send a POST request to http://localhost:8069/case_study/applicant/get with a JSON payload to create applicants.

## Development Notes

- The module is located in the ./addons/gymbeam_custom directory, which is mounted to /mnt/extra-addons in the Docker container.
- To apply changes to the module, modify the files in ./addons/gymbeam_custom, then restart the container (docker-compose restart) and upgrade the module in Odoo ("Apps" > "GymBeam Custom Module" > "Upgrade").
