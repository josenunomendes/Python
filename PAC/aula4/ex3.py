# This program generates 20 terms of a sequence by a recurrence relation.
Un = 100                    # Un = each term of the sequence. Initially = U0
count = 0                   # count = number of terms generated
while Un > 0:            # While Un is less than 1000
    print(Un)
    Un = 1.01*Un - 1.01     # Set Un to the next term of the sequence
    count += 1              # Increment the count of terms generated

print("Number of terms generated:", count)