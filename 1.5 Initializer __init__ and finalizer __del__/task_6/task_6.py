from typing import Union, List
class CPU:
    def __init__(self, name: str, fr: Union[int,float]):
        self.name = name
        self.fr = fr
        
class Memory:
    def __init__(self, name: str,volume: Union[int, float]):
        self.name = name
        self.volume = volume
        
class MotherBoard:
    def __init__(self, name: str, cpu: CPU, mem_slots: List[Memory]):
        self.name= name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = mem_slots
    def get_config(self):
        total_memory = len(self.mem_slots)
        config_lst = [f"Материнская плата: {self.name}",
                      f"Центральный процессор: {self.cpu.name}, {self.cpu.fr}",
                      f"Слотов памяти: {total_memory}",
                      f"Память: {'; '.join([f'{self.mem_slots[i].name} - {self.mem_slots[i].volume}' for i in range(len(self.mem_slots))])}"]

        return config_lst
cpu = CPU('intel',333)
mem = [Memory('Kingston',220),Memory('Kingston',221),Memory('Kingston',222),Memory('Kingston',224)]
mb = MotherBoard('ASUS',cpu,mem)
