

def getSubjects():
  subjects = []
  with open("subjects.txt", "r") as file:
    for subject in file:
      subjects.append(subject.strip())
    
  return sorted(subjects)


def filterSubjects(user, subjects):
  print("filtering...")
  print(user)
  with open("users.txt", "r") as file:
    for line in file:
      if user.lower() in line:
        userDetails = line.split()[1:]
        subjects = [subject for subject in subjects if userDetails[0] in subject]
        print(subjects)
        break

  return subjects