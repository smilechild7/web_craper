import csv

def save_to_file(keyword, jobs):
    file = open(f"{keyword}_jobs.csv", "w") # 존재하지 않으면 새로 만듬, w는 쓰기 모드 (기본은 "r" 읽기)
    writer = csv.writer(file)
    writer.writerow(["Title","Comapany","Location","Reward","Link"]) #writerow 메서드는 list를 받는다
    for job in jobs:
        writer.writerow(job.values()) # value 값들만 모아서 리스트로 반환 
    file.close() 