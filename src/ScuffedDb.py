from datetime import datetime

class DB():
  def __init__(self, type):
    self.fileName = "db.txt"
    if type == "exam":
      self.fileName = "exam-db.txt"

  def getLargest(self, data):
    largest = 0
    for item in data:
      if int(data[-1].split()[0]) > largest:
        largest = int(data[-1].split()[0])
    return largest
  
  def add(self, entry):
    with open(self.fileName, "r") as file:
      data = file.readlines()
      entry = str(self.getLargest(data)+1) + " &| " + entry
    
    if not ["Yes" for item in data if entry[entry.index("&|"):].replace("&|", "").replace(" ", "")  in item.replace("&|", "").replace(" ", "")]:
            
      try:
        with open(self.fileName, "a") as file:
          file.write(entry)
  
      except Exception:
        print("COULDNT WRITE AND OPEN TO DB")

  
  def grab(self):
    with open(self.fileName, "r") as file:
      return file.readlines()

  
  def remove(self, index):
    with open(self.fileName, "r") as file:
      data = [item for item in file.readlines() if int(item.split("&|")[0]) != int(index)]

    with open(self.fileName, "w") as file:
      for item in data:
        if len(item) > 1:
          file.write(item)


  
  def update(self):
    with open(self.fileName, "r") as file:
      try:
        data = {entry.replace(entry.split()[-1], ""): int(entry.split()[-1].replace("-","")) for entry in file.readlines() }
      except ValueError:
        return

    now = int(datetime.now().strftime("%Y%m%d"))
    data = dict(sorted(data.items(), key=lambda item: item[1]))
    data = {key: value for key, value in data.items() if value >= now }

    with open(self.fileName, "w") as file:
      for value, date in data.items():
        if len(value) > 1:
          dateString = str(date)[:4] + "-" + str(date)[4:6] + "-" + str(date)[6:]
          file.write(value.replace("\n", "") + dateString + "\n")
      