def score_deal(amount: float, risk: int, customer_type: str) -> float: 
    base = amount / 1000.0 
    if customer_type == "enterprise": 
        multiplier = 1.3 
    elif customer_type == "smb": 
        multiplier = 1.0 
    else: 
        multiplier = 0.9 
    
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
    if score >= 8: 
        return "APPROVE" 
    if score >= 4: 
        return "REVIEW" 
    return "REJECT" 

def main() -> None: 
    amount = 10000.0 
    risk = 35 
    customer_type = "smb" 

    s = score_deal(amount, risk, customer_type) 
    print(f"score={s:.2f} decision={decision(s)}") 

if __name__ == "__main__": 
    main() 