import pandas as pd
import xlsxwriter


class SeatAllotment:
    def __init__(self, studentProfile: list, collegeData: list):
        """
        :param studentProfile: list of dict
        :param collegeData:     list of dict

        Format:
         studentProfile =  [

            {
                "StudentID": id,
                "StudentName": "name",
                "meritMarks": marks,
                "caste": "open/sc/st/obc",
                "collegeChoice": ['college1', 'college2'...],
                "studentEmail": "email",
                "studentPhone": phoneNumber
            },

         ]

         collegeData = [

            {
                "collegeFullName": "name",
                "collegeCode": code,
                "branchOffered": ["b1", "b2"],
                "seatsAvailable": [seats, seats]
                "openSeats": ,
                "otherSeats":

            },
         ]
        """
        self.studentProfile = studentProfile
        self.collegeData = collegeData

    def genMeritList(self):

        if self.studentProfile is None:
            print("PLease enter Student profile list first.")
            return
        else:
            for i in range(len(self.studentProfile) - 1):
                for j in range(len(self.studentProfile) - 1):
                    if self.studentProfile[i]["meritMarks"] < self.studentProfile[i + 1]["meritMarks"]:
                        swap = self.studentProfile[i]
                        self.studentProfile[i] = self.studentProfile[i + 1]
                        self.studentProfile[i + 1] = swap

    def exportMeritList(self, fileName: str):
        fileName = fileName + ".xlsx"
        df = pd.DataFrame(self.studentProfile)
        wb = xlsxwriter.Workbook(fileName)
        ws = wb.add_worksheet("Merit List")
        wb.close()
        df.to_excel(fileName)

    def allotSeat(self):
        seatAlloted = []
        # Merit wise check students cast.
        for i in range(len(self.studentProfile)):
            for j in range(len(self.studentProfile[i]["collegeChoice"])):
                for k in range(len(self.collegeData)):
                    if self.studentProfile[i]["collegeChoice"][j] == self.collegeData[k]["collegeFullName"]:
                        branch = self.studentProfile[i]["branch"]
                        inx = None
                        for x in range(len(self.collegeData[k]["branchOffered"])):
                            if branch ==    self.collegeData[k]["branchOffered"][x]:
                                inx = x
                                x += 1
                                break
                            else:
                                x += 1

                        if self.studentProfile[i]["caste"] == "open":
                            if self.collegeData[k]["openSeats"][inx] > 0:
                                self.collegeData[k]["openSeats"][inx] -= 1
                                seatAlloted.append({

                                    "StudentID": self.studentProfile[i]["StudentID"],
                                    "CollegeAlloted": self.collegeData[k]["collegeFullName"],
                                    "SeatType": "open"
                                })
                                break  # Seat alloted
                        else:
                            if self.studentProfile[i]["caste"] == "other":
                                if self.collegeData[k]["otherSeats"][inx] > 0:
                                    self.collegeData[k]["otherSeats"][inx] -= 1
                                    seatAlloted.append({

                                        "StudentID": self.studentProfile[i]["StudentID"],
                                        "CollegeAlloted": self.collegeData[k]["collegeFullName"],
                                        "SeatType": "other"
                                    })
                                    break  # Seat alloted

                    else:
                        k += 1
                j += 1

            i += 1

        print(seatAlloted)


studentProfile = [

    {
        "StudentID": 1,
        "StudentName": "Azim Baldiwala",
        "meritMarks": 19,
        "caste": "open",
        "collegeChoice": ['LJ University', 'nirma'],
        "studentEmail": "azim@gmail.com",
        "studentPhone": 179126511,
        "branch": "cs"

    },

    {
        "StudentID": 2,
        "StudentName": "Ali",
        "meritMarks": 19.2,
        "caste": "open",
        "collegeChoice": ['nirma'],
        "studentEmail": "ali@gmail.com",
        "studentPhone": 179126511,
        "branch": "cs"

    },

    {
        "StudentID": 3,
        "StudentName": "x",
        "meritMarks": 18,
        "caste": "open",
        "collegeChoice": ['nirma'],
        "studentEmail": "x@gmail.com",
        "studentPhone": 179126511,
        "branch": "cs"

    },

]

collegeData = [

    {
        "collegeFullName": "nirma",
        "collegeCode": 1,
        "branchOffered": ["cs", "me"],
        "seatsAvailable": [2, 60],
        "openSeats": [2, 55],
        "otherSeats": [0, 5]

    },

    {
        "collegeFullName": "LJ University",
        "collegeCode": 2,
        "branchOffered": ["cs", "me"],
        "seatsAvailable": [10, 60],
        "openSeats": [0, 10],
        "otherSeats": [50, 10]

    },

]

x = SeatAllotment(studentProfile, collegeData)
x.genMeritList()
x.exportMeritList('merit')
x.allotSeat()
