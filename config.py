from datetime import datetime, timedelta
import random

first_name = 'Raisin'
first_name_space = 'Raisin '
first_name_second_user = 'Bruce'
first_name_capital_letters = 'RAISIN'
last_name = 'McGee'
last_name_space = 'McGee '
last_name_second_user = 'Almighty'
last_name_capital_letters = 'MCGEE'
zip_code = '94102'
zip_code_space = '94102 '
zip_code_invalid = '93013'
employee_id = 'R123456'
employee_id_space = 'R123456 '
employee_id_second_user = 'R234567'
employee_id_small_letter = 'r123456'
#need update
date_of_birth = '01/02/1980'
#need update
date_of_birth_failed = '01/03/1980'
#need update
date_of_birth_second_eser = '05/23/2007'
#need update
date_of_birth_second_eser_failed = '05/24/2007'
date_of_birth_not_eligible = '05/20/1985'

first_name_under13 = 'Smokey'
last_name_under13 = 'Bear'
#need update
date_of_birth_under13 = '06/30/2016'
#need update
date_of_birth_under13_failed = '07/01/2016'
employee_id_under13 = 'R456789'
zip_code_under13 = '92039'


first_name_under18 = 'Richard'
last_name_under18 = 'Scarry'
#need update
date_of_birth_under18 = '12/12/2007'
#need update
date_of_birth_under18_failed = '12/13/2007'
employee_id_under18 = 'R123455'
zip_code_under18 = '20394'

street_address = 'Миroвачка ÅÆØ'
city = 'Belgrade'
state = 'Alabama'
phone_number = '+381652000000'
email = 'nikolaradovic1985+testdelete2512231@gmail.com'
existed_email = 'nikolaradovic1985+testdelete0502241@gmail.com'

# new user email
today = datetime.now()
formatted_day = today.strftime('%d%m%y_%H%M%S')
counter = random.randint(21, 100)
new_user_email = f'nikolaradovic1985+testdelete{formatted_day}{counter}@gmail.com'