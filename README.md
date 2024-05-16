Your task is to develop a program that simulates the scheduling of processes using First-Come First-Served (FCFS), Shortest Remaining Time (SRT) (i.e., Shortest Job First with preemption), and Round-Robin (RR) with a specified time quantum (Q). Assume a Context Switch Time (CS) of x milliseconds.
Your simulator should create the Process Control Block (PCB) for each process with the necessary data structure.
Upon completion of the last process, your simulator should display the following results on the screen:
A Gantt Chart illustrating the execution times of the processes
Finish time for each process
Waiting time for each process
Turnaround time for each process
CPU utilization
The program should read the list of processes, including their arrival times and CPU bursts, along with the values of x and Q (Context Switch Time and Quantum, respectively), from a text file.
