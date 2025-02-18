# 코사인 유사도를 이용한 최종 코드

import torch
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image
import os
import torch.nn.functional as F
import numpy as np

# GPU 사용 여부 확인
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 사전 학습된 ResNet-18 불러오기
model = models.resnet18(pretrained=True)

# 마지막 fc 레이어를 제거하여 특징 추출만 하도록 설정
model = torch.nn.Sequential(*list(model.children())[:-1])  # 마지막 fc 레이어 제외
model = model.to(device)
model.eval()  # 평가 모드 설정

# 이미지 전처리 함수 (ResNet-18에 맞게 크기 조정 및 정규화)
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # ResNet-18 입력 크기
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# 특징 벡터 추출 함수
def extract_feature_vector(image_path):
    """이미지에서 특징 벡터 추출"""
    image = Image.open(image_path).convert("RGB")
    image = transform(image).unsqueeze(0).to(device)
    
    with torch.no_grad():
        feature_vector = model(image)  # 마지막 fc 레이어를 제외한 모델에서 특징 추출
        feature_vector = feature_vector.view(feature_vector.size(0), -1)  # 평탄화
    return feature_vector

# 코사인 유사도 계산 함수
def cosine_similarity(v1, v2):
    """두 벡터 간의 코사인 유사도 계산"""
    v1 = v1.squeeze()  # (batch_size, features) -> (features)
    v2 = v2.squeeze()  # (batch_size, features) -> (features)
    return F.cosine_similarity(v1, v2, dim=0).item()

# 특징 벡터가 저장된 .pt 파일 로드하기
def load_feature_vectors(feature_folder):
    """저장된 .pt 파일에서 특징 벡터들 로드"""
    feature_vectors = {}
    for file_name in os.listdir(feature_folder):
        if file_name.endswith('.pt'):
            file_path = os.path.join(feature_folder, file_name)
            feature_vectors[file_name] = torch.load(file_path).to(device)  # .pt 파일 로드
    return feature_vectors

# 지역 정보를 담고 있는 텍스트 파일에서 이미지 이름과 지역명 읽기
def load_image_locations(location_file):
    """지역 정보가 저장된 텍스트 파일에서 이미지 이름과 지역 정보를 로드"""
    image_locations = {}
    with open(location_file, 'r', encoding='utf-8') as f:
        for line in f:
            # 공백을 제거하고 쉼표로 나누기
            parts = line.strip().split(',')
            if len(parts) == 2:  # 이미지 이름과 지역 정보가 정확히 2개일 경우
                image_name, location = parts
                image_locations[image_name] = location
            else:
                print(f"이 줄에서 문제 발생: {line.strip()}")  # 디버깅용 출력
    return image_locations

# 주어진 폴더에서 이미지들의 특징 벡터 추출 후 유사도 계산
def find_most_similar_images(query_image_path, feature_folder, location_file, top_n=3):
    """입력 이미지와 특징 벡터 폴더 내에서 가장 유사한 이미지 찾기 (상위 n개)"""
    query_feature = extract_feature_vector(query_image_path)
    
    feature_vectors = load_feature_vectors(feature_folder)  # 특징 벡터들 로드
    image_locations = load_image_locations(location_file)  # 지역 정보 로드
    
    similarities = []
    
    for image_name, db_feature in feature_vectors.items():
        similarity = cosine_similarity(query_feature, db_feature)
        similarities.append((image_name, similarity))
    
    # 유사도가 높은 순으로 정렬
    similarities.sort(key=lambda x: x[1], reverse=True)
    
    # 상위 top_n 개의 이미지들 찾기
    similar_images = []
    for idx, (image_name, similarity) in enumerate(similarities[:top_n]):
        location = image_locations.get(image_name, "지역 정보 없음")  # 이미지에 해당하는 지역 정보 가져오기
        similar_images.append((image_name, location, similarity))
    
    return similar_images

# 테스트 예시
query_image_path = r"C:\Users\wq188\Pictures\Screenshots\스크린샷 2025-02-18 220413.png"  # 예시 이미지
feature_folder = r"C:\Users\wq188\Desktop\image\features"  # 특징 벡터 폴더 경로
location_file = r"C:\Users\wq188\Desktop\이미지 지역 정보.txt"  # 지역 정보가 저장된 파일

# 상위 3개의 가장 유사한 이미지 찾기
most_similar_images = find_most_similar_images(query_image_path, feature_folder, location_file, top_n=3)

# # 결과 출력
# for idx, (image_name, location, similarity) in enumerate(most_similar_images):
#     # '.pt' 확장자 제거
#     image_name = image_name.replace('.pt', '')  
#     print(f"Rank {idx + 1}: {image_name}, 지역: {location}, 유사도: {similarity}")

if __name__ == '__main__':
    # 테스트용 예시
    query_image_path = r"C:\Users\wq188\Pictures\Screenshots\스크린샷 2025-02-18 220413.png"
    feature_folder = r"C:\Users\wq188\Desktop\image\features"
    location_file = r"C:\Users\wq188\Desktop\이미지 지역 정보.txt"
    similar_images = find_most_similar_images(query_image_path, feature_folder, location_file, top_n=3)
    for idx, (image_name, location, similarity) in enumerate(similar_images):
        print(f"Rank {idx+1}: {image_name}, 지역: {location}, 유사도: {similarity}")
