'''
2018 Busan Gifted Computer Education Center (High school 1st grade) Team Project

Member = Semin Park, Hyunseo Lee, Yunsoo Jeon
Date = 2018. 08. 15.
'''

# Import
import os
import time

# Open File
file_num = open("list_num.txt" ,'r')
file_category = open("list_category.txt",'r')
file_date = open("list_date.txt",'r')
file_feature = open("list_feature.txt",'r')

#List
list_num = []
list_category = []
list_date = []
list_feature = []
admin_passwd = "password"

# Data Reading from File to List
list_num = file_num.readlines()
list_date = file_date.readlines()
list_feature = file_feature.readlines()
list_category = file_feature.readlines()

# <<<<<  Code Start    >>>>>

# 데이터 무결성 검증
def data_integrity_check():
    if(len(list_num) == len(list_date) == len(list_feature)):
        return 0
    else:
        return 1

if data_integrity_check == "1":
    print("=" * 70)
    print("   2018 부산정보영재교육원 고1 정보심화반 팀 프로젝트 | 오류 > 무결성 검증 통과 실패  Input File을 확인해주세요")
    print("=" * 70)
    print("\n")
    print("   프로그램을 실행하는데 필요한 데이터가 손상되었습니다.\n   프로그램이 5초 뒤 종료됩니다.")
    time.sleep(5)
    exit()
elif data_integrity_check == "0":
    print("=" * 70)
    print("   2018 부산정보영재교육원 고1 정보심화반 팀 프로젝트 | 무결성 검증 완료")
    print("=" * 70)
    print("\n")
    print("   프로그램을 실행하는데 필요한 데이터의 검증에 성공하였습니다.\n   프로그램이 5초 뒤 실행됩니다.")
    time.sleep(5)

    # 프로그램 시작
    while True:
        # 메인 매뉴
        os.system("cls")
        print("=" * 70)
        print("   2018 부산정보영재교육원 고1 정보심화반 팀 프로젝트 | 메인메뉴 >")
        print("=" * 70)
        print("\n")
        print("   부산정보영재교육원 팀 프로젝트 - 분실물 찾기 프로그램\n\n\n   원하시는 메뉴를 선택해 주세요\n   1. 분실물 검색 / 2. 분실물 관리 / 0. 프로그램 종료\n")
        m_menu = input()
        if m_menu == "1":
            # 분실물 검색 메뉴
            os.system("cls")
            print("=" * 70)
            print("   2018 부산정보영재교육원 고1 정보심화반 팀 프로젝트 | 메인메뉴 > 분실물 검색")
            print("=" * 70)
            print("\n")
            print("   분실물을 검색하는 메뉴입니다.\n\n   해당하는 분실물의 종류를 알맞게 입력해 주세요.\n   (분실물 입력 종류 : 옷, 가방, 지갑, 학용품, 전자기기, 기타)")
            search_menu = input()
            menu_index = []



        elif m_menu == "2":
            # 분실물 관리 메뉴
            os.system("cls")
            print("=" * 70)
            print("   2018 부산정보영재교육원 고1 정보심화반 팀 프로젝트 | 관리자 권한 필요")
            print("=" * 70)
            print("\n")
            print("   분실물 관리 메뉴는 관리자 권한이 필요합니다.\n   아래에 관리자 비밀번호를 입력해 주세요 \n password =>")
            password = input()
            if password == admin_passwd:
                            print("   2018 부산정보영재교육원 고1 정보심화반 팀 프로젝트 | 메인메뉴 > 분실물 관리")
                            print("=" * 70)
                            print("\n")
                            print("   ")
            else:
                print("관리자 패스워드가 일치하지 않습니다. 확인 후 다시 시도해주세요\n")


        elif m_menu == "0":
            exit()

        else:
            os.system("cls")
            print("=" * 70)
            print("   2018 부산정보영재교육원 고1 정보심화반 팀 프로젝트 | 오류")
            print("=" * 70)
            print("\n")
            print("   잘못된 메뉴를 입력하셨습니다. 다시 선택해 주세요 (5초 후 메뉴로 돌아갑니다.)")
            time.sleep(5)
