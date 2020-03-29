import pygame, sys
from Sudoku.settings import *
from Sudoku.buttonClass import *


class App:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.grid = finishedBoard
        self.running = True
        self.selected = None
        self.mousePos = None
        self.state = "playing"
        self.font = pygame.font.SysFont("arial", cellSize // 2)
        self.playingButtons = []
        self.menuButtons = []
        self.endButtons = []
        self.lockCells = []
        self.incorrectCells = []
        self.finish = False
        self.cellChange = False
        self.load()

    def run(self):
        while self.running:
            if self.state == "playing":
                self.playing_events()
                self.playing_update()
                self.playing_draw()
        pygame.quit()
        sys.exit()

    ############ PLAYING STATE FUNCTIONS ############
    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                selected = self.mouseOnGrid()
                if selected:
                    self.selected = selected
                else:
                    self.selected = None
            if event.type == pygame.KEYDOWN:
                if self.selected and list(self.selected) not in self.lockCells:
                    if self.isInt(event.unicode):
                        self.grid[self.selected[1]][self.selected[0]] = int(event.unicode)
                        self.cellChange = True

    def playing_update(self):
        self.mousePos = pygame.mouse.get_pos()
        for button in self.playingButtons:
            button.update(self.mousePos)
        if self.cellChange:
            self.incorrectCells = []
            if self.allCellsDone():
                self.checkAllCells()
                if len(self.incorrectCells) == 0:
                    print("Congratulations")

    def playing_draw(self):
        self.window.fill(WHITE)
        for button in self.playingButtons:
            button.draw(self.window)
        if self.selected:
            self.drawSelection(self.window, self.selected)
        self.shareLockCells(self.window, self.lockCells)
        self.shareIncorrectCells(self.window, self.incorrectCells)
        self.drawNumbers(self.window)
        self.drawGrid(self.window)
        pygame.display.update()
        self.cellChange = False

    ############ BOARD CHECKING FUNCTIONS ########
    def allCellsDone(self):
        for row in self.grid:
            for num in row:
                if num == 0:
                    return False
        return True

    def checkAllCells(self):
        # self.checkRow()
        # self.checkCol()
        self.checkSmallGrid()

    def checkSmallGrid(self):
        for x in range(3):
            for y in range(3):
                possible = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for i in range(3):
                    for j in range(3):
                        xid = x*3+i
                        yid = y*3+j
                        if self.grid[yid][xid] in possible:
                            possible.remove(self.grid[yid][xid])
                        else:
                            if [xid, yid] not in self.incorrectCells and [xid, yid] not in self.lockCells:
                                self.incorrectCells.append([xid, yid])

    def checkRow(self):
        for yid, row in enumerate(self.grid):
            possible = [1,2,3,4,5,6,7,8,9]
            for xid in range(9):
                if self.grid[yid][xid] in possible:
                    possible.remove(self.grid[yid][xid])
                else:
                    if [xid, yid] not in self.lockCells:
                        self.incorrectCells.append([xid, yid])

    def checkCol(self):
        for xid in range(9):
            for yid, row in enumerate(self.grid):
                possible = [1,2,3,4,5,6,7,8,9]
                if self.grid[yid][xid] in possible:
                    possible.remove(self.grid[yid][xid])
                else:
                    if [xid, yid] not in self.incorrectCells and [xid, yid] not in self.lockCells:
                        self.incorrectCells.append([xid, yid])

    ############ HELPER FUNCTIONS ###########
    def shareIncorrectCells(self, window, incorrect):
        for cell in incorrect:
            pygame.draw.rect(window, INCORRECTCELLCOLOUR,
                             (cell[0] * cellSize + gridPos[0], cell[1] * cellSize + gridPos[1], cellSize, cellSize))

    def shareLockCells(self, window, lock):
        for cell in lock:
            pygame.draw.rect(window, LOCKEDCELLCOLOUR,
                             (cell[0] * cellSize + gridPos[0], cell[1] * cellSize + gridPos[1], cellSize, cellSize))


    def drawNumbers(self, window):
        for yid, row in enumerate(self.grid):
            for xid, num in enumerate(row):
                if num != 0:
                    pos = [xid * cellSize + gridPos[0], yid * cellSize + gridPos[1]]
                    self.textToScreen(window, str(num), pos)

    def drawSelection(self, window, pos):
        pygame.draw.rect(window, LIGHTBLUE,
                         (pos[0] * cellSize + gridPos[0], pos[1] * cellSize + gridPos[1], cellSize, cellSize))

    def drawGrid(self, window):
        pygame.draw.rect(window, BLACK, (gridPos[0], gridPos[1], WIDTH - 150, HEIGHT - 150), 2)
        for x in range(9):
            pygame.draw.line(window, BLACK, (gridPos[0] + x * cellSize, gridPos[1]),
                             (gridPos[0] + x * cellSize, gridPos[1] + 450), 2 if x % 3 == 0 else 1)
            pygame.draw.line(window, BLACK, (gridPos[0], gridPos[1] + x * cellSize),
                             (gridPos[0] + 450, gridPos[1] + x * cellSize), 2 if x % 3 == 0 else 1)

    def mouseOnGrid(self):
        if self.mousePos[0] < gridPos[0] or self.mousePos[0] > gridPos[0] + gridSize or self.mousePos[1] < gridPos[1] or \
                self.mousePos[1] > gridPos[1] + gridSize:
            return False
        return (self.mousePos[0] - gridPos[0]) // cellSize, (self.mousePos[1] - gridPos[1]) // cellSize

    def loadButtons(self):
        self.playingButtons.append(Button(20, 40, 40, 100))

    def textToScreen(self, window, text, pos):
        font = self.font.render(text, False, BLACK)
        fontWidth = font.get_width()
        fontHeight = font.get_height()
        pos[0] += (cellSize - fontWidth) // 2
        pos[1] += (cellSize - fontHeight) // 2
        window.blit(font, pos)

    def load(self):
        self.loadButtons()
        for yid, row in enumerate(self.grid):
            for xid, num in enumerate(row):
                if num != 0:
                    self.lockCells.append([xid, yid])

    def isInt(self, string):
        try:
            int(string)
            return True
        except:
            return False
