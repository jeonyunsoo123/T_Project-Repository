//This program was coded by JeonYunSoo. All copyrights reserved.
//Anyone who uses this code without permission will be accused for cyber theft.
//Thank you.
#include<stdio.h>
#include<windows.h>
int main_menu();
int hotel_checkin();
int hotel_checkout();
int view_availabe_room();
int administrator_mode();
int hotel_room_array[10][10]= {0};
int hotel_room_stay_people_number_kid[10][10] = {0};
int hotel_room_stay_people_number_teen[10][10] = {0};
int hotel_room_stay_people_number_adult[10][10] = {0};
int main(){
    main_menu();

}

int clear_page(){
printf("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");}

int main_menu(){
int menu_selection;
    clear_page();
    printf("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n");
    printf("||                                                                             ||\n");
    printf("||                                                                             ||\n");
    printf("||                     Welcome to Hotel Management Program                     ||\n");
    printf("||                                                                             ||\n");
    printf("||                                                                             ||\n");
    printf("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n\n");
    printf("||1. Hotel Checkin 2.Hotel Checkout 3.View Available Rooms 4.Administration Mode|\n\n");
    printf("||             Input Your Selection of Options : ");
    scanf("%d",&menu_selection);
    if(menu_selection==1){hotel_checkin();};
    if(menu_selection==2){hotel_checkout();};
    if(menu_selection==3){view_availabe_room();};
    if(menu_selection==4) {administrator_mode();};
    if(menu_selection!=1 || 2 || 3 || 4) {
        clear_page();
        printf("Error! Invalid Integer input.\n Restarting Program");
        Sleep(3000);
        main_menu();
        }
    }
int hotel_checkout(){
    clear_page();
    printf("We wish you had a great time at our hotel.\n Now we will help you with your check out after your payment completes.\n\n");
    Sleep(5000);
    clear_page();
    printf("please input the room number in a form of <number> 0 <number> : ");
    int input_checkout_x,input_checkout_y;
    scanf("%d 0 %d",&input_checkout_x,&input_checkout_y);

    clear_page();
    if(hotel_room_array[input_checkout_x][input_checkout_y] != 1){
        printf("There is NO VALID DATA for this room. \n Check your room number and try again or contact one of our staffs.");
        Sleep(3000);
        main_menu();
    }
    printf("Hello! Customer from room %d0%d!.\n We will now help you with your checkout.\n Please check the following Informations.\n\n\n",input_checkout_x,input_checkout_y);
    printf("-----------Payment Report-------------\n");
    printf("Room number : %d0%d\n",input_checkout_x,input_checkout_y);
    printf("Number of Kid Stayers : %d\n\n",hotel_room_stay_people_number_kid[input_checkout_x][input_checkout_y]);
     printf("Number of Teen Stayers : %d\n\n",hotel_room_stay_people_number_teen[input_checkout_x][input_checkout_y]);
     printf("Number of Adult Stayers : %d\n\n",hotel_room_stay_people_number_adult[input_checkout_x][input_checkout_y]);
    printf("Room price : 400 USD\n\n");
    printf("Additional cost for extra people : %d USD \n\n\n",30*(hotel_room_stay_people_number_kid[input_checkout_x][input_checkout_y])+40*(hotel_room_stay_people_number_teen[input_checkout_x][input_checkout_y])+50*(hotel_room_stay_people_number_kid[input_checkout_x][input_checkout_y]));
    printf("Total Payment : %d\n",400+30*(hotel_room_stay_people_number_kid[input_checkout_x][input_checkout_y])+40*(hotel_room_stay_people_number_teen[input_checkout_x][input_checkout_y])+50*(hotel_room_stay_people_number_kid[input_checkout_x][input_checkout_y]));
    printf("--------------------------------------\n\n");
    Sleep(9000);
    clear_page();
    printf("To continue with your payment please contact our staff.\n\n");
    printf("STAFF_PASSWORD : ");
    int staff_password;
    scanf("%d",&staff_password);
    if(staff_password!=1234567890) { clear_page(); printf("Error. Please Start Again."); Sleep(3000); hotel_checkout();}

    clear_page();
    printf("Your checkout process is complete. Please return the key card to our staff\n\n");
    hotel_room_array[input_checkout_x][input_checkout_y]= 0;
    hotel_room_stay_people_number_kid[input_checkout_x][input_checkout_y] = 0;
    hotel_room_stay_people_number_teen[input_checkout_x][input_checkout_y] = 0;
    hotel_room_stay_people_number_adult[input_checkout_x][input_checkout_y] = 0;
    Sleep(3000);
    main_menu();
}
int hotel_checkin(){
    int checkin_array_x,checkin_array_y;
    clear_page();
    printf("    1  2  3  4  5  6  7  8  9\n\n");
    printf("1  �� �� �� �� �� �� �� �� ��                       These are the rooms we have in our hotel\n\n");
    printf("2  �� �� �� �� �� �� �� �� ��\n\n");
    printf("3  �� �� �� �� �� �� �� �� ��\n\n");
    printf("4  �� �� �� �� �� �� �� �� ��                       Please Select the room you hope to stay.\n\n");
    printf("5  �� �� �� �� �� �� �� �� ��\n\n");
    printf("6  �� �� �� �� �� �� �� �� ��\n\n");
    printf("7  �� �� �� �� �� �� �� �� ��\n\n");
    printf("8  �� �� �� �� �� �� �� �� ��                         <IMPORTANT> Notice for Selection\n\n");
    printf("9  �� �� �� �� �� �� �� �� ��             Room selection should be (X array) <Space> 0 <Space> (Y array)\n\n");

    printf("\n             <IMPORTANT> PLEASE FOLLOW THE INPUT METHOD MENTIONED ABOVE <IMPORTANT>\n\n");
    printf(" Input your Room selection : ");
    scanf("%d 0 %d",&checkin_array_x,&checkin_array_y);
     if(checkin_array_x>=10 || checkin_array_y >=10) {
        clear_page();
        printf("I'm sorry. Input Value out of normal range. Please try again.\n Restarting Program ");
        Sleep(3000);
        main_menu();
    }
    clear_page();
    if( hotel_room_array[checkin_array_x][checkin_array_y]){
            printf("I'm sorry. The Room you have selected is already being used. \n Please select another room. \n Restarting program...");
            Sleep(3000);
            hotel_checkin();
    }
    printf("\n\n\n<IMPORTANT NOTICE>      HOTEL ROOM CONFIRMATION      <IMPORTANT NOTICE>\n");
    printf("The room you have selected is  %d0%d  Is that correct?(y/n) : ",checkin_array_x,checkin_array_y);

   // printf ("\n\n %d %d \n\n",q,s);

    char room_confirmation;
    int staying_people_number_kid,staying_people_number_teen,staying_people_number_adult;
    getchar();
    scanf("%c",&room_confirmation);
    if(room_confirmation=='y'){
         //   int count=0;0 ;
        hotel_room_array[checkin_array_x][checkin_array_y] = 1; //count ++;
        clear_page();
        printf("\n\n Please input the number of Kids staying in the hotel room : ");
        scanf("%d",&staying_people_number_kid);
         printf("\n\n Please input the number of Teens staying in the hotel room : ");
        scanf("%d",&staying_people_number_teen);
         printf("\n\n Please input the number of Adults staying in the hotel room : ");
        scanf("%d",&staying_people_number_adult);
        if(staying_people_number_kid + staying_people_number_teen + staying_people_number_adult>=7) {
                clear_page();
                printf("You have exceeded the maximum number of intake. Please retry at a value under 7.\n Program Will restart");
                Sleep(3000);
                hotel_checkin();
        }
        hotel_room_stay_people_number_kid[checkin_array_x][checkin_array_y] = staying_people_number_kid;
        hotel_room_stay_people_number_teen[checkin_array_x][checkin_array_y] = staying_people_number_teen;
        hotel_room_stay_people_number_adult[checkin_array_x][checkin_array_y] = staying_people_number_adult;
        clear_page();

        //printf("\n\n %d \n\n",staying_people_number);
        printf("Thank you. Your Check In is successful. \nYour room number is %d0%d. \n Thank you for visiting our hotel.",checkin_array_x,checkin_array_y);
      //  printf("%d\n\n\n",count);
  /*     int i,j;
        for( i=1;i<10;i++){
            for( j=1;j<10;j++){
                printf("%d  ",hotel_room_array[i][j]);}}

    printf("\n\n\n");


        for( i=1;i<10;i++){
            for( j=1;j<10;j++){
                printf("%d  ",hotel_room_stay_people_number[i][j]);}}*/
        Sleep(5000);
        clear_page();
        main_menu();
    }
    else if(room_confirmation=='n'){
        printf("Sorry Wrong INPUT. Restarting Program");
        Sleep(3000);

        hotel_checkin();
    }
    else hotel_checkin();

}
int view_availabe_room() {
    clear_page();
    int i,j;
    printf("Checking the rooms for you. Please wait.\n\n");
    for(i=1;i<10;i++){
        for(j=1;j<10;j++){
        if(hotel_room_array[i][j]==1) printf("Room : %d0%d is Unavailable\n",i,j);
        if(hotel_room_array[i][j]!=1) printf("Room : %d0%d is Available\n",i,j);
        }}
printf("\n\nPress Any Key to go back to Home Screen...");
getchar();
main_menu();
}
int administrator_mode(){
    clear_page();
    printf("\nThis menu is for administrator ONLY.");
    printf("\nIn order to protect customer data this section is digitally sealed with password.");
    Sleep(3000);
    clear_page();
    printf("ADMINISTRATOR PASSWORD : ");
    int admin_pass;
    scanf("%d",&admin_pass);
    if(admin_pass == 1234567890){
        printf("Loading All Database DATA..... \n\n Please wait.");  Sleep(1000);clear_page();
        printf("Loading All Database DATA..... \n\n Please wait..");  Sleep(1000);clear_page();
        printf("Loading All Database DATA..... \n\n Please wait...");  Sleep(1000);clear_page();
        printf("Loading All Database DATA..... \n\n Please wait.");  Sleep(1000);clear_page();
        printf("Loading All Database DATA..... \n\n Please wait..");  Sleep(1000);clear_page();
        printf("Loading All Database DATA..... \n\n Please wait...");  Sleep(1000); clear_page();
        int i,j;
       printf("Hotel Room Availability\n");
        for(i=1;i<10;i++){
        for(j=1;j<10;j++){
        if(hotel_room_array[i][j]==1) printf("Room : %d0%d is Unavailable\n",i,j);
        if(hotel_room_array[i][j]!=1) printf("Room : %d0%d is Available\n",i,j);
        }}
        int counta=0;
        printf("\n\n\nNumber of kids in each room\n");
        for(i=1;i<10;i++){
        for(j=1;j<10;j++){
            printf("Room %d0%d has %d kids.\n",i,j,hotel_room_stay_people_number_kid[i][j]);
            counta= counta+hotel_room_stay_people_number_kid[i][j];

        }}
        printf("\n\n\nNumber of teens in each room\n");
        for(i=1;i<10;i++){
        for(j=1;j<10;j++){
            printf("Room %d0%d has %d teens.\n",i,j,hotel_room_stay_people_number_teen[i][j]);
            counta= counta+hotel_room_stay_people_number_teen[i][j];
        }}

        printf("\n\n\nNumber of adults in each room\n");
        for(i=1;i<10;i++){
        for(j=1;j<10;j++){
            printf("Room %d0%d has %d adults.\n",i,j,hotel_room_stay_people_number_adult[i][j]);
            counta= counta+hotel_room_stay_people_number_adult[i][j];
        }}
        printf("\n\n There are Total %d people in the hotel now.",counta);
        getchar();


    }
}
