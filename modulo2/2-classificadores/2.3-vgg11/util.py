from torchvision import transforms
import json

class Preprocessador:
    def __init__(self):
        self.preprocessamento = transforms.Compose([
                            transforms.Resize(256),
                            transforms.CenterCrop(224),
                            transforms.ToTensor(),
                            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
                        ])
    def executa(self, imagem):
        return self.preprocessamento(imagem)

# Obtem o label de acordo com o indice melhor classificado.
def getLabel(index):
    class_idx = json.load(open("./labels/imagenet_class_index.json"))
    idx2label = [class_idx[str(k)][1] for k in range(len(class_idx))]
    return idx2label[index]
