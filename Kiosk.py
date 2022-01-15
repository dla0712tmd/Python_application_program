class MenuClass:
    def __init__(self):
       self.menu = ['','불고기 버거', '빅맥' , '1955버거', '치즈버거', '슈림프버거', '맥스파이시', '싸이버거']
       self.price = [0,2500, 5000, 2700, 3500, 4000, 4500, 6000]
       self.total = 0
       self.count1 = self.count2 = self.count3 = self.count4 = self.count5 = self.count6 = self.count7 = 0
       #***self를 활용한 globals() 이용을 생각하고 찾으며 가능하다면 다중선언으로 바꾸기***
    # 메뉴 보이기
    def menu_print(self):
        i = 1
        print("==========버거퀸 메뉴==========")
        while i< len(self.menu):
            
            print(i, self.menu[i], self.price[i])
            #print("%d. %-10s %5d"% (i, menu[i], price[i]))
            i = i+1

        print("==============================")
    

    #############################
    # 햄버거 선택 옵션
    def menu_select(self):
        n = int(input("햄버거를 선택하세요 : "))
        price_sum = self.price[n] 
        print(self.menu[n], self.price[n],'원 ', '합계 ', price_sum, '원')

        # 햄버거 추가 주문

        while n != 0:
            print()
            n = int(input("계속 주문은 햄버거 번호를, 지불은 0을 누르세요 : "))
            if n > 0 and n < len(self.menu):
                price_sum = price_sum + self.price[n]
                print(self.menu[n], self.price[n],'원 ', '합계 ', price_sum, '원')

                if n == 1: #각 메뉴를 주문하면 주문 수량을 저장 함
                    self.count1 += 1
                
                elif n == 2:
                    self.count2 += 1

                elif n == 3:
                    self.count3 += 1

                elif n == 4:
                    self.count4 += 1

                elif n == 5:
                    self.count5 += 1

                elif n == 6:
                    self.count6 += 1

                elif n == 7:
                    self.count7 += 1


            else:
                if n == 0 :
                    print("주문이 완료되었습니다.")
                else :
                    print("없는 메뉴입니다.")
        self.total += price_sum
        return price_sum
   

    ##############################
    # 지불
    def menu_pay(self, total_price):
        
       # 지불
        while True:
            
            global pay
            pay = int(input("\n지불 금액을 입력하세요 : "))
            
            if pay >= total_price:
                print("결제가 완료되었고 거스름돈은 {0}원 입니다".format(pay-total_price))
                
                break
            
            else:
                print("결제 금액보다 더 많은 돈을 넣어주세요")
              

    def receipt(self): #영수증 출력 옵션
        
        receipt_file = open("receipt.txt", "w", encoding = "utf8")
        print("-----------------------------" , file = receipt_file)
        print("상품명  단가 수량 금액" , file = receipt_file)
        print(self.menu[1] ,self.price[1],self.count1,self.price[1] * self.count1 , file = receipt_file)
        print(self.menu[2] ,self.price[2],self.count2,self.price[2] * self.count2 , file = receipt_file)
        print(self.menu[3] ,self.price[3],self.count3,self.price[3] * self.count3 , file = receipt_file)
        print(self.menu[4] ,self.price[4],self.count4,self.price[4] * self.count4 , file = receipt_file)
        print(self.menu[5] ,self.price[5],self.count5,self.price[5] * self.count5 , file = receipt_file)
        print(self.menu[6] ,self.price[6],self.count6,self.price[6] * self.count6 , file = receipt_file)
        print(self.menu[7] ,self.price[7],self.count7,self.price[7] * self.count7 , file = receipt_file)
        print("합계", self.total , file = receipt_file)
        print("-----------------------------" , file = receipt_file)
        receipt_file.close() 

        print("영수증이 출력되었습니다.")

menu1 = MenuClass()
#인스턴스 생성

#일일 정산용
   
calc = 0
while(calc != 1):
    menu1.menu_print()
    total_price = menu1.menu_select()
    menu1.menu_pay(total_price)
    calc = int(input("주문을 마치고 싶다면 1, 새로운 주문은 2을 누르세요."))

print_receipt = input("영수증을 출력하고 싶다면 'Y' 하고 싶지않으면 'N'를 입력해주세요")

if print_receipt == 'Y': #파일 입출력으로 따로 처리
    menu1.receipt() #메소드를 호출하고 싶다면 위의 인스턴스 생성 한것을 이용해 호출
   
      
elif print_receipt == 'N': #바로 종료
    print("총 주문액은 {0}원 이고 거스름돈은 {1}원 입니다".format(menu1.total ,pay-total_price ))