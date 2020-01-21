class StalinList(list):
    """Implements StalinSort but acts like any other list"""
    def sort(self):
        i = 0
        elements = len(self)-1
        while i < elements:
            cur = self[i]
            next = self[i+1]
            if cur <= next:
                elements -= 1
                self.pop(i)
                i -= 1

