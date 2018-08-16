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
for i in range(0, len(list_num)):
    list_num[i] = list_num[i].strip()
print(list_num)
list_date = file_date.readlines()
for i in range(0, len(list_date)):
    list_date[i] = list_date[i].strip()
print(list_date)
list_feature = file_feature.readlines()
for i in range(0, len(list_feature)):
    list_feature[i] = list_feature[i].strip()
print(list_feature)
list_category = file_category.readlines()
for i in range(0, len(list_category)):
    list_category[i] = list_category[i].strip()
print(list_category)

#Error Code
def call_error():
    os.system("cls")
    print("*" * 70)
    print("*" * 70)
    print(" " * 25 + "<<<<<오류가 발생하였습니다. 처음부터 다시 시도해주세요!>>>>>")

# 엔터를 누르면 돌아갑니다 함수
def enter_delay():
    print("엔터를 누르면 이전 화면으로 돌아갑니다.")
    input()

# Export list to file
def export_to_file():
    file_num = open("list_num.txt" ,'w')
    file_category = open("list_category.txt",'w')
    file_date = open("list_date.txt",'w')
    file_feature = open("list_feature.txt",'w')

    file_num.write("\n".join(list_num))
    file_category.write("\n".join(list_category))
    file_date.write("\n".join(list_date))
    file_feature.write("\n".join(list_feature))
# <<<<<  Code Start    >>>>>

# 데이터 무결성 검증
def data_integrity_check():

    if(len(list_num) == len(list_date) == len(list_feature)):
        file_num.close()
        file_date.close()
        file_feature.close()
        file_category.close()

        return 0
    else:
        return 1




if data_integrity_check() == 1:
    print("=" * 70)
    print("   2018 부산정보영재교육원 고1 정보심화반 팀 프로젝트 | 오류 > 무결성 검증 통과 실패  Input File을 확인해주세요")
    print("=" * 70)
    print("\n")
    print("   프로그램을 실행하는데 필요한 데이터가 손상되었습니다.\n   프로그램이 5초 뒤 종료됩니다.")
    time.sleep(5)
    exit()
else:
    print("=" * 70)
    print("   2018 부산정보영재교육원 고1 정보심화반 팀 프로젝트 | 무결성 검증 완료")
    print("=" * 70)
    print("\n")
    print("   프로그램을 실행하는데 필요한 데이터의 검증에 성공하였습니다.\n   프로그램이 5초 뒤 실행됩니다.")
    #time.sleep(5)
    print("hello")
    # 프로그램 시작
    while True:
        # 메인 매뉴
        os.system("cls")
        print("=" * 70)
        print("   2018 부산정보영재교육원 고1 정보심화반 팀 프로젝트 | 메인메뉴 >")
        print("=" * 70)
        print("\n")
        print("   부산정보영재교육원 팀 프로젝트 - 분실물 찾기 프로그램\n\n\n   원하시는 메뉴를 선택해 주세요\n   1. 분실물 검색 / 2. 분실물 관리 / 3. 분실물 목록 보기 / 0. 프로그램 종료\n")
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
            search_until = len(list_num)
            for i in range(0, search_until):
                if(list_category[i].strip() == search_menu):
                    menu_index.append(i)
            for i in menu_index:
                print("일렬번호 : %4d   종류 : %s         날짜 : %d        특징 : %s" % (int(list_num[i]), list_category[i].strip(), int(list_date[i]), list_feature[i].strip() ))
            enter_delay()




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
                            os.system("cls")
                            print("<<관리자 비밀번호가 일치합니다>>")
                        #    time.sleep(3)
                            print("   2018 부산정보영재교육원 고1 정보심화반 팀 프로젝트 | 메인메뉴 > 분실물 관리")
                            print("=" * 70)
                            print("\n")
                            print("   ")
                            print("어느 작업을 수행하시겠습니까? \n     1. 분실물 등록\n     2.분실물 삭제")
                            selection = int(input())
                            if selection == 1:
                                found_no = len(list_num)
                                print("분실물 등록번호는 %d번 입니다" % found_no)
                                print("분실물의 종류를 선택해주세요 (1.옷  2.가방  3.지갑  4.학용품  5.전자기기  6.기타 )\n ->")
                                found_type = int(input())
                                print("\n\n")
                                print("분실물 습득 일자를 입력해주세요 ->")
                                found_date = int(input())
                                print("\n\n")
                                print("특징을 상세히 입력해주세요 ->")
                                found_feature = input()

                                #각각 list에 분실물 추가
                                list_num.append(str(found_no))

                                if(found_type == 1):
                                    list_category.append("옷")
                                elif(found_type == 2):
                                    list_category.append("가방")
                                elif(found_type == 3):
                                    list_category.append("지갑")
                                elif(found_type == 4):
                                    list_category.append("학용품")
                                elif(found_type == 5):
                                    list_category.append("전자기기")
                                elif(found_type == 6):
                                    list_category.append("기타")

                                list_date.append(str(found_date))
                                list_feature.append(found_feature)

                                os.system("cls")
                                print("정상 처리되었습니다.")
                                export_to_file()
                                print(list_num)
                                print(list_category)
                                print(list_date)
                                print(list_feature)
                                enter_delay()
                            if selection == 2:
                                search_range = len(list_num)
                                for i in range(0, search_range):
                                    print("일렬번호 : %3d     종류 : %s     습득날짜     %s       특징 : %s" % (int(list_num[i]), list_category[i], list_date[i], list_feature[i]))
                                print("\n\n삭제하실 물품의 일렬번호를 입력해주세요 ->")
                                del_input = int(input())
                                list_category[del_input] = '삭제된 물품입니다'
                                list_date[del_input] = '99999999'
                                list_feature[del_input] = '삭제된 물품입니다'
                                os.system("cls")
                                print("정상 처리되었습니다\n통계 집계를 위해 일렬번호는 사라지지 않습니다.")
                                enter_delay()


            else:
                print("관리자 패스워드가 일치하지 않습니다. 확인 후 다시 시도해주세요\n")
                enter_delay()



        elif m_menu == "0":
            os.system("taskkill /IM python.exe")

        elif m_menu == '3':
            for i in range(0, len(list_num)):
                print("일렬번호 : %3d     종류 : %s     습득날짜     %s       특징 : %s" % (int(list_num[i]), list_category[i], list_date[i], list_feature[i]))
            enter_delay()
        elif m_menu == '4':
            export_to_file()

        else:
            os.system("cls")
            print("=" * 70)
            print("   2018 부산정보영재교육원 고1 정보심화반 팀 프로젝트 | 오류")
            print("=" * 70)
            print("\n")
            print("   잘못된 메뉴를 입력하셨습니다. 다시 선택해 주세요 (5초 후 메뉴로 돌아갑니다.)")
            time.sleep(5)
