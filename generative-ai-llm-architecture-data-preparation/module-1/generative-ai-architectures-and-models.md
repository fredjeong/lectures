RNNs: sequential or time series data (natural order or time-dependency)
- loop-based design for training
- fine-tuning 중요
- nlp
- language translation
- speech recognition
- image captioning

Transformers
- real-time
- fine-tuning: output layer만 튜닝
- uses self-attention mechanism to focus on the most important parts of the information

GANs
- generator, discriminator로 이루어짐
- generator는 가짜 샘플을 생성하여 판별자에게 보내고, 판별자는 이를 실제 샘플과 비교하여 샘플이 진짜일 가능성을 점수로 매김
- 이러한 경쟁 과정을 통해 결과 개선
- 이미지 및 비디오 생성에 효과적

VAEs
- 인코더: 입력 데이터를 추상 공간에 압축
- 디코더: 압축된 정보를 이용해 재생성
- 중요한 패턴을 기억하므로 유사한 특성을 고융하는 새로운 데이터 샘플을 만들 수 있음

Diffusion models
- 노이즈를 제거하거나 왜곡된 샘플을 재구성하는 방법을 학습하여 이미지를 생성하도록 훈련
- 저화질 이미지에서 고품질 이미지를 생성할 수 있음

이러한 생성형 AI 모델은 강화학습과 연관성이 있음
훈련 중 강화 학습 기법을 사용해 특정 작업에 맞게 성능을 미세 조정하고 최적화할 수 있다