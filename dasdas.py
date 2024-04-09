# n, k = map(int, input().split())
# arr = []
# for _ in range(n):
#     arr.append(int(input()))
# arr = sorted(arr, reverse=True)

# result = 0
# i = 0
# while k > 0:
#     result += k // arr[i]
#     k = k % arr[i]
#     i += 1

# print(result)
users = {
    'user1': 'password1',
    'user2': 'password2',
    'user3': 'password3'
}

def login(username, password):
    if username in users and users[username] == password:
        return True
    else:
        return False
    
# 로그인 테스트
username = input("사용자 이름을 입력하세요: ")
password = input("비밀번호를 입력하세요: ")

if login(username, password):
    print("로그인 성공!")
else:
    print("로그인 실패. 사용자 이름 또는 비밀번호를 확인하세요.")
