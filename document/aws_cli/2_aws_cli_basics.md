# AWS CLI examples

## AWS CLI 개요
- 사용자가 GUI 환경이 아닌 콘솔에서 CLI 명령어로 AWS의 기능을 제어할 수 있는 환경
- 일반적으로 클라우드 기반의 서버 환경을 구축할 때 가장 일반적으로 사용되고 있음


## 기본 명령어들
### VPC
- 보안그룹의 기본 정보를 보기 위한 명령
```bash
aws ec2 describe-vpcs
```
![보안그룹 GUI 사진 예시](./images/vpc_1.png)

- 보안그룹의 생성을 위한 명령어 [reference](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-security-group.html)
```bash
aws ec2 create-security-group \
--group-name HelloWorld \
--description "Hello World Demo" \
--vpc-id YOUR_VPC_ID
```
![새로생성된 보안 그룹](./images/vpc_2.png)

- 보안그룹에 IN/OUT bound 설정하기 [reference](https://docs.aws.amazon.com/cli/latest/reference/ec2/authorize-security-group-ingress.html)

```bash
aws ec2 authorize-security-group-ingress \
  --group-name HelloWorld \
  --protocol tcp \
  --port 22 \
  --cidr 0.0.0.0/0
```
![IN/OUT 바운드 설정](./images/vpc_3.png)

- 보안그룹 설정 정보 확인하기 [reference](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-security-groups.html)
```bash
aws ec2 describe-security-groups \
 --group-names HelloWorld \
 --output table
```
