'''
2018 Busan Gifted Computer Education Center (High school 1st grade) Team Project

Member = Semin Park, Hyunseo Lee, Yunsoo Jeon
Date = 2018. 08. 15.
'''

# Import
import os
import time


# List
file_num = open("list_num.txt" ,'r')
file_category = open("list_category.txt",'r')
file_date = open("list_date",'r')
file_category = open("list_feature",'r')
list_num = []
list_category = []
list_date = []
list_feature = []
admin_passwd = "password"


# Code
def data_integrity_check():
    if(len(list_num) == len(list_date) == len(list_feature) == len(list_category)):
        return 0
    else
        return 1

if data_integrity_check == "1":
    print("=" * 70)
    print("   2018 부산정보영재교육원 고1 정보심화반 팀 프로젝트 | 오류 > 무결성 검증 통과 실패")
    print("=" * 70)
    print("\n")
    print("   프로그램을 실행하는데 필요한 데이터가 손상되었습니다.\n   프로그램이 5초 뒤 종료됩니다.")
    time.sleep(5)
    break
elif data_integrity_check == "0":
    print("=" * 70)
    print("   2018 부산정보영재교육원 고1 정보심화반 팀 프로젝트 | 무결성 검증 완료")
    print("=" * 70)
    print("\n")
    print("   프로그램을 실행하는데 필요한 데이터의 검증에 성공하였습니다.\n   프로그램이 5초 뒤 실행됩니다.")
    time.sleep(5)
    while True:
        os.system("cls")
        print("=" * 70)
        print("   2018 부산정보영재교육원 고1 정보심화반 팀 프로젝트 | 메인메뉴 >")
        print("=" * 70)
        print("\n")
        print("   부산정보영재교육원 팀 프로젝트 - 분실물 찾기 프로그램\n")
        print("\n\n")
        print("   원하시는 메뉴를 선택해 주세요\n   1. 분실물 검색 / 2. 분실물 관리 / 0. 프로그램 종료\n")
        m_menu = input("")
        if m_menu == "1":
            os.system("cls")
            print("=" * 70)
            print("   2018 부산정보영재교육원 고1 정보심화반 팀 프로젝트 | 메인메뉴 > 분실물 검색")
            print("=" * 70)
            print("\n")
            print("   분실물을 검색하는 메뉴입니다.\n")

        elif m_menu == "2":
            os.system("cls")


        elif m_menu == "0":
            break

        else:
            os.system("cls")
            print("=" * 70)
            print("   2018 부산정보영재교육원 고1 정보심화반 팀 프로젝트 | 오류")
            print("=" * 70)
            print("\n")
            print("   잘못된 메뉴를 입력하셨습니다. 다시 선택해 주세요 (5초 후 메뉴로 돌아갑니다.)")
            time.sleep(5)
