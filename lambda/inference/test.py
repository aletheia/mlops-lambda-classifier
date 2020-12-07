from index import handler
import json

event = {
    "body": "{\"Total_Relationship_Count\":4,\"Months_Inactive_12_mon\":0,\"Contacts_Count_12_mon\":10,\"Total_Revolving_Bal\":1000,\"Total_Trans_Amt\":187,\"Total_Trans_Ct\":200,\"Total_Ct_Chng_Q4_Q1\":100,\"Avg_Utilization_Ratio\":1}" 
}

customer = {
    'Total_Relationship_Count': 4, 
    'Months_Inactive_12_mon': 0, 
    'Contacts_Count_12_mon': 10,
    'Total_Revolving_Bal': 1000, 
    'Total_Trans_Amt': 187, 
    'Total_Trans_Ct': 200, 
    'Total_Ct_Chng_Q4_Q1': 100,
    'Avg_Utilization_Ratio': 1
}

event = {}
event['body'] = json.dumps(customer)

context = {}
handler(event,context)