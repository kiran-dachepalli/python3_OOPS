class Item:
    def __init__(self,name=None,price=0,category=None):
        self._name=name
        self._price=price
        self._category=category
        if self.price <=0:
            raise ValueError('Invalid value for price, got {}'.format(self._price))
            
    @property
    def name(self):
        return self._name
    @property    
    def price(self):
        return self._price
    @property    
    def category(self):
        return self._category
                   
    def __str__(self):
        return '{}@{}-{}'.format(self._name,self._price,self._category)
        
class Query:
    list_opp=['IN','EQ','GT','GTE','LT','LTE','STARTS_WITH','ENDS_WITH','CONTAINS']
    def __init__(self,field=None,operation=None,value=None):
        self.field=field
        self.value=value
        self.operation=operation
        if self.operation  not in Query.list_opp:
            raise ValueError('Invalid value for operation, got {}'.format(self.operation))
            
    def __str__(self):
        return f'{self.field} {self.operation} {self.value}'

class Store:
    def __init__(self):
        self.list_objects=[]
        
    def __str__(self):
        if self.list_objects==[]:
            return 'No items'
            
        return '\n'.join(map(str,self.list_objects))    
        
    def add_item(self,other_items):
        self.list_objects.append(other_items)
        
    def filter(self,query):
        q_object=Store()
        for item in self.list_objects:
            field_name=query.field
            if query.operation =='EQ' and getattr(item,field_name)==query.value:
                q_object.add_item(item)
            elif query.operation =='GT' and getattr(item,field_name)>query.value:
                q_object.add_item(item)
            elif query.operation =='GTE' and getattr(item,field_name)>=query.value:
                q_object.add_item(item)
            elif query.operation =='LT' and getattr(item,field_name)<query.value:
                q_object.add_item(item)
            elif query.operation =='LTE' and getattr(item,field_name)<=query.value:
                q_object.add_item(item)
            elif (query.operation =='STARTS_WITH' or query.operation =='ENDS_WITH' or query.operation=='CONTAINS') and query.value in getattr(item,field_name):
                q_object.add_item(item)
            elif query.operation =='IN' and getattr(item,field_name) in query.value:
                q_object.add_item(item)
        return q_object  
        
    def exclude(self,query):
        q_object=Store()
        include_obj = self.filter(query)
        for items in self.list_objects:
            if items not in include_obj.list_objects:
                q_object.add_item(items)
        return q_object
    
    def count(self):
        return len(self.list_objects)
        
    """     
    def filter(self,query):
        q_object=Store()
        if query.operation== 'EQ':
            for i in self.list_objects:
                if i.name== query.value:
                    q_object.add_item(i)
                elif i.price== query.value:
                    q_object.add_item(i)
                elif i.category==query.value:
                    q_object.add_item(i)
        
        elif query.operation == 'GT':
            for i in self.list_objects:
                if i.name== query.value:
                    q_object.add_item(i)
                elif i.price > query.value:
                    q_object.add_item(i)
                elif i.category==query.value:
                    q_object.add_item(i)
                    
        elif query.operation == 'GTE':
            for i in self.list_objects:
                if i.name== query.value:
                    q_object.add_item(i)
                elif i.price >= query.value:
                    q_object.add_item(i)
                elif i.category==query.value:
                    q_object.add_item(i)
                    
        elif query.operation == 'LT':
            for i in self.list_objects:
                if i.name== query.value:
                    q_object.add_item(i)
                elif i.price < query.value:
                    q_object.add_item(i)
                elif i.category==query.value:
                    q_object.add_item(i)
            
        elif query.operation == 'LTE':
            for i in self.list_objects:
                if i.name== query.value:
                    q_object.add_item(i)
                elif i.price <= query.value:
                    q_object.add_item(i)
                elif i.category==query.value:
                    q_object.add_item(i)
                    
        elif query.operation == 'STARTS_WITH':
            for i in self.list_objects:
                if i.name.startswith(query.value):
                    q_object.add_item(i)
                elif i.category.startswith(query.value):
                    q_object.add_item(i)
                    
        elif query.operation == 'ENDS_WITH':
            for i in self.list_objects:
                if i.name.endswith(query.value):
                    q_object.add_item(i)
                elif i.category.endswith(query.value):
                    q_object.add_item(i)
                    
        elif query.operation == 'CONTAINS':
            if query.field == 'name': 
                for i in self.list_objects:
                    if i.name.__contains__(query.value):
                        q_object.add_item(i)
            else:
                for i in self.list_objects:
                    if i.category.__contains__(query.value):
                        q_object.add_item(i)
                    
        elif query.operation == 'IN':
            for i in self.list_objects:
                if i.name in (query.value):
                    q_object.add_item(i)
                elif i.category in (query.value):
                    q_object.add_item(i)
                elif i.price in (query.value):
                    q_object.add_item(i)
            
        return q_object
    """
