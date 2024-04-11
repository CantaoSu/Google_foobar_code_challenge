
class StairCase(object):
    stair_cache = {}
    stair_record = 0
    
    def __init__(self):
        pass
    
    def find_all_combination_at_nth_stair(self, n):
        if n < 3: return 0
    
        while n > self.stair_record:
            n_ = self.stair_record + 1
            n_str = str(n_)
            m_str = str(n_-1)
            
            temp = []
            for i in range(n_):
                m_ = i + 1
                b_ = n_ - m_
                if m_ < b_:
                    temp.append(self.stair_cache[str(m_)]['self'])
                else:
                    temp.append(self.get_stair_combination_at_base_i(m_, b_))
                    if temp[-1] <= 0:
                        break

            self_ = 1 + sum(temp)
            sum_ = self_ - 1
            other_ = [sum_]
            for i in range(n_):
                sum_ -= temp[i]
                if sum_ <= 0:
                    break
                other_.append(sum_)

            self.stair_cache[n_str] = {'self': self_, 'other': other_}
            self.stair_record = int(n_str)
                
        
        return self.stair_cache[str(n)]['self'] - 1
                    
    def get_stair_combination_at_base_i(self, m, idx):
        m_str = str(m)
        if m_str in self.stair_cache:
            other_ = self.stair_cache[m_str]['other']
            idx_ = m - idx
            if idx_ < len(other_):
                return other_[idx_]
            else:
                return 0
                
    
    @staticmethod
    def reset_step():
        StairCase.stair_cache.clear()
        StairCase.stair_record = 3
        StairCase.stair_cache['1'] = {'self': 1, 'other':[0]}
        StairCase.stair_cache['2'] = {'self': 1, 'other':[0]}
        StairCase.stair_cache['3'] = {'self': 2, 'other':[1]}
        
        
StairCase.reset_step()
stair = StairCase()
print(stair.find_all_combination_at_nth_stair(5))