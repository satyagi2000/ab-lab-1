def score_deal(amount: float, risk: int, customer_type: str) -> float: 
    base = amount / 1000.0 

    multipliers = { 
        "enterprise": 1.25, 
        "smb": 1.0, 
        "consumer": 0.9, 
        } 
    multiplier = multipliers.get(customer_type, 0.9)
    
    if risk >= 80: 
        penalty = 3.0 
    elif risk >= 50: 
        penalty = 2.0 
    elif risk >= 20: 
        penalty = 1.0 
    else: 
        penalty = 0.3 
    return (base * multiplier) - penalty 

def decision(score: float) -> str: 
    thresholds = [
        (8, "APPROVE"),
        (4, "REVIEW"),
    ]
    for threshold, label in thresholds:
        if score >= threshold:
            return label
    return "REJECT"

def main() -> None: 
    amount = 10000.0 
    risk = 35
    customer_type = "smb" 

    s = score_deal(amount, risk, customer_type) 
    print(f"score={s:.2f} decision={decision(s)}") 

if __name__ == "__main__": 
    main() 