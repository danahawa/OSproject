class Process:
    def __init__(self, pid, arrival_time, cpu_burst):
        self.pid = pid
        self.arrival_time = arrival_time
        self.cpu_burst = cpu_burst
        self.remaining = cpu_burst
        self.start_time = 0
        self.finish_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0
    
    def __str__(self):
        print(f'     {self.pid}      |       {self.arrival_time}       |       {self.cpu_burst}  ')


def FCFS(processes, context_switch_time):
    completed_processes = []
    gantt_chart = []
    current_time = 0
    total_burst_time = sum(process.cpu_burst for process in processes)
    processes.sort(key=lambda x: x.arrival_time)
    while processes :
            process = processes[0]
        
            if current_time <= process.arrival_time:
                current_time = process.arrival_time
                
            process.start_time = current_time
            current_time += process.cpu_burst
            process.finish_time = current_time
            process.turnaround_time = process.finish_time - process.arrival_time
            process.waiting_time = process.turnaround_time - process.cpu_burst
            gantt_chart.append((process.pid, current_time)) 
            current_time += context_switch_time
            completed_processes.append(process)   
            processes.pop(0) 
    cpu_utilization = (total_burst_time / current_time) * 100                
    return gantt_chart ,completed_processes  ,cpu_utilization 

######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
def RR(processes, Q, ContextSwitchTime):
    current_time = 0
    ready = []
    waiting = []
    gantt_chart = []
    completed_processes =[]
    total_burst_time = sum(process.cpu_burst for process in processes)
    processes.sort(key=lambda x: x.arrival_time)
    while processes or ready or waiting:
        
        for process in processes:
            if process.arrival_time <= current_time:
                ready.append(process)
                processes.remove(process)

    
        if ready:
            running = ready.pop(0)  

            if running.cpu_burst <= Q:
                running.start_time = current_time
                current_time += running.cpu_burst 
                gantt_chart.append((running.pid, current_time))
                running.finish_time = current_time
                running.turnaround_time = running.finish_time - running.arrival_time
                running.waiting_time = running.turnaround_time - running.cpu_burst+ContextSwitchTime
                completed_processes.append(running)
                running.cpu_burst = 0

            else:
                current_time += Q + ContextSwitchTime
                running.cpu_burst -= Q
                gantt_chart.append((running.pid, current_time))
                ready.append(running)

        elif waiting:
            current_time = min(process.arrival_time for process in waiting)
    cpu_utilization = (total_burst_time / current_time) * 100  
    return gantt_chart,completed_processes ,cpu_utilization

######################################################################################################################################
def SRTF(processes, ContextSwitchTime):
    waiting = []
    ready = []
    completed_processes = []
    gantt_chart = []
    current_time = 0
    total_burst_time = sum(process.cpu_burst for process in processes)

    while processes or ready or waiting:
        
        for process in processes:
            if process.arrival_time <= current_time and process.remaining > 0:
                ready.append(process)
                processes.remove(process)

       
        if not ready:
            current_time += 1
            continue

       
        ready.sort(key=lambda x: x.remaining)
        running = ready[0]

        
        if not running.start_time:
            running.start_time = current_time

        
        current_time += 1
        running.remaining -= 1
        gantt_chart.append((running.pid, current_time))

        
        for process in ready:
            if process.remaining < running.remaining:
                
                waiting.append(running)
                ready.remove(running)
                running = process
                break

        
        if running.remaining == 0:
            running.finish_time = current_time
            running.turnaround_time = running.finish_time - running.arrival_time
            running.waiting_time = running.turnaround_time - running.cpu_burst + ContextSwitchTime
            completed_processes.append(running)
            ready.remove(running)

       
        for process in waiting:
            if process.arrival_time <= current_time:
                ready.append(process)
                waiting.remove(process)

    cpu_utilization = (total_burst_time / current_time) * 100            

    return gantt_chart, completed_processes,cpu_utilization

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def read(filename):
    processes = []
    with open(filename, 'r') as file:
        for line in file:
            pid, arrival_time, cpu_burst = map(int, line.strip().split())
            processes.append(Process(pid, arrival_time, cpu_burst))
    return processes

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.>..
def calculate_avg(completed_processes):
    for process in completed_processes:
        total_waiting_time = process.waiting_time
        total_turnaround_time = process.turnaround_time
    avg_waiting_time = total_waiting_time / len(completed_processes)
    avg_turnaround_time = total_turnaround_time / len(completed_processes)
    return avg_waiting_time,avg_turnaround_time
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
if __name__ == "__main__":
    path=('C:\\Users\\DELL\\Desktop\\osproject\\processes.txt')
    processes=read(path)
    context_switch_time = 0.001
    Q=4
    p1 = processes.copy()
    print("process id  |  arrival time  |  CPU burst")
    for process in processes:
        print('-----------------------------------------')
        print(f'     {process.pid}      |       {process.arrival_time}       |       {process.cpu_burst}  ')

    g_ch,completed_processes,cpu_utilization =FCFS(p1,context_switch_time)
   # g_ch,completed_processes,cpu_utilization =SRTF(p1,context_switch_time)
   # g_ch,completed_processes,cpu_utilization =RR(p1,Q,context_switch_time)
    avg_waiting_time, avg_turnaround_time= calculate_avg(completed_processes) 
    print('\n')
    print('Gantt Chart: id|Finish time')
    print('\n')
    print('---------------------------------------------------------------------------------------------------------')  
    for p,time in  g_ch: 
        print(p,'|',time,sep="",end='   ') 
    print('\n')
    print('---------------------------------------------------------------------------------------------------------')  
   
    for process in completed_processes:
        print(f"id:{process.pid}  |   start time:{process.start_time}  |   finish time:{process.finish_time} |  waiting time :{process.waiting_time}  |  turnaround time:{process.turnaround_time}")    
        print('\n')
    print(f'CPU utilization: {cpu_utilization}')
    print(f'average wating time: {avg_waiting_time}')
    print(f'average turnaround time: {avg_turnaround_time}')
     
