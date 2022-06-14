def Knapsack(pubkey: list, target: int) -> bytes:
    # Credit to VincBreaker
    a = pubkey
    s = target
    n = len(a)
    k = ceil(sqrt(n) / 2)

    mat = []
    for i in range(n):
        row = [0 for _ in range(n + 1)]
        row[i] = 1
        row[-1] = k * a[i]
        mat.append(row)
    mat.append([1 / 2 for _ in range(n)] + [k * s])
    mat = matrix(QQ, mat)

    sol = mat.LLL()
    for e in sol:
        if e[-1] == 0:
            msg = 0
            isValidMsg = True
            for i in range(len(e) - 1):
                ei = 1 - (e[i] + (1 / 2))
                if ei != 1 and ei != 0:
                    isValidMsg = False
                    break
                msg |= int(ei) << i
            if isValidMsg:
                msg = bytes.fromhex(hex(msg)[2:])
                return msg
