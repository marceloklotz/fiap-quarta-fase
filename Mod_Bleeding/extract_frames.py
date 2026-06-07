import cv2
import os
import glob

def extract_frames(input_folder, output_folder, fps_target=1):
    # Garante que a pasta de saída (e a subpasta 'images') exista
    images_output = os.path.join(output_folder, 'images')
    os.makedirs(images_output, exist_ok=True)

    # Busca todos os vídeos mp4 na pasta
    video_files = glob.glob(os.path.join(input_folder, '*.mp4'))

    for video_file in video_files:
        video_name = os.path.basename(video_file).split('.')[0]
        cap = cv2.VideoCapture(video_file)

        # Captura o FPS original do vídeo
        original_fps = cap.get(cv2.CAP_PROP_FPS)
        if original_fps == 0:
            continue
            
        # Calcula de quantos em quantos frames devemos salvar para ter 1 frame por segundo
        frame_interval = int(round(original_fps / fps_target))

        count = 0
        saved_count = 0

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Salva o frame se for o intervalo correto
            if count % frame_interval == 0:
                frame_name = f"{video_name}_frame_{saved_count:04d}.jpg"
                frame_path = os.path.join(images_output, frame_name)
                cv2.imwrite(frame_path, frame)
                saved_count += 1

            count += 1

        cap.release()
        print(f"Extraídos {saved_count} frames do vídeo {video_name}")

# Caminho raiz onde estão as pastas atuais (train, val, test) com os mp4
# base_input_dir = './videos' 
base_input_dir = 'C:/Users/Administrador/Documents/FIAP/Fase 4/GynSurg/Modulo/videos' 

# Verificando se o diretório contendo os vídeos foi localizado
if not os.path.exists(base_input_dir):
    print(f"ERRO: A pasta {base_input_dir} não foi encontrada.")
else:
    print(f"Pasta encontrada. Verificando conteúdo em: {os.path.abspath(base_input_dir)}")

# Caminho onde a estrutura do YOLO será gerada
base_output_dir = './dataset_yolo' 

splits = ['train', 'val', 'test']

for split in splits:
    input_dir = os.path.join(base_input_dir, split)
    output_dir = os.path.join(base_output_dir, split)
    print(f"Processando pasta: {split}...")
    extract_frames(input_dir, output_dir, fps_target=1)