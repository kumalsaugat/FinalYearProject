from django.db import models
from django.contrib.auth.models import User
import joblib
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

MARITAL_STATUS = [

    ("1" ,"Single"),
    ("2" , "Married"),
    ("3" , "Widower"),
    ("4" , "Divorced"),
    ("5" , "Facto union" ),
    ("6" , "Legally separated")]    

NATIONALITY = [
    ("1","Portuguese")  ,
    ("2","German")  ,
    ("3","Spanish")  ,
    ("4","Italian")  ,
    ("5","Dutch")  ,
    ("6","English")  ,
    ("7","Lithuanian")  ,
    ("8","Nepal")  ,
    ("9","Cape Verdean")  ,
    ("10","Guinean")  ,
    ("11","Mozambican")  ,
    ("12","Santomean")  ,
    ("13","Turkish")  ,
    ("14","Brazilian")  ,
    ("15","Romanian")  ,
    ("16","Moldova (Republic of)")  ,
    ("17","Mexican")  ,
    ("18","Ukrainian")  ,
    ("19","Russian")  ,
    ("20","Cuban")  ,
    ("21","Colombian")]

Application_Mode = [
    ("1" , "1st phase—general contingent") ,
    ("2" , "Ordinance No. 612/93")  ,
    ("3" , "1st phase—special contingent (Azores Island)")  ,
    ("4" , "Holders of other higher courses")  ,
    ("5" , "Ordinance No. 854-B/99")  ,
    ("6" , "International student (bachelor) ") ,
    ("7" , "1st phase—special contingent (Madeira Island)")  ,
    ("8" , "2nd phase—general contingent")  ,
    ("9" , "3rd phase—general contingent")  ,
    ("10" , "Ordinance No. 533-A/99, item b2) (Different Plan)")  ,
    ("11" , "Ordinance No. 533-A/99, item b3 (Other Institution)")  ,
    ("12" , "Over 23 years old")  ,
    ("13" , "Transfer")  ,
    ("14" , "Change in course")  ,
    ("15" , "Technological specialization diploma holders")  ,
    ("16" , "Change in institution/course")  ,
    ("17" , "Short cycle diploma holders")  ,
    ("18" , "Change in institution/course (International)")]
  
COURSE = [
    ("1" , "Biofuel Production Technologies"),
    ("2" , "Animation and Multimedia Design"),
    ("3" , "Social Service (evening attendance)"),
    ("4" , "Agronomy"),
    ("5" , "Communication Design"),
    ("6" , "Veterinary Nursing"),
    ("7" , "Informatics Engineering"),
    ("8" , "Equiniculture"),
    ("9" , "Management"),
    ("10" , "Social Service"),
    ("11" , "Tourism"),
    ("12" , "Nursing"),
    ("13" , "Oral Hygiene"),
    ("14" , "Advertising and Marketing Management"),
    ("15" , "Journalism and Communication"),
    ("16" , "Basic Education"),
    ("17" , "Management (evening attendance)")]

Previous_qualification = [
    ("1" , "Secondary education"),
    ("2" , "Higher education—bachelor’s degree"),
    ("3" , "Higher education—degree"),
    ("4" , "Higher education—master’s degree"),
    ("5" , "Higher education—doctorate"),
    ("6" , "Frequency of higher education"),
    ("7" , "12th year of schooling—not completed"),
    ("8" , "11th year of schooling—not completed"),
    ("9" , "Other—11th year of schooling"),
    ("10" , "10th year of schooling"),
    ("11" , "10th year of schooling—not completed"),
    ("12" , "Basic education 3rd cycle (9th/10th/11th year) or equivalent"),
    ("13" , "Basic education 2nd cycle (6th/7th/8th year) or equivalent"),
    ("14" , "Technological specialization course"),
    ("15" , "Higher education—degree (1st cycle)"),
    ("16" , "Professional higher technical course"),
    ("17" , "Higher education—master’s degree (2nd cycle)")]

Mother_Qualification = [
    ("1" , "Secondary Education—12th Year of Schooling or Equivalent" ),
    ("2" , "Higher Education—bachelor’s degree" ),
    ("3" , "Higher Education—degree" ),
    ("4" , "Higher Education—master’s degree" ),
    ("5" , "Higher Education—doctorate" ),
    ("6" , "Frequency of Higher Education" ),
    ("7" , "12th Year of Schooling—not completed" ),
    ("8" , "11th Year of Schooling—not completed" ),
    ("9" , "7th Year (Old)" ),
    ("10" , "Other—11th Year of Schooling" ),
    ("11" , "2nd year complementary high school course" ),
    ("12" , "10th Year of Schooling" ),
    ("13" , "General commerce course" ),
    ("14" , "Basic Education 3rd Cycle (9th/10th/11th Year) or Equivalent" ),
    ("15" , "Complementary High School Course" ),
    ("16" , "Technical-professional course" ),
    ("17" , "Complementary High School Course—not concluded" ),
    ("18" , "7th year of schooling" ),
    ("19" , "2nd cycle of the general high school course" ),
    ("20" , "9th Year of Schooling—not completed" ),
    ("21" , "8th year of schooling" ),
    ("22" , "General Course of Administration and Commerce" ),
    ("23" , "Supplementary Accounting and Administration" ),
    ("24" , "Unknown" ),
    ("25" , "Cannot read or write" ),
    ("26" , "Can read without having a 4th year of schooling" ),
    ("27" , "Basic education 1st cycle (4th/5th year) or equivalent" ),
    ("28" , "Basic Education 2nd Cycle (6th/7th/8th Year) or equivalent" ),
    ("29" , "Technological specialization course" ),
    ("30" , "Higher education—degree (1st cycle)" ),
    ("31" , "Specialized higher studies course" ),
    ("32" , "Professional higher technical course" ),
    ("33" , "Higher Education—master’s degree (2nd cycle)" ),
    ("34" , "Higher Education—doctorate (3rd cycle)" )]

Father_Qualification = [
    ("1" , "Secondary Education—12th Year of Schooling or Equivalent" ),
    ("2" , "Higher Education—bachelor’s degree" ),
    ("3" , "Higher Education—degree" ),
    ("4" , "Higher Education—master’s degree" ),
    ("5" , "Higher Education—doctorate" ),
    ("6" , "Frequency of Higher Education" ),
    ("7" , "12th Year of Schooling—not completed" ),
    ("8" , "11th Year of Schooling—not completed" ),
    ("9" , "7th Year (Old)" ),
    ("10" , "Other—11th Year of Schooling" ),
    ("11" , "2nd year complementary high school course" ),
    ("12" , "10th Year of Schooling" ),
    ("13" , "General commerce course" ),
    ("14" , "Basic Education 3rd Cycle (9th/10th/11th Year) or Equivalent" ),
    ("15" , "Complementary High School Course" ),
    ("16" , "Technical-professional course" ),
    ("17" , "Complementary High School Course—not concluded" ),
    ("18" , "7th year of schooling" ),
    ("19" , "2nd cycle of the general high school course" ),
    ("20" , "9th Year of Schooling—not completed" ),
    ("21" , "8th year of schooling" ),
    ("22" , "General Course of Administration and Commerce" ),
    ("23" , "Supplementary Accounting and Administration" ),
    ("24" , "Unknown" ),
    ("25" , "Cannot read or write" ),
    ("26" , "Can read without having a 4th year of schooling" ),
    ("27" , "Basic education 1st cycle (4th/5th year) or equivalent" ),
    ("28" , "Basic Education 2nd Cycle (6th/7th/8th Year) or equivalent" ),
    ("29" , "Technological specialization course" ),
    ("30" , "Higher education—degree (1st cycle)" ),
    ("31" , "Specialized higher studies course" ),
    ("32" , "Professional higher technical course" ),
    ("33" , "Higher Education—master’s degree (2nd cycle)" ),
    ("34" , "Higher Education—doctorate (3rd cycle)" )]

Mother_Occupation = [
    ("1" , "Student" ),
    ("2" , "Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers" ),
    ("3" , "Specialists in Intellectual and Scientific Activities" ),
    ("4" , "Intermediate Level Technicians and Professions" ),
    ("5" , "Administrative staff" ),
    ("6" , "Personal Services, Security and Safety Workers, and Sellers" ),
    ("7" , "Farmers and Skilled Workers in Agriculture, Fisheries, and Forestry" ),
    ("8" , "Skilled Workers in Industry, Construction, and Craftsmen" ),
    ("9" , "Installation and Machine Operators and Assembly Workers" ),
    ("10" , "Unskilled Workers" ),
    ("11" , "Armed Forces Professions" ),
    ("12" , "Other Situation; (blank)" ),
    ("13" , "blank" ),
    ("14" , "Armed Forces Officers" ),
    ("15" , "Armed Forces Sergeants" ),
    ("16" , "Other Armed Forces personnel" ), 
    ("17" , "Directors of administrative and commercial services" ),
    ("18" , "Hotel, catering, trade, and other services directors" ),
    ("19" , "Specialists in the physical sciences, mathematics, engineering, and related techniques" ),
    ("20" , "Health professionals" ),
    ("21" , "Teachers" ),
    ("22" , "Specialists in finance, accounting, administrative organization, and public and commercial relations" ),
    ("23" , "Intermediate level science and engineering technicians and professions" ),
    ("24" , "Technicians and professionals of intermediate level of health" ),
    ("25" , "Intermediate level technicians from legal, social, sports, cultural, and similar services" ),
    ("26" , "Information and communication technology technicians" ),
    ("27" , "Office workers, secretaries in general, and data processing operators" ),
    ("28" , "Data, accounting, statistical, financial services, and registry-related operators" ),
    ("29" , "Other administrative support staff" ),
    ("30" , "Personal service workers" ),
    ("31" , "Sellers" ),
    ("32" , "Personal care workers and the like" ),
    ("33" , "Protection and security services personnel" ),
    ("34" , "Market-oriented farmers and skilled agricultural and animal production workers" ),
    ("35" , "Farmers, livestock keepers, fishermen, hunters and gatherers, and subsistence" ),
    ("36" , "Skilled construction workers and the like, except electricians" ),
    ("37" , "Skilled workers in metallurgy, metalworking, and similar" ),
    ("38" , "Skilled workers in electricity and electronics" ),
    ("39" , "Workers in food processing, woodworking, and clothing and other industries and crafts" ),
    ("40" , "Fixed plant and machine operators" ),
    ("41" , "Assembly workers" ),
    ("42" , "Vehicle drivers and mobile equipment operators" ),
    ("43" , "Unskilled workers in agriculture, animal production, and fisheries and forestry" ),
    ("44" , "Unskilled workers in extractive industry, construction, manufacturing, and transport" ),
    ("45" , "Meal preparation assistants" ),      
    ("46" , "Street vendors (except food) and street service providers" )]

Father_Occupation = [
    ("1" , "Student" ),
    ("2" , "Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers" ),
    ("3" , "Specialists in Intellectual and Scientific Activities" ),
    ("4" , "Intermediate Level Technicians and Professions" ),
    ("5" , "Administrative staff" ),
    ("6" , "Personal Services, Security and Safety Workers, and Sellers" ),
    ("7" , "Farmers and Skilled Workers in Agriculture, Fisheries, and Forestry" ),
    ("8" , "Skilled Workers in Industry, Construction, and Craftsmen" ),
    ("9" , "Installation and Machine Operators and Assembly Workers" ),
    ("10" , "Unskilled Workers" ),
    ("11" , "Armed Forces Professions" ),
    ("12" , "Other Situation; (blank)" ),
    ("13" , "blank" ),
    ("14" , "Armed Forces Officers" ),
    ("15" , "Armed Forces Sergeants" ),
    ("16" , "Other Armed Forces personnel" ), 
    ("17" , "Directors of administrative and commercial services" ),
    ("18" , "Hotel, catering, trade, and other services directors" ),
    ("19" , "Specialists in the physical sciences, mathematics, engineering, and related techniques" ),
    ("20" , "Health professionals" ),
    ("21" , "Teachers" ),
    ("22" , "Specialists in finance, accounting, administrative organization, and public and commercial relations" ),
    ("23" , "Intermediate level science and engineering technicians and professions" ),
    ("24" , "Technicians and professionals of intermediate level of health" ),
    ("25" , "Intermediate level technicians from legal, social, sports, cultural, and similar services" ),
    ("26" , "Information and communication technology technicians" ),
    ("27" , "Office workers, secretaries in general, and data processing operators" ),
    ("28" , "Data, accounting, statistical, financial services, and registry-related operators" ),
    ("29" , "Other administrative support staff" ),
    ("30" , "Personal service workers" ),
    ("31" , "Sellers" ),
    ("32" , "Personal care workers and the like" ),
    ("33" , "Protection and security services personnel" ),
    ("34" , "Market-oriented farmers and skilled agricultural and animal production workers" ),
    ("35" , "Farmers, livestock keepers, fishermen, hunters and gatherers, and subsistence" ),
    ("36" , "Skilled construction workers and the like, except electricians" ),
    ("37" , "Skilled workers in metallurgy, metalworking, and similar" ),
    ("38" , "Skilled workers in electricity and electronics" ),
    ("39" , "Workers in food processing, woodworking, and clothing and other industries and crafts" ),
    ("40" , "Fixed plant and machine operators" ),
    ("41" , "Assembly workers" ),
    ("42" , "Vehicle drivers and mobile equipment operators" ),
    ("43" , "Unskilled workers in agriculture, animal production, and fisheries and forestry" ),
    ("44" , "Unskilled workers in extractive industry, construction, manufacturing, and transport" ),
    ("45" , "Meal preparation assistants" ),      
    ("46" , "Street vendors (except food) and street service providers" )]


Gender = [
    ("1" , "male"),
    ("0", "female")
    ]

Attendance = [
    ("1" , "Day Shift") ,
    ("0" , "Evening Shift")
    ]

Age_at_enrollment = [
    ("1" , "Yes"),
    ("0" , "No")
    ]

Displaced = [
    ("1" , "Yes"),
    ("0" , "No")
    ]

Educational_Special_Needs = [
    ("1" , "Yes"),
    ("0" , "No")
    ]

Debtor = [
    ("1" , "Yes"),
    ("0" , "No")
    ]

Tuition_fees_up_to_date = [
    ("1" , "Yes"),
    ("0" , "No")
    ]

Scholarship_Holder = [
    ("1" , "Yes"),
    ("0" , "No")
    ]

International = [
    ("1" , "Yes"),
    ("0" , "No")
    ]



class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50, blank=True)
    College_ID = models.CharField(max_length=50)
    Nationality = models.CharField(choices=NATIONALITY, max_length=50)
    Marital_Status = models.CharField(choices=MARITAL_STATUS, max_length=50 )
    Application_Order = models.CharField(max_length=50)
    Application_Mode = models.CharField(choices=Application_Mode ,max_length=50)
    Course = models.CharField(choices=COURSE, max_length=50)
    Attendance = models.CharField(choices=Attendance , max_length=50)
    Previous_qualification = models.CharField(choices=Previous_qualification ,max_length=50)
    
    Father_Qualification = models.CharField(choices=Father_Qualification , max_length=50)
    Mother_Qualification = models.CharField(choices=Mother_Qualification ,max_length=50)
    Father_Occupation = models.CharField(choices=Father_Occupation ,max_length=50)
    Mother_Occupation = models.CharField(choices=Mother_Occupation ,max_length=50)
    Displaced = models.CharField(choices=Displaced ,max_length=50)
    Educational_Special_Needs = models.CharField(choices=Educational_Special_Needs ,max_length=50)
    Debtor = models.CharField(choices=Debtor ,max_length=50)
    Tuition_fees_up_to_date = models.CharField(choices=Tuition_fees_up_to_date ,max_length=50)
    Gender = models.CharField(choices=Gender ,max_length=50)
    Scholarship_Holder = models.CharField(choices=Scholarship_Holder ,max_length=50)
    Age_at_enrollment = models.PositiveIntegerField(validators=[MinValueValidator(15), MaxValueValidator(50)])
    International = models.CharField(choices=International ,max_length=50)
    
    Curricular_units_1st_sem_credited = models.PositiveIntegerField()
    Curricular_units_1st_sem_enrolled = models.PositiveIntegerField()
    Curricular_units_1st_sem_evaluations = models.PositiveIntegerField()
    Curricular_units_1st_sem_approved = models.PositiveIntegerField()
    Curricular_units_1st_sem_grade = models.PositiveIntegerField()
    Curricular_units_1st_sem_without_evaluations = models.PositiveIntegerField()

    Curricular_units_2nd_sem_credited = models.PositiveIntegerField()
    Curricular_units_2nd_sem_enrolled = models.PositiveIntegerField()
    Curricular_units_2nd_sem_evaluations = models.PositiveIntegerField()
    Curricular_units_2nd_sem_approved = models.PositiveIntegerField()
    Curricular_units_2nd_sem_grade = models.PositiveIntegerField()
    Curricular_units_2nd_sem_without_evaluations = models.PositiveIntegerField()

    Unemployment_Rate = models.IntegerField()
    Inflation_Rate = models.IntegerField()
    GDP = models.IntegerField()

    is_submitted = models.BooleanField(default=False)

    
    predictions = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        from .RandomForest import RandomForest

        LoadModel = joblib.load(open("C:\django project\Final Year Project Code\FinalProject\models\Student_Prediction_Model.pkl", "rb"))
        predicted_label = LoadModel.predict(
            [[self.Nationality,
                self.Marital_Status,
                self.Application_Order,
                self.Application_Mode,
                self.Course,
                self.Attendance,
                self.Previous_qualification,
                self.Father_Qualification,
                self.Mother_Qualification,
                self.Father_Occupation,
                self.Mother_Occupation,
                self.Displaced,
                self.Educational_Special_Needs,
                self.Debtor,
                self.Tuition_fees_up_to_date,
                self.Gender,
                self.Scholarship_Holder,
                self.Age_at_enrollment,
                self.International,
                self.Curricular_units_1st_sem_credited,
                self.Curricular_units_1st_sem_enrolled,
                self.Curricular_units_1st_sem_evaluations,
                self.Curricular_units_1st_sem_approved,
                self.Curricular_units_1st_sem_grade,
                self.Curricular_units_1st_sem_without_evaluations,
                self.Curricular_units_2nd_sem_credited,
                self.Curricular_units_2nd_sem_enrolled,
                self.Curricular_units_2nd_sem_evaluations,
                self.Curricular_units_2nd_sem_approved,
                self.Curricular_units_2nd_sem_grade,
                self.Curricular_units_2nd_sem_without_evaluations,
                self.Unemployment_Rate,
                self.Inflation_Rate,
                self.GDP


              ]]
            )
        
        # convert the predicted label to its corresponding string value
        if predicted_label == 0:
            prediction_str = "Dropout"
        elif predicted_label == 1:
            prediction_str = "Enrolled"
        else:
            prediction_str = "Graduate"

        # set the predictions field to the string value of the predicted label
        self.predictions = prediction_str

        return super().save(*args, *kwargs)
        
    def __str__(self):
        return f"user:{self.user}, Name: {self.Name}, College ID: {self.College_ID}"