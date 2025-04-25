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

## Email Sending Configuration (Task 1, Subtask 4e)

This section describes how to configure Gmail as the outgoing email server in Odoo for the "Send emails" functionality implemented in Task 1, Subtask 4d. It also explains where to find failed emails in the Odoo GUI if the email sending fails.

### Configuring Gmail as the Outgoing Email Server

To enable the "Send emails" button (which sends emails based on the Excel file uploaded in the `employee_contacts` field), you need to configure Gmail as the outgoing email server in Odoo. Follow these steps:

1. **Prepare Gmail Account**:
   1.1 Ensure your Gmail account has 2-Step Verification enabled (Google Account > Security > 2-Step Verification).
   1.2 Generate an App Password for Odoo:
     1.2.1 Go to App Passwords in Google Account.
     1.2.2 Generate the password and copy it.

2. **Configure Outgoing Email Server in Odoo**:
   - Log in to Odoo as an administrator.
   - Go to "Settings" > "General Settings".
   - In the "Emails" section, find "Outgoing Email Servers" and click "Create".
   - Fill in the details:
      - **Name**: `Gmail SMTP`
      - **SMTP Server**: `smtp.gmail.com`
      - **SMTP Port**: `587`
      - **Connection Encryption**: `TLS (STARTTLS)`
      - **Username**: Your Gmail address (e.g., `your.email@gmail.com`)
      - **Password**: The App Password generated earlier (e.g., `abcd efgh ijkl mnop`)
   - Save the settings and click "Test Connection". You should see a "Connection Test Successful" message.

3. **Test Email Sending**:
   - Go to "Employees" and select an employee.
   - Ensure the `employee_contacts` field has an Excel file uploaded.
   - Click the "Send emails" button.
   - If configured correctly, emails will be sent to the addresses listed in the Excel file with the subject from the second column and the body "Welcome in GymBeam".

### Finding Failed Emails in Odoo

If the email sending fails (e.g., due to incorrect SMTP settings or invalid email addresses), Odoo stores these emails in a queue. You can view and manage them in the GUI as follows:

1. **Activate Developer Mode**:
   - Go to "Settings" and click "Activate the developer mode" under "Developer Tools".

2. **Access the Email Queue**:
   - In the top menu, search for "Emails" or navigate to "Settings" > "Technical" > "Emails".
   - This opens the email queue where all email attempts are logged.

3. **Locate Failed Emails**:
   - Look for emails with a status of "Exception" or "Failed".
   - Click on a failed email to see the error message (e.g., "SMTP Authentication Failed" or "Invalid Recipient").
   - You can retry sending the email by clicking "Retry" or delete it if no longer needed.

## Development Notes

- The module is located in the ./addons/gymbeam_custom directory, which is mounted to /mnt/extra-addons in the Docker container.
- To apply changes to the module, modify the files in ./addons/gymbeam_custom, then restart the container (docker-compose restart) and upgrade the module in Odoo ("Apps" > "GymBeam Custom Module" > "Upgrade").
