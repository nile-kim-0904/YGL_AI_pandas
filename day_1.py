#!/usr/bin/env python
# coding: utf-8

# In[1]:


#시리즈: 1차원 배열 -> 인덱스와 값이 존재
import pandas as pd # pandas의 자료구조는 series와 dataframe이 존재


# In[3]:


dict_data = {'a':1,'b':2,'c':3}
list_data = [1,2,3]

srd = pd.Series(dict_data)
srl = pd.Series(list_data)

#print(type(dict_data),dict_data)
#print(type(srd),srd)
#print(type(list_data),list_data)
#print(type(srl),srl)


# In[6]:


#인덱스 확인
print("srd.index",srd.index)
print("srl.index",srl.index)

#시리즈의 값을 확인
print("srd.values",srd.values)
print("srl.values",srl.values)


# In[17]:


#각 자료의 원소 선택
sr_data = pd.Series(list(range(10)))
#srl[idx_start:idx_end] start 포함, end 포함 안함
sr_data[1:4]
srd['a']
srd['a':'c']


# In[21]:


sr_key = pd.Series({'a':1,'b':2,'c':3,'d':4,'e':5})
sr_key[['a','d']]

print(sr_key['a':'c']) #'c'를 포함
print(sr_key[0:2]) #인덱스 첨자는 2를 포함 안함


# In[40]:


sr_list = pd.Series(list(range(5)),index=['a','b','c','d','x'])
sr_list
sr_list1 = pd.Series(list(range(10)),index=[x for x in 'abcdefghij'])


# In[47]:


# 마지막 자료를 출력
print(sr_list[-1:])
print()
# 1번째부터 3번째까지의 자료 출력, 인덱스명으로도 출력
print(sr_list[1:4], '\n', sr_list1['b':'e'])
print()
# 인덱스명 'b'와 'd'의 값을 출력
print(sr_list[['b','d']])


# In[50]:


# dataframe: 2차원, pandas.DataFrame(data(2차원),[index= ],[columns= ]) -> []는 생략 가능
# dictionary 데이터로 데이터프레임 생성
dict_data = {'c0':[1,2,3],'c1':[4,5,6],'c2':[7,8,9]}
df = pd.DataFrame(dict_data)
df


# In[64]:


# dataframe -> index명과 column명을 부여
df = pd.DataFrame([[15,'남','수리중'],[17,'여','덕명중']],index=['준서','예은'],columns=['나이','성별','학교'])
df


# In[87]:


# 인덱스명을 변경 -> 행 인덱스, 열 이름
# 객체명.index = 새로운 인덱스명
# 객체명.columns = 새로운 컬럼명
df.index = ['a','b']
df
df.columns = ['연령','남녀','소속']
df

# 일부 인덱스명만 수정
# 객체명.rename(index={기존인덱스:새로운인덱스, ...})
# 객체명.rename(columns={기존컬럼명:새로운컬럼명, ...})
# '남녀'를 '성별'로 컬럼 변경, 'a'를 '준서'로 변경
df.rename(index={'a':'준서'},columns={'남녀':'성별'},inplace=True)
df


# In[88]:


# 새로운 행을 추가 df.loc['인덱스명'] = [값, ...] 또는 df.인덱스명 = 값
df.loc['철수'] = [17,'남','덕명중']
df


# In[91]:


# 행과 열을 삭제
# 행 삭제 -> 객체.drop(행인덱스 또는 배열, axis=0)
# 열 삭제 -> 객체.drop(열이름 또는 배열, axis=1)
df.drop('준서',axis=0)
df.drop('성별',axis=1)


# In[107]:


# 이름을 키로, 국어, 영어, 수학, 과학 점수를 값으로
# 입력받아 dictionary에 저장한 후
# 해당 자료를 데이터 프레임으로 전환 -> 인덱스명은 이름으로
dict_score = {}
def create_student():
    while True:
        name = input("이름 입력 > ")
        if(name=='q'):
            break
        score = list(map(int,input("국어 영어 수학 과학 점수 입력 > ").split()))
        dict_score[name] = score
    print(dict_score)

create_student()
df = pd.DataFrame(dict_score)
df = df.transpose()
df.columns = ['국어','영어','수학','과학']
df


# - 데이터프레임은 2차원: 시리즈가 여러개
# - pandas.DataFrame(2차원배열 또는 딕셔너리, index=, columns= )
# - 딕셔너리는 key가 컬럼명으로 됨
# - 딕셔너리의 키를 인덱스명으로 지정하면서 데이터프레임으로 변환
#     -- pandas.DataFrame.from_dict(딕셔너리데이터, origin='index')
# - 데이터프레임의 특정 컬럼을 인덱스로 변환
#     -- 데이터프레임.set_index('컬럼명')
#     
# - 인덱스를 변경: 데이터프레임.index = [인덱스명, ...]
# - 컬럼명을 변경: 데이터프레임.columns = [컬럼명, ...]
# - 일부 인덱스 이름을 변경: 데이터프레임.rename({old_idx:new_idx, ..}, inplace= )

# In[146]:


exam_data = {'수학':[90,80,70],'영어':[99,89,95],
            '음악':[85,95,100],'체육':[100,90,100]}
df = pd.DataFrame(exam_data,index=['서준','우현','인아'])
print(df)


# In[147]:


# 행 인덱스명을 사용하여 1개 행 선택 ('서준')
print(df.loc['서준'])
# 행 인덱스(정수)를 사용하여 1개 행 선택 (0행)
print(df.iloc[0])

# 두개의 행을 선택 '서준','우현'
print(df.loc[['서준','우현']])
print(df.iloc[[0,1]])

print(df.loc['서준':'우현'])
print(df.iloc[0:1])


# In[148]:


# 컬럼을 선택: df.컬럼명 또는 df['컬럼명']
#print(df.수학,'\n',df['영어'])
print(df[['수학','음악']])


# In[149]:


# 범위 슬라이싱: 객체.iloc[start:end:step]
df.iloc[0:3:1]
df.iloc[::-1]
df.iloc[::2]


# In[150]:


# 데이터프레임의 각 원소를 선택
# 인덱스 이름: 데이터프레임 객체.loc[인덱스명, 컬럼명]
# 정수 위치 인덱스: 데이터프레임 객체.iloc[행번호, 열번호]
# 서준의 여어 점수를 출력
print(df.loc['서준','영어'],df.iloc[0,1])

# 서준과 인아의 영어와 음악점수를 출력
df.loc[['서준','인아'],['영어','음악']]

# 서준부터 인아까지, 수학부터 음악까지
df.loc['서준':'인아','수학':'음악']
df.iloc[:,:-1]

# 서준의 수학과 체육 점수만 출력
df.loc[['서준'],['수학','체육']]
#df.iloc[0,[0,3]]
df.loc['철수']=[80,90,100,90]
df
# 새로운 열 추가: 데이터프레임 객체['컬럼명'] = 값
df['국어'] = [100,80,90,100]
df
# 기존의 행을 복사해서 추가
df.loc['추가'] = df.loc['서준']
df


# In[172]:


# 이름,국어,영어,수학 점수를 입력받아, 이름을 인덱스로 데이터 프레임에 저장
# df를 출력
# 이름을 입력받아 데이터프레임의 자료를 검색해서 출력
# 이름과 과목을 입력 받아 데이터 출력
dict_score = {}
def create_score():
    while True:
        name = input("이름 입력 > ")
        if(name=='q'):
            break
        score = list(map(int,input("국어 영어 수학 점수 입력 > ").split()))
        dict_score[name] = score

def search_score():
    name = input("이름 입력 > ")
    if name in df.index:
        print(df.loc[[name]])
    else:
        print("이름이 존재하지 않습니다")

def search_title():
    name = input("이름 입력 > ")
    if name in df.index:
        subject = input("과목 입력 > ")
        if subject in df.columns:
            print(df.loc[[name],subject])
        else:
            print("과목이 존재하지 않습니다")
    else:
        print("이름이 존재하지 않습니다")
    
def add_score():
    subject = input("과목 입력 > ")
    score = list(map(int,input("점수 입력 > ").split()))
    df[subject] = score
    print(df)
    
create_score()

df = pd.DataFrame(dict_score)
df = df.transpose()
df.columns = ['국어','영어','수학']
df

search_score()
search_title()
add_score()
df


# In[ ]:




