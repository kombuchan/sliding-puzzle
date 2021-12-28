from time import process_time
from state import State
from solver import Solver
import heapq

goalTest = [[0,1,2],[3,4,5],[6,7,8]]

class Euclidean(Solver):
		

	def solve(self):
		start_time = process_time()
		queue = [self.initialState]
		self.initialState.getFEuclidean()
		self.explored.add(self.initialState.id)
		while queue:
			self.expandedNodes += 1
			state = heapq.heappop(queue)
			if (state.board == goalTest):
				self.finalState = state
				self.runningTime = process_time() - start_time
				return True
			if state.depth+1 > self.depth:
				self.depth = state.depth+1
			for neighbor in state.neighbors():
				if not ((neighbor.id in self.explored)):
					self.explored.add(neighbor.id)
					neighbor.getFEuclidean()
					heapq.heappush(queue,neighbor)
		self.runningTime = process_time() - start_time
		return False