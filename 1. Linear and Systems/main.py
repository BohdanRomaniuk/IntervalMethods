from interval import interval, inf, imath
import math

def liniar_half(start, end, e):
    print('-----Iteration for [', start, ', ', end, ']')
    check = end - start
    if check <= e:
        print('FOUND X =', start, ' ', end)
        return
    X0 = interval([start, end])
    f = X0 ** 3 - 6 * X0 ** 2 + 11 * X0 - 6
    print('F: ', f)

    mid = (start + end) / 2;
    if 0 in f:
        liniar_half(start, mid, e)
        liniar_half(mid, end, e)
        return

print("Лінійний алгоритм навпіл");
print("x^3 - 6*x^2 + 11*x - 6 = 0");
print("1, 2, 3");
print("[0; 6]");
print("------------");
x1 = 1;
x2 = 2;
x3 = 3;
e = 10 ** (-2)

a = 0;
b = 6;

liniar_half(a, b, e)

def liniar_mura(start, end, e):
    print('-----Iteration for [', start, ', ', end, '] ----------')
    check = end - start
    if check < e:
        print('FOUND X =', start, ' ', end)
        return
    X0 = interval([start, end])
    mid = (start + end) / 2;
    f = mid ** 3 - 3 * mid + 2
    if f == 0.0:
        liniar_mura(start, mid, e)
        liniar_mura(mid, end, e)
        return
    print('function value:', f);
    print('middle: ', end - start)
    f_derivative = 3 * X0 * X0 - 3

    U = mid - f / f_derivative
    X1 = U & X0
    [liniar_mura(x.inf, x.sup, e) for x in X1]

print("Лінійний алгоритм Мура");
print("x^3 - 6*x^2 + 11*x - 6 = 0");
print("1, 2, 3");
print("[0; 6]");
print("------------");
x1 = 1;
x2 = 2;
x3 = 3;
e = 10**(-6)

a = -2;
b = 1;

liniar_mura(a, b, e)


def liniar_hansen(start, end, e):
    print('-----Iteration for [', start, ', ', end, '] ----------')
    check = end - start
    X0 = interval([start, end])
    if check < e:
        print('FOUND X =', start, ' ', end)
        return;

    mid = (start + end) / 2;
    f = mid ** 3 - 6 * mid ** 2 + 11 * mid - 6

    print('function value:', f);
    F_derivative = 3 * X0 * X0 - 12 * X0 + 11

    temp = [x for x in F_derivative]
    c = temp[0].inf
    d = temp[0].sup
    print("c: ", c)
    print("d: ", d)

    if 0 not in F_derivative:
        print('Stop. F_derivative does not have 0')
        print("X0: ", X0)
        return;

    if f == 0.0:
        print('FOUND X =', start, ' ', end)
        liniar_hansen(start, mid, e)
        liniar_hansen(mid, end, e)
        return
    elif f > 0.0:
        if c == 0.0:
            q = mid - f / d
            U = interval([-math.inf, q])
        elif d == 0.0:
            p = mid - f / c
            U = interval([p, math.inf])
        elif c < 0.0 and 0.0 < d:
            q = mid - f / d
            p = mid - f / c
            U = interval([-math.inf, q]) | interval([p, math.inf])
    elif f < 0.0:
        if c == 0.0:
            q = mid - f / d
            U = interval([q, math.inf])
        elif d == 0.0:
            p = mid - f / c
            U = interval([-math.inf, p])
        elif c < 0.0 and 0.0 < d:
            q = mid - f / d
            p = mid - f / c
            U = interval([-math.inf, p]) | interval([q, math.inf])

    X1 = U & X0
    print('X0: ', X0);
    print('U: ', U);
    print('X1: ', X1);

    result = list(map(lambda x: liniar_hansen(x.inf, x.sup, e), X1))
    return


print("Лінійний алгоритм Хансена");
print("x^3 - 6*x^2 + 11*x - 6 = 0");
print("1, 2, 3");
print("[0; 4]");
print("------------");
x1 = 1;
x2 = 2;
x3 = 3;
e = 10 ** (-2)

a = 0;
b = 4;

liniar_hansen(a, b, e)


def liniar_krafchyk(start, end, e):
    print('-----Iteration for [', start, ', ', end, '] ----------')
    global i
    global i_dividebytwo
    i = i + 1

    X0 = interval([start, end])
    mid = (start + end) / 2;

    f = mid ** 3 - 3 * mid + 2
    print('f: ', f)
    print('width: ', end - start)

    fX0 = X0 * X0 * X0 - 3 * X0 + 2

    f_derivative = 3 * mid ** 2 - 3
    F_derivative = 3 * X0 * X0 - 3

    check = end - start
    if check < e:
        print('FOUND X =', start, ' ', end)
        return

    if 0 in F_derivative:
        # print('0 in F_derivative')
        if mid - start > e:
            liniar_krafchyk(start, mid, e)
            liniar_krafchyk(mid, end, e)
            i_dividebytwo = i_dividebytwo + 1
        return

    U = mid - f / f_derivative + (1 - (F_derivative) / f_derivative) * (X0 - mid)

    X1 = U & X0
    print('X0: ', X0);
    # print('U: ', U);
    # print('X1: ', X1);

    if X0 == X1:
        # print('X0 == X1')
        liniar_krafchyk(start, mid, e)
        liniar_krafchyk(mid, end, e)
        i_dividebytwo = i_dividebytwo + 1
        return

    [liniar_krafchyk(x.inf, x.sup, e) for x in X1]


print("Лінійний алгоритм Крафчика");
print("x^3 - 6*x^2 + 11*x - 6 = 0");
print("1, 2, 3");
x1 = 1;
x2 = 2;
x3 = 3;
e = 10 ** (-6)

a = -2.5;
b = -1.25;

print('[', a, ';', b, ']');
print("------------");

i = 0
i_dividebytwo = 0

liniar_krafchyk(a, b, e)

print("------------");
print('Iterations: ', i)
print('Iterations (divide by two): ', i_dividebytwo)