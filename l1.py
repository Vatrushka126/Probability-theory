import random

def simulate_urns(iterations=1000000):
    white_drawn_count = 0
    
    for _ in range(iterations):
        urn1 = [1] * 15 + [0] * 5
        urn2 = [1] * 6 + [0] * 1
        
        transferred_balls = random.sample(urn1, 3)
        urn2.extend(transferred_balls)
        
        final_ball = random.choice(urn2)
        
        if final_ball == 1:
            white_drawn_count += 1
            
    return white_drawn_count / iterations

emp_prob = simulate_urns()
print(f"Эксперимент: {emp_prob:.4f}")
print(f"Теория: {33/40:.4f}")
