import csv


def List_jobs(jenkins_url,jenkins_user,jenkins_pass):
    import jenkins

    server = jenkins.Jenkins(jenkins_url, jenkins_user, jenkins_pass)
    user = server.get_whoami()
    jobs = server.get_jobs()

    jobs_stats=[]
    for i in jobs:
        jobs_name = i['name']
        jobs_url =i['url'] , 
        jobs_status =i['color']
        jobs_stats.append([jobs_name,jobs_url,jobs_status])
    return jobs_stats

# with open("example.txt" , 'a') as f:
#     content = "hhskjhsuhsr\n"
#     f.write(content)


# with open("example.txt", 'r') as file:
#     cont = file.read()
#     print(cont)

data=List_jobs('http://45.33.11.12:8080','utrains','devops')
with open("jenkins_object.csv", 'w') as j:
    write_row =csv.writer(j)
    write_row.writerow(['JOBS_NAME', 'JOBS_URL', 'JOBS_STATUS'])
    for item in data:
        write_row.writerow(item)