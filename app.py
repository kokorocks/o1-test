from gradio_client import Client

client = Client("yuntian-deng/o1mini")
result = client.predict(
		inputs="Hello!!",
		top_p=1,
		temperature=1,
		chat_counter=0,
		chatbot=[],
		api_name="/predict"
)
print(result)