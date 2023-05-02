from django import forms
from StudentEvaluation.models import Profile

class DataForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = [  'Name',
                    'College_ID',
                    'Nationality',
                    'Marital_Status',
                    'Application_Order',
                    'Application_Mode',
                    'Course',
                    'Attendance',
                    'Previous_qualification',
                    'Father_Qualification',
                    'Mother_Qualification',
                    'Father_Occupation',
                    'Mother_Occupation',
                    'Displaced',
                    'Educational_Special_Needs',
                    'Debtor',
                    'Tuition_fees_up_to_date',
                    'Gender',
                    'Scholarship_Holder',
                    'Age_at_enrollment',
                    'International',
                    'Curricular_units_1st_sem_credited',
                    'Curricular_units_1st_sem_enrolled',
                    'Curricular_units_1st_sem_evaluations',
                    'Curricular_units_1st_sem_approved',
                    'Curricular_units_1st_sem_grade',
                    'Curricular_units_1st_sem_without_evaluations',
                    'Curricular_units_2nd_sem_credited',
                    'Curricular_units_2nd_sem_enrolled',
                    'Curricular_units_2nd_sem_evaluations',
                    'Curricular_units_2nd_sem_approved',
                    'Curricular_units_2nd_sem_grade',
                    'Curricular_units_2nd_sem_without_evaluations',
                    'Unemployment_Rate',
                    'Inflation_Rate',
                    'GDP',
                    ]
