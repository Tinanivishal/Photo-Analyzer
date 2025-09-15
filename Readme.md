# 📸 Photo Upload & Analysis System  

This project demonstrates a **serverless image analysis pipeline** using **AWS services**.  
Users can upload photos to an S3 bucket, which automatically triggers a Lambda function.  
The Lambda function uses **Amazon Rekognition** to analyze the image and store the extracted labels with confidence scores into a **MySQL database hosted on Amazon RDS**.  

---

## 🚀 Architecture Flow  

1. User uploads a photo → Stored in **Amazon S3**.  
2. **S3 event** triggers a **Lambda function**.  
3. **Lambda** calls **Amazon Rekognition** → Extracts labels (e.g., `Dog`, `Person`).  
4. **Lambda** stores results in **Amazon RDS MySQL**.  
5. **IAM Roles** provide secure access between AWS services.  

---

## 🛠️ AWS Services Used  

- **Amazon S3** → Stores uploaded images.  
- **AWS Lambda** → Serverless function to process events.  
- **Amazon Rekognition** → Image analysis (labels & confidence).  
- **Amazon RDS (MySQL)** → Database to store image labels.  
- **IAM** → Secure role-based access.  

---

## 📂 Database Schema  

```sql
CREATE DATABASE PhotoApp;
USE PhotoApp;

CREATE TABLE PhotoLabels (
  id INT AUTO_INCREMENT PRIMARY KEY,
  ImageKey VARCHAR(255) NOT NULL,
  Label VARCHAR(100) NOT NULL,
  Confidence DECIMAL(5,2) NOT NULL,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
⚙️ Setup Instructions
1. Create S3 Bucket
Go to S3 → Create bucket.

Name: photo-upload-bucket-<yourname> (must be unique).

Block all public access (keep private).

2. Create RDS MySQL Database
Engine: MySQL

Instance identifier: photoanalysisdb

Username: admin

Password: Iantpln1232025

Enable Public Access = Yes (for learning only).

Open port 3306 in Security Group for Lambda’s VPC.

3. Create Database Table
Use SQL Electron or MySQL client to run the schema above.

4. Create IAM Role for Lambda
Trusted entity: Lambda

Attach policies:

AmazonS3ReadOnlyAccess

AmazonRekognitionFullAccess

AmazonRDSFullAccess (for learning)

Role name: LambdaPhotoAnalysisRole

5. Create Lambda Function
Function name: PhotoAnalyzerLambda

Runtime: Python 3.12

Execution role: LambdaPhotoAnalysisRole

6. Add S3 Trigger
Inside Lambda → Add Trigger → Select S3.

Choose bucket → photo-upload-bucket-<yourname>.

Event type: PUT.

7. Deploy Lambda Code
Upload my_lambda_function.zip (from repo or Drive link).

8. Upload a Test Image
Upload a .jpg to the S3 bucket.

Check RDS MySQL with:

sql
Copy code
SELECT * FROM PhotoLabels;
You should see labels like:

matlab
Copy code
Dog   | 98.12%
Person| 95.45%
📊 Example Output
ID	ImageKey	Label	Confidence	CreatedAt
1	dog.jpg	Dog	98.12	2025-09-15 10:23:00
2	dog.jpg	Person	95.45	2025-09-15 10:23:00

📌 Notes
For production, set RDS Public Access = No.

Restrict IAM permissions to follow least privilege principle.

You can extend this project with:

API Gateway + Lambda for API-based access.

SNS Notifications when new labels are added.

Frontend (React/Angular) to display uploaded images with analysis results.

📜 License
This project is licensed under the MIT License.

yaml
Copy code

---

👉 Vishal, do you also want me to **add the Lambda Python code section** inside the README (instead of just uploading ZIP), so others can directly see and run it from GitHub?







Ask ChatGPT
