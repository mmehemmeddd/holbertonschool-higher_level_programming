#!/usr/bin/python3
"""Paskal üçbucağı modulu."""


def pascal_triangle(n):
    """n ölçülü Paskal üçbucağını siyahılar siyahısı kimi qaytarır."""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # Həmişə 1 ilə başlayır

        for j in range(1, i):
            # Yeni rəqəm = üst sətirdəki eyni indeksli + ondan əvvəlki indeksli
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)  # Həmişə 1 ilə bitir
        triangle.append(new_row)

    return triangle
