import streamlit as st

# タイトルと説明
st.title('DiSC診断')
st.write('これからいくつかの質問をしてあなたを四つの型を診断します')
st.write('(注意)これは課題用に作られたデモ版です。事実と異なる場合があります。')

# スコアの初期化
tate = 0
yoko=0

# 質問1
sensi1 = st.selectbox(
    '森で見つけた道標が朽ちていたら、本当に正しい方向を示しているか考えますか？',
    ['はい', 'いいえ']
)
if sensi1 == 'はい':
    yoko += 1
else:
    yoko -= 1

# 質問2
sensi2 = st.selectbox(
    'もし、かつて明瞭だった山道が根や蔦に覆われて行方を失っていたとしても、あなたはその先へ進むことを選びますか？',
    ['はい', 'いいえ']
)
if sensi2 == 'はい':
    tate += 1
else:
    tate -= 1

# 質問3
sensi3 = st.selectbox(
    '長い坂道を登るとき、急ぐよりも景色を楽しみながら進みたいと思いますか？',
    ['はい', 'いいえ']
)
if sensi3 == 'はい':
    tate -= 1
else:
    tate += 1
# 質問4
sensi4 = st.selectbox(
    '鏡に映る景色を見るとき、自分の姿よりも背景に目が行くことが多いですか？',
    ['はい', 'いいえ']
)
if sensi4 == 'はい':
    yoko += 1
else:
    yoko -= 1
# 質問5
sensi5 = st.selectbox(
    'もしどんなに大きな嵐が来ても、灯台の光を消さずに守り続けるべきだと思いますか？',
    ['はい', 'いいえ']
)
if sensi5 == 'はい':
    yoko += 1
else:
    yoko -= 1
# 質問6
sensi6 = st.selectbox(
    '映画館で隣が騒がしいとき、あなたは注意しますか？',
    ['はい', 'いいえ']
)
if sensi6 == 'はい':
    tate -= 1
else:
    tate += 1
# 質問7
sensi7 = st.selectbox(
    'ネットで見つけた商品が『絶対お得！』と書かれていたら、あなたはすぐに購入を決めますか？',
    ['はい', 'いいえ']
)
if sensi7 == 'はい':
    yoko -= 1
else:
    yoko += 1
# 質問8
sensi8 = st.selectbox(
    '旅行の前夜、あなたは持ち物リストを作り確認しますか？',
    ['はい', 'いいえ']
)
if sensi8 == 'はい':
    tate -= 1
else:
    tate += 1
# 質問9
sensi9 = st.selectbox(
    '友人が行きたい場所を提案したとき、あなたは自分の意見を抑えて同意しますか？',
    ['はい', 'いいえ']
)
if sensi9 == 'はい':
    yoko -= 1
else:
    yoko += 1
# 質問10
sensi10 = st.selectbox(
    '買い物をするとき、レシートを確認して金額が合っているかチェックしますか？',
    ['はい', 'いいえ']
)
if sensi10 == 'はい':
    tate -= 1
else:
    tate += 1
# 結果表示のボタン
left_column, right_column = st.columns(2)
button = left_column.button('結果を表示')

if button:
    # 結果判定
    if (tate>0)&(yoko>0):
        type1='主導型'
    elif (tate>0)&(yoko<0):
        type1='感化型'
    elif (tate<0)&(yoko>0):
        type1='慎重型'
    else:
        type1='安定型'
        # 結果を右カラムに表示
    right_column.write(f'あなたは **{type1}** です！')

    st.write('DiSC理論とは？https://www.hrpro.co.jp/miraii/post-3018/')
