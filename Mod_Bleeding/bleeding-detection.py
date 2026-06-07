import cv2
import os
from ultralytics import YOLO

# 1. Defina os caminhos com segurança
model_path = r'C:\Users\Administrador\Documents\FIAP\Fase 4\GynSurg\Modulo\best.pt'
video_path = r'C:\Users\Administrador\Documents\FIAP\Fase 4\GynSurg\Modulo\video_cirurgia.mp4'

if not os.path.exists(model_path):
    print(f"ERRO: Arquivo do modelo não encontrado em {os.path.abspath(model_path)}")
    exit()

if not os.path.exists(video_path):
    print(f"ERRO: Vídeo não encontrado em {os.path.abspath(video_path)}")
    exit()

# 2. Carrega o modelo
model = YOLO(model_path)

# 3. Configurações de alerta
THRESHOLD_SANGRAMENTO = 0.85

# Configurações de estilo para o texto
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.5
thickness = 1
padding = 10 

cap = cv2.VideoCapture(video_path)

print("Processando... Pressione 'q' para sair.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Fim do vídeo ou falha na leitura.")
        break

    # stream=True otimiza a memória para processamento de vídeo
    results = model(frame, stream=True) 

    for r in results:
        probs = r.probs
        top1_id = probs.top1
        confidence = probs.top1conf.item()
        label_name = model.names[top1_id]

        # Lógica de Alerta
        if label_name == 'bleeding' and confidence > THRESHOLD_SANGRAMENTO:
            # Borda vermelha na tela toda
            cv2.rectangle(frame, (0, 0), (frame.shape[1], frame.shape[0]), (0, 0, 255), 15)
            
            texto = f"ALERTA: SANGRAMENTO ({confidence:.2f})"
            color = (0, 0, 255) # Vermelho
        else:
            # Borda verde na tela toda
            cv2.rectangle(frame, (0, 0), (frame.shape[1], frame.shape[0]), (0, 255, 0), 15)
            texto = "SEGURO"
            color = (0, 255, 0) # Verde

        # Calcula o tamanho do texto para o fundo dinâmico
        (w, h), baseline = cv2.getTextSize(texto, font, font_scale, thickness)

        # Desenha o retângulo de fundo (coordenadas: (10,10) até o tamanho do texto + padding)
        cv2.rectangle(frame, (10, 10), (10 + w + padding, 10 + h + padding), color, -1)

        # Desenha o texto por cima (cor branca para contraste)
        cv2.putText(frame, texto, (10 + padding // 2, 10 + h), 
                    font, font_scale, (255, 255, 255), thickness)

    # Exibe em tempo real
    cv2.imshow('Monitoramento GynSurg', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()