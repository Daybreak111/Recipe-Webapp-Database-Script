### User_Account

```sql
varchar(20) acc_id;
varchar(20) acc_num;
varchar(20) pwd;
varchar(20) name;
varchar(20) email;
varchar(20) phone;
int(1) gender; comment "1 stands for male, 0 stands for female"
varchar(20) height;
varchar(20) weight;
int(4) age;
varchar(20) exp_weight; comment "expected weight"
varchar(20) BMI;
varchar(20) BMR;
varchar(200) avoidance_list; comment "Food to be avoided"
int(1) state; comment "1 stands for active, 0 stands for frozen"
datetime create_time;
datetime expired_time;
```



### Recipes

```sql
varchar(20) rec_id;
varchar(20) name;
Varchar(200) ingredient_list; comment "list of ingredient Id"
varchar(20) calorie;
varchar(200) description;
int(1) type: comment "1 is breakfast; 2 is lunch; 4 is dinner; 3 is breakfast/lunch; 5 is breakfast/dinner; 6 is lunch/dinner; 7 is breakfast/lunch/dinner"
int(10) likes;
datetime create_time;
datetime expired_time;
```



### Ingredients

```sql
varchar(20) ing_id;
varchar(20) name;
varchar(20) calorie;
varchar(200) description;
varchar(200) recipe_list; comment "List of recipe ID contains this ingredient"
datetime create_time;
datetime expired_time;
```

