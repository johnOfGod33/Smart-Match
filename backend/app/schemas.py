from enum import Enum

class Job_offer_type(str,Enum):
  internship = "internship"
  full_time = "full_time"
  part_time = "part_time"
  freelance = "freelance"
  volunteer = "volunteer"
