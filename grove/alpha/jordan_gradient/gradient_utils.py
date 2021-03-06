import numpy as np

def real_to_binary(number, precision=16):
    """ Convert real decimal to precision-bit binary fraction
    
    :param float number: Real decimal over [0, 1).
    :param int precision: Number of bits of binary precision.
    :return float bf: Binary fraction representation of real decimal.
    """

    n_sign = np.sign(number)
    number = abs(number)
    number = round(number, precision+2)
    bf = ''
    for val in range(precision):
        number *= 2
        frac, whole = np.modf(number)
        bf += str(int(whole))
        number = frac
    bf = float(n_sign * float('.' + bf))
    
    return bf

def binary_to_real(number):
    """ Convert binary fraction to real decimal
    
    :param float number: Floating point representation of binary fraction.
    :return float deci: Real decimal representation of binary fraction.
    """    
   
    if isinstance(number, str):
        if number[0] == '-':
            n_sign = -1
        else:
            n_sign = 1
    elif isinstance(number, float):
        n_sign = np.sign(number)

    deci = 0
    for ndx, val in enumerate(str(number).split('.')[-1]):
        deci += float(val) / 2**(ndx+1)
    deci *= n_sign
        
    return deci

def measurements_to_bf(measurements):
    """ Convert measurements into gradient binary fraction
    
    :param list measurements: Output measurements of gradient program.
    :return float bf: Binary fraction representation of gradient estimate.
    """

    measurements = np.array(measurements)
    stats = measurements.sum(axis=0) / len(measurements)
    stats_str = [str(int(i)) for i in np.round(stats[::-1][1:])]
    bf_str = '0.' + ''.join(stats_str)
    bf = float(bf_str)
    
    return bf
