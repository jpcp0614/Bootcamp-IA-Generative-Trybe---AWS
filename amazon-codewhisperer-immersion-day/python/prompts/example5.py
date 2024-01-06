# define torch nn.module with 1 input layer,
# 3 hidden layers, and 1 output layer
import torch.nn as nn
import torch

# define function to train model


def train_model(model, train_loader, criterion, optimizer, num_epochs):
    for epoch in range(num_epochs):
        running_loss = 0.0
        for i, data in enumerate(train_loader, 0):
            inputs, labels = data
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
            if i % 2000 == 1999:
                print(
                    "[%d, %5d] loss: %.3f" % (
                        epoch + 1, i + 1, running_loss / 2000)
                    )
                running_loss = 0.0
    print("Finished Training")
