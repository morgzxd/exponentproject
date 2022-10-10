from time import perf_counter

def expt(x, n):
    if n < 0:
        raise ValueError("n = {} is less than 0".format(n))

    if n == 0:
        return 1

    elif n % 2 == 0:
        result = expt(x, n // 2)
        return result * result

    else:
        return x * expt(x, n - 1)


def older_expt(x, n):
    if n < 0:
        raise ValueError('n = {} is less than zero'.format(n))

    result = 1
    for _ in range(n):
        result *= n

    return result


def old_expt(x, n):
    if n < 0:
        raise ValueError("n = {} is less than 0".format(n))
    elif n == 0:
        return 1
    else:
        return x * old_expt(x, n - 1)


def main():

    f = open("expt_data.csv", "w")
    f.write("exponent,min_runtime_new,min_runtime_old,\n")

    for i in range(1, 10000):
        old_min = 10
        new_min = 10

        for _ in range(10):
            runtime_new = perf_counter()
            expt(17, i)
            runtime_new = perf_counter() - runtime_new
            if runtime_new < new_min:
                new_min = runtime_new

            runtime_old = perf_counter()
            older_expt(17, i)
            runtime_old = perf_counter() - runtime_old
            if runtime_old < old_min:
                old_min = runtime_old
        print(f"Writing results for exponent {i}")
        f.write(f"{i},{new_min},{old_min}\n")
    f.close()


if __name__ == '__main__':
    main()
