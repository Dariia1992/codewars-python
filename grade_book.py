"""
Complete the function so that it finds the average of
the three scores passed to it and returns the letter value associated with that grade.
"""
def get_grade(s1, s2, s3):
   grades = (s1 + s2 +s3) / 3
   if grades >= 90:
    return "A"
   elif grades >= 80:
    return "B"
   elif grades >= 70:
    return "C"
   elif grades >= 60:
    return "D"
   else:
    return "F"
