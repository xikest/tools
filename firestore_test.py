from tools.db.firestoremanager import FirestoreManager
import pandas as pd


credentials_file = "web-scraper_key.json"  
firestore_manager = FirestoreManager(credentials_file)


data2 = {
    'product': ['Laptop', 'Tablet', 'Smartphone'],
    'price': [999, 499, 799],
    'stock': [50, 150, 200]
}
df2 = pd.DataFrame(data2)


dataframes_dict = {'products': df2}
firestore_manager.save_dataframe(dataframes_dict, collection_name="sample_collection")

# 저장된 DataFrame 데이터 읽기
# Firestore에서 데이터 읽기
dataframe = firestore_manager.read_data('sample_collection')
print(dataframe)  # 데이터프레임 출력



# 예제 2: 리스트 업로드 및 읽기
list_data = {
    "sample_list_doc": ["apple", "banana", "cherry", "date"]
}

# Firestore에 리스트 저장
firestore_manager.save_list(list_data)

# Firestore에서 리스트 데이터 읽기
list_from_firestore = firestore_manager.read_list("sample_list_doc")
print("Firestore에서 읽은 리스트 데이터:", list_from_firestore)
