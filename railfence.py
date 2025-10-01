def rail_fence_encrypt(text, rails):
    fence = [['' for _ in range(len(text))] for _ in range(rails)]
    row, step = 0, 1

    # 지그재그로 문자 배치
    for col, char in enumerate(text):
        fence[row][col] = char
        if row == 0:
            step = 1
        elif row == rails - 1:
            step = -1
        row += step

    # 행 단위로 읽어서 암호문 생성
    encrypted = ''.join(''.join(r) for r in fence)
    return encrypted


def rail_fence_decrypt(cipher, rails):
    # 빈 격자 만들기
    fence = [['' for _ in range(len(cipher))] for _ in range(rails)]
    row, step = 0, 1

    # 경로 표시용
    for col in range(len(cipher)):
        fence[row][col] = '*'
        if row == 0:
            step = 1
        elif row == rails - 1:
            step = -1
        row += step

    # 암호문 채워넣기
    idx = 0
    for r in range(rails):
        for c in range(len(cipher)):
            if fence[r][c] == '*' and idx < len(cipher):
                fence[r][c] = cipher[idx]
                idx += 1

    # 경로 따라 평문 읽기
    row, step = 0, 1
    result = []
    for col in range(len(cipher)):
        result.append(fence[row][col])
        if row == 0:
            step = 1
        elif row == rails - 1:
            step = -1
        row += step

    return ''.join(result)


# 실행 예제
plain_text = "HELLOWORLD"
rails = 3

cipher_text = rail_fence_encrypt(plain_text, rails)
decrypted_text = rail_fence_decrypt(cipher_text, rails)

print("평문 :", plain_text)
print("암호문:", cipher_text)
print("복호문:", decrypted_text)