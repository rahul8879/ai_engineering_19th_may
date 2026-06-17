def predict(cibil_score,income):
    if cibil_score < 600:
        if income < 20000:
            return "Rejected"
        else:
            return "Rejected"
    elif cibil_score >= 700 and income >= 30000:
        return "Approved"
    else:
        return "Rejected"
    
 