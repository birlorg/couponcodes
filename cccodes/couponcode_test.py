from .coupon import validate, generate, normalize


def test_check_digit():
	assert validate('T13P-2LMP-E0B5') is True
	assert validate('HA0B-R1W6-76JH') is True
	assert validate('5QMU-M10M-VE0D') is True
	assert validate('FLY6-9A0E-NFHN') is True
	assert validate('DQV8-YAL9-RW4R') is True
	assert validate('POOP-TOOT-HAPS') is False

def test_normalize():
	assert normalize('tI3P-SLMP-E0B5') == 'T13P-5LMP-E0B5'
