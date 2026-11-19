"""Intentionally buggy legacy checkout exercise. Do not fix in the baseline."""

def checkout(subtotal, shipping, discount_percent):
    if subtotal < 0 or shipping < 0:
        raise ValueError('Amounts must be nonnegative')
    if not 0 <= discount_percent <= 100:
        raise ValueError('Discount must be between 0 and 100')
    # Legacy bug: discount accidentally applies to shipping too.
    total = (subtotal + shipping) * (1 - discount_percent / 100)
    # Legacy bug: mysterious adjustment can make tiny orders negative.
    if subtotal < 1:
        total -= 5
    return round(total, 2)
