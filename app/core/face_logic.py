from deepface import DeepFace
import os

def verify_faces(reference_img_path: str, live_img_path: str):
    """
    Compara la foto del carnet (referencia) con la foto capturada en vivo.
    """
    try:
        # DeepFace.verify realiza el matching entre dos imágenes
        # model_name puede ser 'VGG-Face', 'Facenet', 'OpenFace', etc.
        result = DeepFace.verify(
            img1_path = reference_img_path, 
            img2_path = live_img_path,
            model_name = "VGG-Face",
            enforce_detection = True # Lanza error si no detecta un rostro
        )
        return result
    except Exception as e:
        return {"error": str(e)}