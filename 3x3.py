import random

class Cube3x3:
    def __init__(self, front: str = "W", top: str = "R") -> None:
        self.cube = ["W", "W", "W", "W", "W", "W", "W", "W", "W",
                     "B", "B", "B", "B", "B", "B", "B", "B", "B",
                     "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y",
                     "G", "G", "G", "G", "G", "G", "G", "G", "G",
                     "R", "R", "R", "R", "R", "R", "R", "R", "R",
                     "O", "O", "O", "O", "O", "O", "O", "O", "O"]
                     
        while((self.cube[4] != front) & (self.cube[4] != top)):
            self.__rotateCube("Y")
        
        if(self.cube[4] == top):
            self.__rotateCube("X")
            while(self.cube[4] != front):
                self.__rotateCube("Y")
        else:
            while(self.cube[40] != top):
                self.__rotateCube("Z")
        

    def __str__(self) -> str:
        return f"""
    +---------+
   / {self.cube[36]}  {self.cube[37]}  {self.cube[38]} /|
  / {self.cube[39]}  {self.cube[40]}  {self.cube[41]} / |
 / {self.cube[42]}  {self.cube[43]}  {self.cube[44]} / {self.cube[29]}|
+---------+ {self.cube[28]}{self.cube[32]}|
| {self.cube[0]}  {self.cube[1]}  {self.cube[2]} |{self.cube[27]}{self.cube[31]}{self.cube[35]}|
| {self.cube[3]}  {self.cube[4]}  {self.cube[5]} |{self.cube[30]}{self.cube[34]} +
| {self.cube[6]}  {self.cube[7]}  {self.cube[8]} |{self.cube[33]}/
+---------+

+---------+
| {self.cube[18]}  {self.cube[19]}  {self.cube[20]} |{self.cube[9]}\\
| {self.cube[21]}  {self.cube[22]}  {self.cube[23]} |{self.cube[12]} \\
| {self.cube[24]}  {self.cube[25]}  {self.cube[26]} |{self.cube[15]} {self.cube[10]}\\
+---------+  {self.cube[13]} +
 \ {self.cube[51]}  {self.cube[52]}  {self.cube[53]} \ {self.cube[16]}{self.cube[11]}|
  \ {self.cube[48]}  {self.cube[49]}  {self.cube[50]} \ {self.cube[14]}|
   \\ {self.cube[45]}  {self.cube[46]}  {self.cube[47]} \{self.cube[17]}|
    +---------+
        """

    def __spinFace(self, face: str, clockwise: bool) -> None:
        match face:
            case "F":
                center = 4
            case "L":
                center = 13
            case "B":
                center = 22
            case "R":
                center = 31
            case "U":
                center = 40
            case "D":
                center = 49
            case _:
                return
        
        if(clockwise):
            temp1, temp2, temp3 = self.cube[center - 2], self.cube[center - 3], self.cube[center - 4]
            self.cube[center - 2], self.cube[center - 3], self.cube[center - 4] = self.cube[center - 4], self.cube[center - 1], self.cube[center + 2]
            self.cube[center - 4], self.cube[center - 1], self.cube[center + 2] = self.cube[center + 2], self.cube[center + 3], self.cube[center + 4]
            self.cube[center + 2], self.cube[center + 3], self.cube[center + 4] = self.cube[center + 4], self.cube[center + 1], self.cube[center - 2]
            self.cube[center + 4], self.cube[center + 1], self.cube[center - 2] = temp1, temp2, temp3
        else:
            temp1, temp2, temp3 = self.cube[center - 2], self.cube[center - 3], self.cube[center - 4]
            self.cube[center - 2], self.cube[center - 3], self.cube[center - 4] = self.cube[center + 4], self.cube[center + 1], self.cube[center - 2]
            self.cube[center + 4], self.cube[center + 1], self.cube[center - 2] = self.cube[center + 2], self.cube[center + 3], self.cube[center + 4]
            self.cube[center + 2], self.cube[center + 3], self.cube[center + 4] = self.cube[center - 4], self.cube[center - 1], self.cube[center + 2]
            self.cube[center - 4], self.cube[center - 1], self.cube[center + 2] = temp1, temp2, temp3
    
    def __rotateCube(self, direction: str) -> None:
        match direction:
            case "X":
                temp0, temp1, temp2, temp3, temp4, temp5, temp6, temp7, temp8 = self.cube[0], self.cube[1], self.cube[2], self.cube[3], self.cube[4], self.cube[5], self.cube[6], self.cube[7], self.cube[8]
                self.cube[0], self.cube[1], self.cube[2], self.cube[3], self.cube[4], self.cube[5], self.cube[6], self.cube[7], self.cube[8] = self.cube[47], self.cube[46], self.cube[45], self.cube[50], self.cube[49], self.cube[48], self.cube[53], self.cube[52], self.cube[51]
                self.cube[47], self.cube[46], self.cube[45], self.cube[50], self.cube[49], self.cube[48], self.cube[53], self.cube[52], self.cube[51] = self.cube[26], self.cube[25], self.cube[24], self.cube[23], self.cube[22], self.cube[21], self.cube[20], self.cube[19], self.cube[18]
                self.cube[26], self.cube[25], self.cube[24], self.cube[23], self.cube[22], self.cube[21], self.cube[20], self.cube[19], self.cube[18] = self.cube[36], self.cube[37], self.cube[38], self.cube[39], self.cube[40], self.cube[41], self.cube[42], self.cube[43], self.cube[44]
                self.cube[36], self.cube[37], self.cube[38], self.cube[39], self.cube[40], self.cube[41], self.cube[42], self.cube[43], self.cube[44] = temp0, temp1, temp2, temp3, temp4, temp5, temp6, temp7, temp8

                self.__spinFace("L", True)
                self.__spinFace("R", False)
            case "X'":
                temp0, temp1, temp2, temp3, temp4, temp5, temp6, temp7, temp8 = self.cube[0], self.cube[1], self.cube[2], self.cube[3], self.cube[4], self.cube[5], self.cube[6], self.cube[7], self.cube[8]
                self.cube[0], self.cube[1], self.cube[2], self.cube[3], self.cube[4], self.cube[5], self.cube[6], self.cube[7], self.cube[8] = self.cube[36], self.cube[37], self.cube[38], self.cube[39], self.cube[40], self.cube[41], self.cube[42], self.cube[43], self.cube[44]
                self.cube[36], self.cube[37], self.cube[38], self.cube[39], self.cube[40], self.cube[41], self.cube[42], self.cube[43], self.cube[44] = self.cube[26], self.cube[25], self.cube[24], self.cube[23], self.cube[22], self.cube[21], self.cube[20], self.cube[19], self.cube[18]
                self.cube[26], self.cube[25], self.cube[24], self.cube[23], self.cube[22], self.cube[21], self.cube[20], self.cube[19], self.cube[18] = self.cube[47], self.cube[46], self.cube[45], self.cube[50], self.cube[49], self.cube[48], self.cube[53], self.cube[52], self.cube[51]
                self.cube[47], self.cube[46], self.cube[45], self.cube[50], self.cube[49], self.cube[48], self.cube[53], self.cube[52], self.cube[51] = temp0, temp1, temp2, temp3, temp4, temp5, temp6, temp7, temp8

                self.__spinFace("L", False)
                self.__spinFace("R", True)
            case "Y":
                temp0, temp1, temp2, temp3, temp4, temp5, temp6, temp7, temp8 = self.cube[0], self.cube[1], self.cube[2], self.cube[3], self.cube[4], self.cube[5], self.cube[6], self.cube[7], self.cube[8]
                self.cube[0], self.cube[1], self.cube[2], self.cube[3], self.cube[4], self.cube[5], self.cube[6], self.cube[7], self.cube[8] = self.cube[27], self.cube[28], self.cube[29], self.cube[30], self.cube[31], self.cube[32], self.cube[33], self.cube[34], self.cube[35]
                self.cube[27], self.cube[28], self.cube[29], self.cube[30], self.cube[31], self.cube[32], self.cube[33], self.cube[34], self.cube[35] = self.cube[18], self.cube[19], self.cube[20], self.cube[21], self.cube[22], self.cube[23], self.cube[24], self.cube[25], self.cube[26]
                self.cube[18], self.cube[19], self.cube[20], self.cube[21], self.cube[22], self.cube[23], self.cube[24], self.cube[25], self.cube[26] = self.cube[9], self.cube[10], self.cube[11], self.cube[12], self.cube[13], self.cube[14], self.cube[15], self.cube[16], self.cube[17]
                self.cube[9], self.cube[10], self.cube[11], self.cube[12], self.cube[13], self.cube[14], self.cube[15], self.cube[16], self.cube[17] = temp0, temp1, temp2, temp3, temp4, temp5, temp6, temp7, temp8

                self.__spinFace("U", True)
                self.__spinFace("D", False)
            case "Y'":
                temp0, temp1, temp2, temp3, temp4, temp5, temp6, temp7, temp8 = self.cube[0], self.cube[1], self.cube[2], self.cube[3], self.cube[4], self.cube[5], self.cube[6], self.cube[7], self.cube[8]
                self.cube[0], self.cube[1], self.cube[2], self.cube[3], self.cube[4], self.cube[5], self.cube[6], self.cube[7], self.cube[8] = self.cube[9], self.cube[10], self.cube[11], self.cube[12], self.cube[13], self.cube[14], self.cube[15], self.cube[16], self.cube[17]
                self.cube[9], self.cube[10], self.cube[11], self.cube[12], self.cube[13], self.cube[14], self.cube[15], self.cube[16], self.cube[17] = self.cube[18], self.cube[19], self.cube[20], self.cube[21], self.cube[22], self.cube[23], self.cube[24], self.cube[25], self.cube[26]
                self.cube[18], self.cube[19], self.cube[20], self.cube[21], self.cube[22], self.cube[23], self.cube[24], self.cube[25], self.cube[26] = self.cube[27], self.cube[28], self.cube[29], self.cube[30], self.cube[31], self.cube[32], self.cube[33], self.cube[34], self.cube[35]
                self.cube[27], self.cube[28], self.cube[29], self.cube[30], self.cube[31], self.cube[32], self.cube[33], self.cube[34], self.cube[35] = temp0, temp1, temp2, temp3, temp4, temp5, temp6, temp7, temp8

                self.__spinFace("U", False)
                self.__spinFace("D", True)
            case "Z":
                temp0, temp1, temp2, temp3, temp4, temp5, temp6, temp7, temp8 = self.cube[27], self.cube[28], self.cube[29], self.cube[30], self.cube[31], self.cube[32], self.cube[33], self.cube[34], self.cube[35]
                self.cube[27], self.cube[28], self.cube[29], self.cube[30], self.cube[31], self.cube[32], self.cube[33], self.cube[34], self.cube[35] = self.cube[42], self.cube[39], self.cube[36], self.cube[43], self.cube[40], self.cube[37], self.cube[44], self.cube[41], self.cube[38]
                self.cube[42], self.cube[39], self.cube[36], self.cube[43], self.cube[40], self.cube[37], self.cube[44], self.cube[41], self.cube[38] = self.cube[17], self.cube[16], self.cube[15], self.cube[14], self.cube[13], self.cube[12], self.cube[11], self.cube[10], self.cube[9]
                self.cube[17], self.cube[16], self.cube[15], self.cube[14], self.cube[13], self.cube[12], self.cube[11], self.cube[10], self.cube[9] = self.cube[45], self.cube[48], self.cube[51], self.cube[46], self.cube[49], self.cube[52], self.cube[47], self.cube[50], self.cube[53]
                self.cube[45], self.cube[48], self.cube[51], self.cube[46], self.cube[49], self.cube[52], self.cube[47], self.cube[50], self.cube[53] = temp0, temp1, temp2, temp3, temp4, temp5, temp6, temp7, temp8

                self.__spinFace("F", True)
                self.__spinFace("B", False)
            case "Z'":
                temp0, temp1, temp2, temp3, temp4, temp5, temp6, temp7, temp8 = self.cube[27], self.cube[28], self.cube[29], self.cube[30], self.cube[31], self.cube[32], self.cube[33], self.cube[34], self.cube[35]
                self.cube[27], self.cube[28], self.cube[29], self.cube[30], self.cube[31], self.cube[32], self.cube[33], self.cube[34], self.cube[35] = self.cube[45], self.cube[48], self.cube[51], self.cube[46], self.cube[49], self.cube[52], self.cube[47], self.cube[50], self.cube[53]
                self.cube[45], self.cube[48], self.cube[51], self.cube[46], self.cube[49], self.cube[52], self.cube[47], self.cube[50], self.cube[53] = self.cube[17], self.cube[16], self.cube[15], self.cube[14], self.cube[13], self.cube[12], self.cube[11], self.cube[10], self.cube[9]
                self.cube[17], self.cube[16], self.cube[15], self.cube[14], self.cube[13], self.cube[12], self.cube[11], self.cube[10], self.cube[9] = self.cube[42], self.cube[39], self.cube[36], self.cube[43], self.cube[40], self.cube[37], self.cube[44], self.cube[41], self.cube[38]
                self.cube[42], self.cube[39], self.cube[36], self.cube[43], self.cube[40], self.cube[37], self.cube[44], self.cube[41], self.cube[38] = temp0, temp1, temp2, temp3, temp4, temp5, temp6, temp7, temp8

                self.__spinFace("F", False)
                self.__spinFace("B", True)

    def rotate(self, face: str) -> None:
        match face:
            case "F":
                temp1, temp2, temp3 = self.cube[11], self.cube[14], self.cube[17]
                self.cube[11], self.cube[14], self.cube[17] = self.cube[47], self.cube[46], self.cube[45]
                self.cube[47], self.cube[46], self.cube[45] = self.cube[27], self.cube[30], self.cube[33]
                self.cube[27], self.cube[30], self.cube[33] = self.cube[42], self.cube[43], self.cube[44]
                self.cube[42], self.cube[43], self.cube[44] = temp1, temp2, temp3
            case "F'":
                temp1, temp2, temp3 = self.cube[11], self.cube[14], self.cube[17]
                self.cube[11], self.cube[14], self.cube[17] = self.cube[42], self.cube[43], self.cube[44]
                self.cube[42], self.cube[43], self.cube[44] = self.cube[27], self.cube[30], self.cube[33]
                self.cube[27], self.cube[30], self.cube[33] = self.cube[47], self.cube[46], self.cube[45]
                self.cube[47], self.cube[46], self.cube[45] = temp1, temp2, temp3
            case "R":
                temp1, temp2, temp3 = self.cube[2], self.cube[5], self.cube[8]
                self.cube[2], self.cube[5], self.cube[8] = self.cube[45], self.cube[48], self.cube[51]
                self.cube[45], self.cube[48], self.cube[51] = self.cube[24], self.cube[21], self.cube[18]
                self.cube[24], self.cube[21], self.cube[18] = self.cube[38], self.cube[41], self.cube[44]
                self.cube[38], self.cube[41], self.cube[44] = temp1, temp2, temp3
            case "R'":
                temp1, temp2, temp3 = self.cube[2], self.cube[5], self.cube[8]
                self.cube[2], self.cube[5], self.cube[8] = self.cube[38], self.cube[41], self.cube[44]
                self.cube[38], self.cube[41], self.cube[44] = self.cube[24], self.cube[21], self.cube[18]
                self.cube[24], self.cube[21], self.cube[18] = self.cube[45], self.cube[48], self.cube[51]
                self.cube[45], self.cube[48], self.cube[51] = temp1, temp2, temp3
            case "U":
                temp1, temp2, temp3 = self.cube[0], self.cube[1], self.cube[2]
                self.cube[0], self.cube[1], self.cube[2] = self.cube[27], self.cube[28], self.cube[29]
                self.cube[27], self.cube[28], self.cube[29] = self.cube[18], self.cube[19], self.cube[20]
                self.cube[18], self.cube[19], self.cube[20] = self.cube[9], self.cube[10], self.cube[11]
                self.cube[9], self.cube[10], self.cube[11] = temp1, temp2, temp3
            case "U'":
                temp1, temp2, temp3 = self.cube[0], self.cube[1], self.cube[2]
                self.cube[0], self.cube[1], self.cube[2] = self.cube[9], self.cube[10], self.cube[11]
                self.cube[9], self.cube[10], self.cube[11] = self.cube[18], self.cube[19], self.cube[20]
                self.cube[18], self.cube[19], self.cube[20] = self.cube[27], self.cube[28], self.cube[29]
                self.cube[27], self.cube[28], self.cube[29] = temp1, temp2, temp3
            case "L":
                temp1, temp2, temp3 = self.cube[0], self.cube[3], self.cube[6]
                self.cube[0], self.cube[3], self.cube[6] = self.cube[36], self.cube[39], self.cube[42]
                self.cube[36], self.cube[39], self.cube[42] = self.cube[26], self.cube[23], self.cube[20]
                self.cube[26], self.cube[23], self.cube[20] = self.cube[47], self.cube[50], self.cube[53]
                self.cube[47], self.cube[50], self.cube[53] = temp1, temp2, temp3
            case "L'":
                temp1, temp2, temp3 = self.cube[0], self.cube[3], self.cube[6]
                self.cube[0], self.cube[3], self.cube[6] = self.cube[47], self.cube[50], self.cube[53]
                self.cube[47], self.cube[50], self.cube[53] = self.cube[26], self.cube[23], self.cube[20]
                self.cube[26], self.cube[23], self.cube[20] = self.cube[36], self.cube[39], self.cube[42]
                self.cube[36], self.cube[39], self.cube[42] = temp1, temp2, temp3
            case "B":
                temp1, temp2, temp3 = self.cube[36], self.cube[37], self.cube[38]
                self.cube[36], self.cube[37], self.cube[38] = self.cube[29], self.cube[32], self.cube[35]
                self.cube[29], self.cube[32], self.cube[35] = self.cube[51], self.cube[52], self.cube[53]
                self.cube[51], self.cube[52], self.cube[53] = self.cube[9], self.cube[12], self.cube[15]
                self.cube[9], self.cube[12], self.cube[15] = temp1, temp2, temp3
            case "B'":
                temp1, temp2, temp3 = self.cube[36], self.cube[37], self.cube[38]
                self.cube[36], self.cube[37], self.cube[38] = self.cube[9], self.cube[12], self.cube[15]
                self.cube[9], self.cube[12], self.cube[15] = self.cube[51], self.cube[52], self.cube[53]
                self.cube[51], self.cube[52], self.cube[53] = self.cube[29], self.cube[32], self.cube[35]
                self.cube[29], self.cube[32], self.cube[35] = temp1, temp2, temp3
            case "D":
                temp1, temp2, temp3 = self.cube[6], self.cube[7], self.cube[8]
                self.cube[6], self.cube[7], self.cube[8] = self.cube[15], self.cube[16], self.cube[17]
                self.cube[15], self.cube[16], self.cube[17] = self.cube[24], self.cube[25], self.cube[26]
                self.cube[24], self.cube[25], self.cube[26] = self.cube[33], self.cube[34], self.cube[35]
                self.cube[33], self.cube[34], self.cube[35] = temp1, temp2, temp3
            case "D'":
                temp1, temp2, temp3 = self.cube[6], self.cube[7], self.cube[8]
                self.cube[6], self.cube[7], self.cube[8] = self.cube[33], self.cube[34], self.cube[35]
                self.cube[33], self.cube[34], self.cube[35] = self.cube[24], self.cube[25], self.cube[26]
                self.cube[24], self.cube[25], self.cube[26] = self.cube[15], self.cube[16], self.cube[17]
                self.cube[15], self.cube[16], self.cube[17] = temp1, temp2, temp3
            case "M":
                temp1, temp2, temp3 = self.cube[1], self.cube[4], self.cube[7]
                self.cube[1], self.cube[4], self.cube[7] = self.cube[37], self.cube[40], self.cube[43]
                self.cube[37], self.cube[40], self.cube[43] = self.cube[25], self.cube[22], self.cube[19]
                self.cube[25], self.cube[22], self.cube[19] = self.cube[46], self.cube[49], self.cube[52]
                self.cube[46], self.cube[49], self.cube[52] = temp1, temp2, temp3
            case "M'":
                temp1, temp2, temp3 = self.cube[1], self.cube[4], self.cube[7]
                self.cube[1], self.cube[4], self.cube[7] = self.cube[46], self.cube[49], self.cube[52]
                self.cube[46], self.cube[49], self.cube[52] = self.cube[25], self.cube[22], self.cube[19]
                self.cube[25], self.cube[22], self.cube[19] = self.cube[37], self.cube[40], self.cube[43]
                self.cube[37], self.cube[40], self.cube[43] = temp1, temp2, temp3
            case "E":
                temp1, temp2, temp3 = self.cube[3], self.cube[4], self.cube[5]
                self.cube[3], self.cube[4], self.cube[5] = self.cube[12], self.cube[13], self.cube[14]
                self.cube[12], self.cube[13], self.cube[14] = self.cube[21], self.cube[22], self.cube[23]
                self.cube[21], self.cube[22], self.cube[23] = self.cube[30], self.cube[31], self.cube[32]
                self.cube[30], self.cube[31], self.cube[32] = temp1, temp2, temp3
            case "E'":
                temp1, temp2, temp3 = self.cube[3], self.cube[4], self.cube[5]
                self.cube[3], self.cube[4], self.cube[5] = self.cube[30], self.cube[31], self.cube[32]
                self.cube[30], self.cube[31], self.cube[32] = self.cube[21], self.cube[22], self.cube[23]
                self.cube[21], self.cube[22], self.cube[23] = self.cube[12], self.cube[13], self.cube[14]
                self.cube[12], self.cube[13], self.cube[14] = temp1, temp2, temp3
            case "S":
                temp1, temp2, temp3 = self.cube[28], self.cube[31], self.cube[34]
                self.cube[28], self.cube[31], self.cube[34] = self.cube[39], self.cube[40], self.cube[41]
                self.cube[39], self.cube[40], self.cube[41] = self.cube[10], self.cube[13], self.cube[16]
                self.cube[10], self.cube[13], self.cube[16] = self.cube[50], self.cube[49], self.cube[48]
                self.cube[50], self.cube[49], self.cube[48] = temp1, temp2, temp3
            case "S'":
                temp1, temp2, temp3 = self.cube[28], self.cube[31], self.cube[34]
                self.cube[28], self.cube[31], self.cube[34] = self.cube[50], self.cube[49], self.cube[48]
                self.cube[50], self.cube[49], self.cube[48] = self.cube[10], self.cube[13], self.cube[16]
                self.cube[10], self.cube[13], self.cube[16] = self.cube[39], self.cube[40], self.cube[41]
                self.cube[39], self.cube[40], self.cube[41] = temp1, temp2, temp3
        
        self.__spinFace(face[0], len(face) == 1)
    
    def scramble(self, moves: int = 50) -> None:
        moveset = ["F", "F'", "R", "R'", "U", "U'", "L", "L'", "B", "B'", "D", "D'", "M", "M'", "E", "E'", "S", "S'"]
        for i in range(moves):
            self.rotate(random.choice(moveset)[0])

c = Cube3x3("G", "W")
c.rotate("U'")
c.rotate("R")
c.rotate("U'")
c.rotate("U'")
c.rotate("R'")
c.rotate("U'")
c.rotate("R")
c.rotate("U'")
c.rotate("R'")
print(c)