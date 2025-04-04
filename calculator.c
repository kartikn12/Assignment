#include<stdio.h>

addition()
{
	int a,b;
	printf("\nEnter First Number: ");
	scanf("%d",&a);
	printf("Enter Second Number:");
	scanf("%d",&b);
	printf("\nYour addition is %d\n",a+b);
}

subtraction()
{
	int a,b;
	printf("\nEnter First Number: ");
	scanf("%d",&a);
	printf("Enter Second Number:");
	scanf("%d",&b);
	printf("Your subtraction is %d\n",a-b);
}

multipication()
{
	int a,b;
	printf("\nEnter First Number: ");
	scanf("%d",&a);
	printf("Enter Second Number:");
	scanf("%d",&b);
	printf("Your multipication is %d\n",a*b);
}

divison()
{
	int a,b;
	printf("\nEnter First Number: ");
	scanf("%d",&a);
	printf("Enter Second Number:");
	scanf("%d",&b);
	printf("Your divison is %d\n",a/b);
}

 main()
{
	while(1)
	{
		int ch;
		printf("---------------MENU----------------\n\n");
		printf("1.Addition \n");
		printf("2.Subtraction \n");
		printf("3.Multipication \n");
		printf("4.Divison \n");
		printf("5.Exit\n");
		printf("\nEnter your Choice :");
		scanf("%d",&ch);
		
		
		
		if(ch==1)
		{
			
		addition();
		break;
		}
	
		else if(ch==2)
		{	
			subtraction();
			break;
		}
		else if(ch==3)
		{
			multipication();
			break;
		}
		else if(ch==4)
		{
			
			divison();
			break;
		}
		else if(ch==5)
		{
			printf("ThankYou!!\n");
		}
		else{
			printf("Invalid Choice Enter A valid Choice\n");
			
		}
	}

}
