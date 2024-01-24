from ultralytics import YOLO
import torch

if torch.cuda.is_available():
    print("CUDA está disponible. GPU:", torch.cuda.get_device_name(0))
else:
    print("CUDA no está disponible.")

def train_model():
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = YOLO("yolov8n-cls.pt")   #Cambiar entre yolov8n-cls.pt y yolov8n.pt dependiendo si es para clasificacion o deteccion

    model.train(data=r"C:\Users\carlo\Downloads\Prueba.v2i.folder",
                epochs=70, batch=16, imgsz=848)

if __name__ == '__main__':
    train_model()
