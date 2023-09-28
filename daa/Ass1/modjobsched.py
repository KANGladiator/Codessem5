import random

def generate_random_jobs(n):
    jobs = []
    for job_id in range(1, n + 1):
        deadline = random.randint(1, n)
        profit = random.randint(1, 100)
        jobs.append((job_id, deadline, profit))
    return jobs

def job_sequencing_with_deadline(jobs):
    jobs.sort(key=lambda x: (x[1], -x[2]))
    max_deadline = max(jobs, key=lambda x: x[1])[1]
    schedule = [-1] * (max_deadline + 1)
    total_profit = 0
    unscheduled_jobs = []
    
    for job in jobs:
        deadline, profit = job[1], job[2]
        while deadline > 0 and schedule[deadline] != -1:
            deadline -= 1
        if deadline > 0:
            schedule[deadline] = job[0]
            total_profit += profit
        else:
            unscheduled_jobs.append(job)
    
    return schedule, total_profit, unscheduled_jobs

n = 10

jobs = generate_random_jobs(n)
for job in jobs:
    print(job)

schedule, profit, unscheduled_jobs = job_sequencing_with_deadline(jobs)

print("Scheduled Jobs:", schedule[1:])
print("Total Profit:", profit)
print("Unscheduled Jobs:", unscheduled_jobs)
