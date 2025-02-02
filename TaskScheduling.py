def greedy_task_scheduling(tasks, num_workers):
    
    tasks.sort(key=lambda x: x[1], reverse=True)   
    
    
    workers = [0] * num_workers
    
     
    task_assignment = [[] for _ in range(num_workers)]  
    
    for task_name, task_time in tasks:
        
        min_worker = workers.index(min(workers))  
        workers[min_worker] += task_time   
        task_assignment[min_worker].append((task_name, task_time))   
    
    return task_assignment, workers

def main():
     
    num_tasks = int(input("Enter the number of tasks: "))
    tasks = []
    
    for i in range(num_tasks):
        task_name = input(f"Enter the name of task {i+1}: ")
        task_time = int(input(f"Enter the processing time for task {task_name}: "))
        tasks.append((task_name, task_time))
    
    num_workers = int(input("Enter the number of workers: "))
    
     
    task_assignment, workers = greedy_task_scheduling(tasks, num_workers)
    
    
    print("\nTask Assignment to Workers:")
    for i, task_list in enumerate(task_assignment):
        task_names = [task[0] for task in task_list]
        total_load = workers[i]
        print(f"Worker {i+1}: Tasks {task_names} - Total Load: {total_load}")
    
    max_load = max(workers)
    print(f"\nMax Load among workers: {max_load}")

if __name__ == "__main__":
    main()