class Grid:
    def __init__(self, rows, columns, show=True, empty_cell='none', repr_char_notshow=""):
        self.rows = rows
        self.columns = columns
        self.show = show
        self.empty_cell = empty_cell
        self.repr_char_notshow = repr_char_notshow
        self.grid = [[None for _ in range(columns)] for _ in range(rows)]
        self.alignments = {}
    
    def __enter__(self):
        return self
    
    def __exit__(self, *args):
        pass
    
    def __repr__(self):
        max_lengths = [max(len(str(self.grid[row][col])) for row in range(self.rows)) for col in range(self.columns)]
        res = ''
        for row in range(self.rows):
            if self.show:
                res += ' | '.join([self._format_cell(row, col, max_lengths) for col in range(self.columns)])
                res += '\n' + '-' * sum(max_lengths[col] + 3 for col in range(self.columns)) + '\n'
            else:
                res += f'{self.repr_char_notshow}'.join([self._format_cell(row, col, max_lengths) for col in range(self.columns)])
                res += '\n'
        return res
    
    def _format_cell(self, row, col, max_lengths):
        cell = str(self.grid[row][col]) if self.grid[row][col] is not None else self.empty_cell
        align = self.alignments.get((row, col))
        if align == 'left':
            return cell.ljust(max_lengths[col])
        elif align == 'center':
            return cell.center(max_lengths[col])
        elif align == 'right':
            return cell.rjust(max_lengths[col])
        else:
            return cell
    
    def __int__(self):
        return self.rows * self.columns
    
    def __str__(self):
        return self.__repr__()
    
    def __iter__(self):
        self.iter_index = 0
        return self
    
    def __next__(self):
        if self.iter_index >= self.rows * self.columns:
            raise StopIteration
        result = self.grid[self.iter_index // self.columns][self.iter_index % self.columns]
        self.iter_index += 1
        return result
    
    def set(self, row, column, value, align=None):
        self.grid[row][column] = value
        if align is not None:
            self.alignments[(row, column)] = align






with Grid(5, 5, show=False) as gr:
    gr.set(0, 0, "Hello", align='center')
    gr.set(1, 1, "World", align='right')
    gr.set(4, 3, "Just Fun", align='left')
    gr.set(1, 2, "!", align='center')
    print(gr)