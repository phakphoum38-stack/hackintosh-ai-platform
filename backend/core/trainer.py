# backend/core/trainer.py

import torch
from torch.utils.data import DataLoader, TensorDataset

from core.model import BootModel
from core.dataset import load_dataset


def train():

    data = load_dataset()

    if len(data) < 10:
        print("⚠️ Not enough data to train")
        return

    # 🧠 split features / labels
    X = torch.tensor([d["x"] for d in data], dtype=torch.float32)
    y = torch.tensor([d["y"] for d in data], dtype=torch.float32).view(-1, 1)

    dataset = TensorDataset(X, y)
    loader = DataLoader(dataset, batch_size=8, shuffle=True)

    # 🤖 model
    model = BootModel()

    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    loss_fn = torch.nn.BCELoss()

    # 🔁 training loop
    for epoch in range(20):

        total_loss = 0

        for xb, yb in loader:

            pred = model(xb)
            loss = loss_fn(pred, yb)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            total_loss += loss.item()

        print(f"Epoch {epoch+1} | Loss: {total_loss:.4f}")

    # 💾 save model
    torch.save(model.state_dict(), "models/latest.pth")

    print("✅ Model saved to models/latest.pth")
