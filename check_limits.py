
def battery_is_ok(temperature, soc, charge_rate):
  
  if(temp_soc_is_okay(temperature,soc) and charge_rate_is_okay(charge_rate)):
    return True

  return False

def temp_soc_is_okay(temperature,soc):
  
  if (temperature < 0 and soc < 20) or (temperature <0 and soc > 80 ) or (temperature > 45 and soc < 20) or (temperature >45 and soc > 80 ):
    print('Temperature or soc is out of range!')
    return False
  
  return True

# def soc_is_okay(soc):
#   if soc < 20 or soc > 80:
#     print('State of Charge is out of range!')
#     return False
#   return True

def charge_rate_is_okay(charge_rate):
  
  if charge_rate > 0.8:
    print('Charge rate is out of range!')
    return False
  
  return True

if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
 
