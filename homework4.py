from math import sqrt


# Написать скрипт для расчета корреляции Пирсона между
# двумя случайными величинами (двумя массивами).
def correlation_calculation(x, y):
    m_x = sum(x)/len(x)
    m_y = sum(y)/len(y)

    def product_differences(xi, yi):
        return (xi - m_x)*(yi - m_y)

    numerator = sum(map(product_differences, x, y))
    denominator = sqrt(
        sum(
            (xi - m_x) ** 2 for xi in x
        ) * sum(
            (yi - m_y)**2 for yi in y
        )
    )
    return numerator/denominator


if __name__ == '__main__':
    array_x = [1, 2, 3]
    array_y = [10, 20, 29]
    print(
        'Коэффициент Пирсона: ' +
        '{:.5f}'.format(correlation_calculation(array_x, array_y))
    )

