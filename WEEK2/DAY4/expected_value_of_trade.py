win_probability = 0.55
average_win = 0.03

loss_probability = 0.45
average_loss = -0.02

expected_return = (
    win_probability * average_win
    + loss_probability * average_loss
)

print("Expected Return:", expected_return)