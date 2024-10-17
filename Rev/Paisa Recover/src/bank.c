#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h> 
#include <openssl/md5.h>

// Global variables
char accnm[] = "78601";
char enc[] = "L0";
char khatm[] = "_5ucc3s";
char waste[] = "w45t3_yr_T1M3}";
char start[] = "CCC{";


void garbage(){
 char strings[20][50]; 
    strcpy(strings[0], "sfrgs");
    strcpy(strings[1], "adadawd");
    strcpy(strings[2], "this");
    strcpy(strings[3], "adadads");
    strcpy(strings[4], "is");
    strcpy(strings[5], "ajddundq2323r2nr2rj2r2");
    strcpy(strings[6], "CCC{N4kL1_jh4nD4}");
    strcpy(strings[7], "String 8");
    strcpy(strings[8], "String 9");
    strcpy(strings[9], "hgfdvb576");
    strcpy(strings[10], "String 11");
    strcpy(strings[11], "String 12");
    strcpy(strings[12], "String 13");
    strcpy(strings[13], "String 14");
    strcpy(strings[14], "String 15");
    strcpy(strings[15], "String 16");
    strcpy(strings[16], "String 17");
    strcpy(strings[17], "String 18");
    strcpy(strings[18], "String 19");
    strcpy(strings[19], "String 20");
    for (int i = 0; i < 20; i++) {
        printf("String %d: %s\n", i + 1, strings[i]);
    }
}

bool validateAccount(const char *input) { //FANGISPRO00690245678
    if (strlen(input) > 20) {
        return false; 
    }

    if (input[0] != 'F' ||
        input[1] != 'A' ||
        input[6] == 'D' ) {
        return false; 
    }
    
    char output[100]; 
    int i = 0;
    while (input[i] != '\0') {
        
        char transformedChar = input[i] + 3;
        output[i] = transformedChar - 10;
        i++;
    }
    output[i] = '\0';
    char compareString[] = "?:G@BLIKH))/2)+-./01";
    return (strcmp(output, compareString) ==0) ;
    return true; 
}

char hash[] = "8a608da82af5e0db";

int sumAscii(char *str) {
    int sum = 0;
    for (int i = 0; str[i] != '\0'; i++) {
        sum += str[i];}
    return sum;
}

// Function to display the main menu
void displayMainMenu() {
    printf("\nWelcome Mr. Levi\n");
    printf("1. Files\n");
    printf("2. Bank\n");
    printf("3. Flag??\n"); }

// Function to display the file menu
void displayFileMenu() {
    printf("\nVictims:\n");
    printf("1. Viqas\n");
    printf("2. Kayani\n");
    printf("3. FANG\n");
    printf("\n");}

// Function to display the bank menu
void displayBankMenu() {
    printf("\n1. Send money\n");
    printf("2. Receive money\n");
    printf("3. Quit\n");
    printf("\n");}

void viqas() {
    printf("\nName: viqas\n");
    printf("Account Number: CIDP729485G633726253\n");
    printf("Note: thorey paise hamein bhi dedo viqas ji\n");
    printf("\n");
}

void kayani() {
    printf("\nName: Kayani\n");
    printf("Account Number: SUII0900786015654398\n");
    printf("Note: Bad Day At Office\n");
    printf("\n");
}

void FANGI() {
    int flag = 0;
    char accnum[] = "FOR0l";  
    printf("\nName: FANG\n");
    printf("Account Number: ");
    if (flag == 1) {
      
      printf("Rk%s%s", accnum,enc);
      printf("\n");}
      
    else{
      printf("\n Oh..no we have ran into a slight problem, the account number has been corrupted");
      flag =+1; }
    printf("Note: FANG my inspiration\n");
    printf("\n");
}

void checkout(){
  char msg[] = "P4ym3nt_";
  printf("%s",msg);
  }
  
void withdrawn(char* Acc){
  printf("to_%s_",Acc);
}
  
// Function to validate password
int validatePassword(char *inputPassword) { //s3cur3p4sswd
    int correctSum = 1160; 

    if (inputPassword[0] != 's' || inputPassword[2] == 'b' || inputPassword[3] != 'u'  || inputPassword[9] == '6' || inputPassword[7] != '4' ) return false;
   
    int inputSum = sumAscii(inputPassword);
    // Compare the sums
    if (inputSum == correctSum) {
        return 1; 
    } else {
        return 0; 
    }
    
}

int amount(){
   int num = 500000;
   int count = 5;
   if (count == 0) {
        return 1;  
    }
    
    int n = 454;
    int m = 3;
    
    return n * amount(n, m, count - 1);
  
    for (int i = 0; i < 100; i++) {
          if (num > 400000){ //dummy loop
              num = num / 2;
          }
          if (num < 400000){
            num = num + 3;
            
          }
      }
}


const char* getHash(int input) {

    static char result[100];  
    if (input == getAmount()) {
        
        strcpy(result, "d87dc2090f3a1c5f");
        strcat(result, hash);
        return result;
    }
    return NULL;
}

int multiply_recursively(int num, int count) {
    if (count == 0) {
        return num; 
    }
    return multiply_recursively(num * 3, count - 1); 
}

int getAmount() {
    int baseNumber = 454; 
    int res = multiply_recursively(baseNumber, 5); 
    res += 59681;
    printf("%d",res);
    return res; 
}

void secret(){
  
  char reply[1];
  printf("Wanna know a secret? [Y/N]");
  scanf("%s",reply);
  
  if (strcmp(reply, "Y") == 0 || strcmp(reply, "y") == 0){
    char flag1[] = "This_fl4g_is";
    char flag2[] = "_the_flag";
    printf("wait 20 seconds\n ");
     printf("Loading...");
    // Loop for 20 seconds
    for (int i = 0; i < 20; i++) {
        printf(".");
        fflush(stdout); 
        sleep(1); 
    }

    printf("\nCCC{%s_jus5_t0_%s.\n",flag1,waste);}
    
  else if (strcmp(reply, "N") == 0 || strcmp(reply, "n") == 0){
          printf("bye then");
  }
  else {
      printf("wrong choice buddy ");
    }
}

char accnum2[] = "0900";

void transaction(int check, int check2){
  if (check == 0xdeadbeef && check2 == 0xdeadface ){
                    
            char Name[4];
		    char enteredAccountNum[11];
		    int enteredAmount;
            printf("\n");
            printf("\n");
		    printf("Enter account name: ");
		    scanf("%s", Name);
		    //printf("%s",Name);
		    printf("Enter account number: ");
		    scanf("%s", enteredAccountNum);
		    printf("Enter amount: ");
		    scanf("%d", &enteredAmount);
		    printf("\n");
		    printf("\n");
		    
		    if (validateAccount(enteredAccountNum) && enteredAmount == getAmount()){
		        
		        printf("\n");
		        printf("\n");
		        printf("\n");
		        printf("************** INVOICE **************\n");
                printf("  Description: Money Transfer        \n");         
                printf("Amount Rs: %d\n",enteredAmount);
                printf("-------------------------------------\n");
                printf("%s",start);
                checkout();
                printf("%s%s}\n",khatm,getHash(enteredAmount));         
                printf("-------------------------------------\n");;
                return ;
                         
		    } else { printf("Error in transaction\n");  return ;
		}
    }else{  printf("Oops, youre missing something, i believe\n");}
}


int main() {
    //secret();
    char password[20];
    int choice = -1;
    int choice2;
    int tries = 3;
    int checkVal = 0xc0debab3;
    int checkval2 = 0xdefec8ed;
    

    while (tries != 0){
        // Prompt user for password
    printf("Enter the password: ");
    scanf("%s", password);
    
    
    
    // Validate password based on sum of ASCII values
    if (validatePassword(password)) {
        printf("Password accepted!\n");
        char flagpart2[] = "fu1_";
        strcat(khatm, flagpart2);
        
        
        // Display main menu options
      while (choice != 0){
        displayMainMenu();
        printf("Enter your choice: ");
        scanf("%d", &choice);
        
      
        	// Perform actions based on user's choice
            
        switch (choice) {
            case 1:
                displayFileMenu();
                printf("Enter your choice: ");
                scanf("%d", &choice2);
                
                switch (choice2) {
                    case 1:
                        viqas();
                        break;
                    case 2:
                        kayani();
                        break;
                    case 3:
                    	printf("Oops.....we have a problem receiving your data\n");
                    	printf("There seems to an error with a function call\n");
                        //black();
                        break;
                    default:
                        printf("Invalid choice\n");
                }
                break;
            case 2:
                // Display bank menu options
                displayBankMenu();
                printf("\n");
                printf("Enter your choice: ");
                printf("\n");
                scanf("%d", &choice);
                
                // Perform actions based on user's choice in bank menu
                switch (choice) {
                    case 1:
                    int cash = 0;
                    if (cash == 1){
                      transaction(checkVal, checkval2);
                    }
                    else{printf("sorry were having some trouble, Aerys pwned our system....u gotta find another way");
                    cash ++;}
                    
		    
		    break;
		    
                        
                        break;
                    case 2:
                         printf("waiting for your. payment..\n");
                          // Loop for 20 seconds
                          for (int i = 0; i < 20; i++) {
                              printf(".");
                              fflush(stdout); 
                              sleep(1); 
                          }
                        printf("nhi milne paise, ja kaam kar'\n");
                        break;
                    case 3:
                        printf("Quitting bank menu\n");
                        break;
                    default:
                        printf("Invalid choice\n");
                }
                break;
            case 3:
            char flag2[]= "_f4k3}";
            char flag1[] = "th15_15";
                printf("CCC{%s%s\n", flag1,flag2);
                return 0;
                
                break;
                break;
            default:
                printf("Invalid choice\n");
       	 	}
        }

        
    } 
    else {
    tries --;
        printf("you get %d more chances.\n",tries);
        
        continue;
    }
    
    }
    printf("\n\nGive up on your dreams and die");
    
    return 0;
}


