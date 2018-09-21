## Setup AWS CLI on windows

#### 1. 가상환경 만들기
- AWS CLI와 boto3를 사용하기 위한 파이썬 가상환경을 설정함

```bash
conda create -n big_data python=3.6
activate big_data
```

#### 2. boto3 설치
```bash
pip install boto3
```

#### 3. AWS CLI 설치
```bash
pip install awscli
```
- 참고 - https://aws.amazon.com/ko/cli/

#### 4. Key access 설정
- AWS CLI와 boto3를 자신의 PC에서 설정하기 위한 key access를 다운로드 함
- IAM 서비스 선택

![](s3_boto3_setup/1.PNG)

![](s3_boto3_setup/2.PNG)

- 사용자 추가
![](s3_boto3_setup/3.PNG)
- 사용자 세부 정보 입력
![](s3_boto3_setup/4.PNG)
- 정책정보 입력
![](s3_boto3_setup/5.PNG)
![](s3_boto3_setup/6.PNG)
- Key access 정보 다운로드 하기(보안유의)
![](s3_boto3_setup/7.PNG)

#### 5. AWS configure
- AWS를 본인의 컴퓨터에서 사용할 수 있도록 정보를 설정함
```bash
aws configure # write your AWS key access information
```
![](s3_boto3_setup/8.PNG)

- 자신의 홈 디렉토리에 `.aws` 파일 생성 여부 확인
![](s3_boto3_setup/9.PNG)


#### 6. S3 Cehck
```python
import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)
```
