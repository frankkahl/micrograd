import torch


def main():
    print(torch.version.cuda, torch.cuda.is_available())
    print(torch.cuda.get_device_name(
        0))  # NVIDIA GeForce RTX 4060 …
    x = torch.randn(3, 3,
                    device="cuda")  # a tensor created directly on the GPU
    print(x.device)  # cuda:0


if __name__ == "__main__":
    main()
