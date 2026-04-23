import torch
from backend.core.model import BootModel
from backend.core.dataset import load_dataset

def train():

    data = load_dataset()

    X = torch.tensor([d["x"] for d in data], dtype=torch.float32)
    y = torch.tensor([d["y"] for d in data], dtype=torch.float32).view(-1,1)

    model = BootModel()

    opt = torch.optim.Adam(model.parameters(), lr=0.001)
    loss_fn = torch.nn.BCELoss()

    for epoch in range(20):

        pred = model(X)
        loss = loss_fn(pred, y)

        opt.zero_grad()
        loss.backward()
        opt.step()

        print("epoch", epoch, "loss", loss.item())

    torch.save(model.state_dict(), "models/latest.pth")

if __name__ == "__main__":
    train()
