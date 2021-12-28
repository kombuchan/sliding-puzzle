from time import process_time
from collections import deque
from state import State
from solver import Solver

goal = [[0,1,2],[3,4,5],[6,7,8]]

class BFS(Solver):
	def solve(self):
		queue = deque([self.initialState])
		self.explored.add(self.initialState.id)
		self.expandedNodes += 1
		start_time = process_time()
		while queue:
			state = queue.popleft()
			state.getFManhattan()
			if (state.board == goal):
				self.finalState = state
				self.runningTime = process_time() - start_time
				return True
			if state.depth+1 > self.depth:
				self.depth = state.depth+1
			for neighbor in state.neighbors():
				if not ((neighbor.id in self.explored)):
					self.explored.add(neighbor.id)
					queue.append(neighbor)
		self.runningTime = process_time() - start_time
		return False