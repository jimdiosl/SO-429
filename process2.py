import os
 
# Running the aforementioned command and saving its output
output = os.popen('wmic process get description, processid').read()
 
# Displaying the output
print(output)