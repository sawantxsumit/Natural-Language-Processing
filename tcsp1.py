class alchemist:
    
    def __init__(self):
        self.n=int(input('Enter the number of recipies :'))
        self.recipes = {}
        for i in range(self.n):
            r = input(f"Enter recipe {i+1}: ")
            potion, ingredients = r.split("=")
            potion = potion.strip()
            ingredients = [x.strip() for x in ingredients.split("+")]

            if potion not in self.recipes:
                self.recipes[potion] = []
            self.recipes[potion].append(ingredients)

        self.desired_potion = input("Enter desired potion: ").strip()
        self.memo={}
    
    
    def get_cost(self,potion):
        if potion not in self.recipes:
            return 0
        
        min_cost=float('inf')
        
        if potion in self.memo:
            return self.memo[potion]
        
        for recipe in self.recipes[potion]:
            # cost of orb= len(ingd.)-1
            cost= len(recipe)-1
            for i in recipe:
                cost = cost + self.get_cost(i) # recursive func for calculating cost
            min_cost=min(min_cost , cost)
        self.memo[potion] = min_cost

            
        return min_cost
        
                
if __name__=='__main__':
    a=alchemist()
    d=a.get_cost(a.desired_potion)
    print(d)
        
            
        
    
    
    
    
    
    
    
    
    
    
    
    
n=4

recipies={
    'awakening'
}
['awakening=snakefangs+wolfbane',
'veritaserum=snakefangs+awakening',
'dragontonic=snakefangs+velarin',
'dragontonic=awakening+veritaserum']

potion='dragontonic'
