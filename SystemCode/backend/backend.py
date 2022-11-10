import sqlite3
import re
import random

conn = sqlite3.connect("/Users/maggie/my-project/backend/job.db")
print("Opened database successfully")

c = conn.cursor()   #获取游标
sql = "SELECT job_id, title, telecommuting,country_id,type_id,experience_id,education_id,main_id,mbti_id_1,mbti_id_2,mbti_id_3,mbti_id_4 from 'test5'"
cursor = c.execute(sql)#执行sql语句

job, title, telecommuting,country,Type,experience,education,function,mbti_id_1,mbti_id_2,mbti_id_3,mbti_id_4 = ([] for i in range(12))

for row in cursor:
    job.append(row[0])
    title.append(row[1])
    telecommuting.append(row[2])
    country.append(row[3])
    Type.append(row[4])
    experience.append(row[5])
    education.append(row[6])
    function.append(row[7])
    mbti_id_1.append(row[8])
    mbti_id_2.append(row[9])
    mbti_id_3.append(row[10])
    mbti_id_4.append(row[11])

conn.close()  #关闭数据库连接

job = [i for i in range(0, 17364)]


def Selection(Index, Target, j):
    i = 0
    Job = []
    while i < len(Index):
        if Target[i] == j:
            Job.append(Index[i])
        else:
            Job = Job
        i = i+1
    return Job


def SelectionSmaller(Index, Target, j):
    i = 0
    Job = []
    while i < len(Index):
        if Target[Index[i]] < j+1:
            Job.append(Index[i])
        else:
            Job = Job
        i = i+1
    return Job


def SelectionUnequal(Index, Target, j):
    i = 0
    Job = []
    if j == 'X':
        Job = Index
    else:
        while i < len(Index):
            if Target[Index[i]] == 'X' or Target[Index[i]] == j:
                Job.append(Index[i])
            else:
                Job = Job
            i = i+1
    return Job


a = SelectionUnequal(job, mbti_id_2, 'N')
# len(a)


def SelectionIdeal(Index, m):
    # function
    Job_1 = Selection(Index, function, m[5])
#     print(len(Job_1))
    Job = SelectionIdeal_Part(Job_1, m)
    return Job


def SelectionIdeal_Part(Job_1,m):
# telecommuting,country,Type
    Job_2 = Selection(Job_1,telecommuting,m[0])
#     print(len(Job_2))
    Job_3 = Selection(Job_1,country,m[1])
#     print(len(Job_3))
    Job_4 = Selection(Job_1,Type,m[2])
#     print(len(Job_4))
    Job_5 = list(set(Job_2) & set(Job_3) & set(Job_4))
#     print(len(Job_5))
    Job_6 = list(set(Job_2) & set(Job_3))
#     print(len(Job_6))
    Job_7 = list(set(Job_4) & set(Job_3))
#     print(len(Job_7))
    Job_8 = list(set(Job_2) & set(Job_4))
#     print(len(Job_8))   
     
    Job_all = [Job_2,Job_3,Job_4,Job_5,Job_6,Job_7,Job_8]
    for jobs in Job_all:
        job = [jobs for jobs in Job_all if len(jobs) != 0]
    i=0
    Job = job[0]
    while i < len(job):
        if len(job[i]) < len(Job):
            Job = job[i]
        else:
            Job = Job
        i=i+1
#     print(len(Job))
    return Job


def SelectionIdeal_Part(Job_1, m):
    # telecommuting,country,Type
    Job_2 = Selection(Job_1, telecommuting, m[0])
#     print(len(Job_2))
    Job_3 = Selection(Job_1, country, m[1])
#     print(len(Job_3))
    Job_4 = Selection(Job_1, Type, m[2])
#     print(len(Job_4))
    Job_5 = list(set(Job_2) & set(Job_3) & set(Job_4))
#     print(len(Job_5))
    Job_6 = list(set(Job_2) & set(Job_3))
#     print(len(Job_6))
    Job_7 = list(set(Job_4) & set(Job_3))
#     print(len(Job_7))
    Job_8 = list(set(Job_2) & set(Job_4))
#     print(len(Job_8))

    Job_all = [Job_2, Job_3, Job_4, Job_5, Job_6, Job_7, Job_8]
    for jobs in Job_all:
        job = [jobs for jobs in Job_all if len(jobs) != 0]
    i = 0
    Job = job[0]
    while i < len(job):
        if len(job[i]) < len(Job):
            Job = job[i]
        else:
            Job = Job
        i = i+1
#     print(len(Job))
    return Job


def SelectionSuitable(Index, m):
    # experience,education,mbti
    Job_1 = SelectionSmaller(Index, experience, m[3])
#     print(len(Job_1))
    Job_2 = SelectionSmaller(Job_1, education, m[4])
#     print(len(Job_2))
    Job_3 = SelectionUnequal(Job_2, mbti_id_1, m[6])
#     print(len(Job_3))
    if len(Job_3) > 0:
        Job_4 = SelectionUnequal(Job_3, mbti_id_2, m[7])
    else:
        Job_4 = SelectionUnequal(Job_2, mbti_id_2, m[7])
        print(1)
#     print(len(Job_4))
    if len(Job_4) > 0:
        Job_5 = SelectionUnequal(Job_4, mbti_id_3, m[8])
    else:
        Job_5 = SelectionUnequal(Job_2, mbti_id_3, m[8])
        print(1)
#     print(len(Job_5))
    if len(Job_5) > 0:
        Job_6 = SelectionUnequal(Job_5, mbti_id_4, m[9])
    else:
        Job_6 = SelectionUnequal(Job_2, mbti_id_4, m[9])
        print(1)
#     print(len(Job_6))

# telecommuting,country,Type
    Job = SelectionIdeal_Part(Job_6, m)
    return Job


def MBTI_comment(m, n):
    # m-ideal n-suitable
    EI_ideal = mbti_id_1[m]
    EI_suitable = n[6]
#     print(EI_ideal,EI_suitable)
    if EI_ideal == 'X' or EI_suitable == 'X' or EI_ideal == EI_suitable:
        comment_1 = 'Communication attitude is often related to the ability to better transfer work to others.The requirements of the job coincide with your social attitude.'
    elif EI_ideal == 'E':
        comment_1 = 'Focusing on working with numbers or words and focuses on analyzing the characteristics of objective things will save a lot of awkwardness in interpersonal interactions.'
    else:
        comment_1 = 'Focusing on interpersonal communication is the best way to leverage your initiative.'

    NS_ideal = mbti_id_2[m]
    NS_suitable = n[7]
#     print(NS_ideal,NS_suitable)
    if NS_ideal == 'X' or NS_suitable == 'X' or NS_ideal == NS_suitable:
        comment_2 = "How you perceive determines how you perceive what's going on in the world.That's what this job requires."
    elif NS_ideal == 'N':
        comment_2 = 'Pay attention to detail and holistic is the strength your personality.'
    else:
        comment_2 = "Having a good sense of abstract things can help you find your comfort zone at work."

    TF_ideal = mbti_id_3[m]
    TF_suitable = n[8]
#     print(TF_ideal,TF_suitable)
    if TF_ideal == 'X' or TF_suitable == 'X' or TF_ideal == TF_suitable:
        comment_3 = 'The way you judge determines which dimension you are more used to measuring the value of things. It will be very usful in this work place.'
    elif NS_ideal == 'T':
        comment_3 = 'Make judgments based on emotional values will make you more caring and patient in your work.'
    else:
        comment_3 = "Make judgments based on logical value will enable you to accomplish your job requirements more efficiently and rigorously."

    PJ_ideal = mbti_id_4[m]
    PJ_suitable = n[9]
#     print(PJ_ideal,PJ_suitable)
    if PJ_ideal == 'X' or PJ_suitable == 'X' or PJ_ideal == PJ_suitable:
        comment_4 = 'Work habits determine whether you will be more suited to creative work or more disciplined in your work, and this job is exactly what you want.'
    elif NS_ideal == 'P':
        comment_4 = 'Your ability to build a structured framework is highly valued in this job.'
    else:
        comment_4 = "It will allow you to maximize your expertise in divergent thinking."

    comment_5 = ""

    ideal = EI_ideal +  NS_ideal + TF_ideal + PJ_ideal
    suitable = EI_suitable + NS_suitable + TF_suitable + PJ_suitable
    comment = comment_1 + "\n" + comment_2 + "\n" + \
        comment_3 + "\n" + comment_4 + "\n" + comment_5

    return ideal, suitable, comment

# A.管理 EXTJ
# B.工程 ISTJ
# C.法学 XSXJ
# D.艺术 IXFP
# E.服务 ESFX
# F.经济 XXTP
# G.理学 INTX
# H.传播 XNFP
# I.医学 XSFJ
# J.教育 EXFJ
# K.语言文学 INFP
# L.其他 XXXX


def description(m):
    if m == 0:
        index = 'This job needs people who are responsible, sincere and loyal to their duties. They should be able to enjoy frameworks, organize detailed work, meet goals on time and be efficient. Since careers are closely related to policies and personnel organization, it is important to be able to use time and resources efficiently to find logical solutions.'
    elif m == 1:
        index = 'The job requires people who can create and develop novel solutions to solve problems or improve existing systems; They must be willing to work with responsible people whose expertise, intelligence and abilities they admire. May be serious and quiet, but focus, finish what you start, and try to organize everything. And to be able to decide for themselves what to do without objecting or interfering, and to do it steadfastly.'
    elif m == 2:
        index = 'This job requires a person with strong logic, good judgment and great talent. They have creative minds and push their own ideas and goals. Vision and ability to quickly find meaningful patterns in external events. They have a great ability to organize and follow through in areas that appeal to them. Uncredulous, critical, independent, determined, with high standards of competence and action.'
    elif m == 3:
        index = 'This job requires someone who is flexible, tolerant, but committed to a cause whose heart is loyal. These people rarely show strong emotions and often appear calm and quiet. However, they can also become enthusiastic once they are committed to their careers. Such a person is capable of personal originality, of intellectual curiosity, of giving quick air to possibilities, and of often acting as a catalyst for the implementation of ideas.'
    elif m == 4:
        index = 'This job requires a caring person with a zest for life. They tend to be critical of themselves. But because they feel responsible for the feelings of others, they rarely criticize in public. They have a good sense of the merits of their actions and are good socialists. This person is best suited to work in a job where they build strong relationships and surround themselves with people they trust and who are creative.'
    elif m == 5:
        index = 'The job requires someone who is talkative, intelligent and sensitive to numbers. They are always striving to improve their abilities. This type of person is born with entrepreneurial heart, love to study, astute and fickle, strong adaptability. Resourceful in solving new and challenging problems and able to easily rationalize their demands.'
    elif m == 6:
        index = 'This job needs someone who is good at solving abstract problems. When they are full, they can flash a spark of creative wisdom. Outwardly quiet, inwardly focused, they are always busy analyzing problems. They are fastidious and highly independent. Capable of incubating new ideas; Focus on a creative process, not the final product. When solving complex problems, it allows them to think outside the box and take some risks to find the best solution.'
    elif m == 7:
        index = 'This job needs someone who is enthusiastic and full of new ideas. They are optimistic, spontaneous, confident and creative, and have a deep sense of what can be done. They are highly inspired, non-conformist, and good at breaking new ground. Extremely enthusiastic, energetic, alert, imaginative. Be able to do almost anything they are interested in.'
    elif m == 8:
        index = "This job requires loyal, single-minded, compassionate people who like to help others. Because such people have a strong work ethic, they will take on the burden if they feel their actions will help. Their most satisfying work is that which requires careful observation and exactness. They need to express their emotional involvement by quietly working behind the scenes, but their personal contributions need to be recognized. Quiet, friendly, responsible and serious. Perform one's duties with dedication. Can make any project or group more stable."
    elif m == 9:
        index = 'This job requires sensitivity and responsibility. Someone who truly cares about the wants and desires of others. They try to deal with things with due regard for the feelings of others. Able to make suggestions or lead group discussions with ease and tact. Social, popular and compassionate. Sensitive to praise and criticism. Like to make people convenient and enable people to achieve their potential. Be able to surround yourself with people you trust and who are creative.'
    elif m == 10:
        index = 'This job requires someone who is gentle, considerate and sensitive. They often express their burning emotions through actions, not words. This person is patient, flexible, easygoing and has no desire to control others. They are not judgmental or seek motive and meaning, and are often loyal followers. Because they enjoy the immediate pleasure, they often slack off and do not want to let excessive urgency and trouble spoil the enjoyment.'
    else:
        index = 'This job requires a pragmatist who likes to do more than talk. They must be analytical, observant, curious, and believe only in solid facts. Being very pragmatic, they make good use of all the resources at their disposal and have a good sense of timing. They are often interested in causes and effects, as well as logical principles that organize facts. Good at getting to the heart of practical problems and finding solutions.'

    return index


# # ideal job
# print(title[ideal_job])
# print(MBTI_comment(ideal_job, m)[0])
# print(description(m[5]), "\n\r")
# # suitable job
# print(title[suitable_job])
# print(MBTI_comment(ideal_job, m)[1])
# # comment
# print(MBTI_comment(ideal_job, m)[2])
