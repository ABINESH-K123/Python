
class shopping_cart:
    shopname='Ku Ku'
    loation='Chennai'
    items={'mobiles':[5,40000],'watch':[3,1000],'tabs':[4,25000]}

    def __init__(self,name,ph_no,address,cart={}):
        self.name=name
        self.ph_no=ph_no
        self.address=address
        self.cart=cart

    @classmethod
    def product_details(cls):
        print('products available are:')
        print('product','quantity','price')
        for product in cls.items:
            print(product,cls.items[product][0],cls.items[product][1],sep='\t')

    def customer_details(self):
        print(f'Your details are:')
        print(f'name:{self.name}')
        print(f'phno:{self.ph_no}')
        print(f'address:{self.address}')
        if self.cart!={}:
            print('product available in your cart are:')
            print('product','quantity','price')
            total=0
            for  product in self.cart:
                sub_total=self.cart[product]*shopping_cart.items[product][1]
                print(product,self.cart[product],sub_total,sep='\t')
                total+=sub_total
            print('Total',total)
        else:
            print('your cart is empty')
                  
                
    def main(self):
        print('--------welcome--------')
        while True:
            print('-------------------')
            print('Enter 1 to display all the product available in the shop')
            print('Eter 2 to display your details')
            print('Enter 3 to add a product in the cart')
            print('Enter 4 to remove the product from the cart')
            print('Enter 5 to exit')

            op=int(input())

            if op==1:
                self.product_details()
            elif op==2:
                self.customer_details()
            elif op==3:
                product_name=input('Enter the product:')
                if product_name in shopping_cart.items:
                    quantity=int(input('Enter the quantity:'))
                    if quantity<=shopping_cart.items[product_name][0]:
                        shopping_cart.items[product_name][0]-=quantity
                        if product_name not in self.cart:
                            self.cart[product_name]=quantity
                        else:
                            self.cart[product_name]=self.cart[product_name]+quantity
                        print('product added successfully')
                    else:
                        print(f' stock not available,only(shopping_cart.items(product_name)[0]) left')
                else:
                    print('product is not available')
            elif op==4:
             if self.cart!={}:
                product_name=input('Enter the product:')
                if product_name in self.cart:
                    quantity=int(input('Enter the quantity:'))
                    if quantity<=self.cart[product_name]:
                        shopping_cart.items[product_name][0]+=quantity
                        self.cart[product_name]-=quantity
                        if self.cart[product_name]==0:
                            self.cart.pop(product_name)
                        else:    
                         print('product removed successfully')
                    else:
                        print(f'you have only{self.cart[product_name]}quantity available in your cart')
                
                else:
                   print ('This product is not available in your cart')
             else:
                 print('your cart is empty')
            elif op==5:
               print('Thank you for shopping')
               break
                        
                                 
                
                            
                        
        
                 
                    
cus=shopping_cart('Abinesh',8098838712,'chennai')
cus.main()


        
            
