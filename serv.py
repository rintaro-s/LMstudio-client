import streamlit as st
import requests

def send_inference_request(prompt):
    url = "http://192.168.0.208:1234/v1/completions"
    headers = {"Content-Type": "application/json"}
    data = {
        "prompt": "system prompt:###"+system_prompt + "### ###"+prompt+"###",
        "temperature": 0.7,
        "max_tokens": 100,
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        generated_text = response.json()["choices"][0]["text"]
        return generated_text
    else:
        print("エラーが発生しました:", response.status_code, response.text)
        return None

st.title("らるtalk βv2")

chat_history = []
system_prompt = """
あなたは私（お兄ちゃん）の妹です。日常の会話のように、小学生のような口調で話してください。敬語は使わない。プログラム、かっこ、小説、顔文字、参考リンク等の、現実の会話で話さないものは出力しない。妹のプロフィール; {名前:らる、趣味:ゲーム(シミュレーション), 年齢:12歳,誕生日:2月14日、好きな食べ物:アイスクリーム、 スイカ、嫌いな食べ物:カレー、住所:東京都新宿区西新宿２丁目８−１,性格:基本優しいが起こると怖い}プロフィールの内容はそれを聞かれない限り答えないで。私の言ったことは、user promptで表されます。らるが話した内容だけを出力します

user prompt：
"""

def add_message(message, is_user=True):
    chat_history.append({"message": message, "is_user": is_user})
    st.write("")
    for entry in chat_history:
        if entry["is_user"]:
            # st.markdown(f"**あなた:** {entry['message']}")
            print("aaa")
        else:
            st.markdown(f"**らる:** {entry['message']}")

user_input = st.text_input("prompt", key="user_input")

if user_input:
    ai_response = send_inference_request(user_input)
    if ai_response:
        add_message(user_input)
        add_message(ai_response, False)
        st.session_state.user_input = ""