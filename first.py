import streamlit as st
import random

# 页面配置
st.set_page_config(page_title="棱镜乐队 音乐播放器", page_icon="🎵", layout="centered")

# 定义棱镜乐队的歌曲数据
songs = [
    {
        "title": "总有一天你会出现在我身边",
        "artist": "棱镜乐队",
        "duration": "4:30",
        "cover": "https://ts1.tc.mm.bing.net/th/id/R-C.1fab562c2d5b13c9766c2a1245f0d627?rik=i68hcmcOXMWwrQ&riu=http%3a%2f%2fpuui.qpic.cn%2fvpic_cover%2ff3331hxg8qs%2ff3331hxg8qs_hz.jpg%2f1280&ehk=4dQr6eC4HWjtewNYmQbvMRVemGuR%2borQEjU3UrwWkNw%3d&risl=&pid=ImgRaw&r=0",
        "audio_url": "https://music.163.com/song/media/outer/url?id=1303027499.mp3"
    },
    {
        "title": "这是我一生中最勇敢的瞬间",
        "artist": "棱镜乐队",
        "duration": "4:34",
        "cover": "https://ts1.tc.mm.bing.net/th/id/R-C.1528374fd021720eea6042651f490a74?rik=rEvN02RUw6uqww&riu=http%3a%2f%2fn.sinaimg.cn%2fsinakd20200717ac%2f200%2fw640h360%2f20200717%2f564a-iwpcxkr7503227.jpg&ehk=5zMa4swwrr7x9WFe2H8WlBVmSZdQHHO2FpXgrDa5HU0%3d&risl=&pid=ImgRaw&r=0",
        "audio_url": "https://music.163.com/song/media/outer/url?id=1366216050.mp3"
    },
    {
        "title": "克林",
        "artist": "棱镜乐队",
        "duration": "5:02",
        "cover": "https://ts1.tc.mm.bing.net/th/id/R-C.cbe5e3ef815e5a7dcf3de075976916e0?rik=PdWcIMhRCa3wmw&riu=http%3a%2f%2fwww.shaomingyang.com%2fuploads%2fallimg%2f210918%2f1911462112-0.jpg&ehk=dqAA5esqDE5a6pMiYvd3n0mSKDeSUeZbg79R0%2fQ33GM%3d&risl=&pid=ImgRaw&r=0",
        "audio_url": "https://music.163.com/song/media/outer/url?id=549320309.mp3"
    }
]

# 初始化会话状态，记录当前播放歌曲索引
if "current_song_idx" not in st.session_state:
    st.session_state.current_song_idx = 0

# 获取当前歌曲
current_song = songs[st.session_state.current_song_idx]

# 页面标题和说明
st.title("🎵 棱镜乐队 音乐播放器")
st.caption("使用Streamlit制作的棱镜乐队专属音乐播放器，支持切歌和基本播放控制")

# 分栏展示封面和歌曲信息
col1, col2 = st.columns([1, 2])
with col1:
    st.image(current_song["cover"], width=200, caption="专辑封面")
with col2:
    st.header(current_song["title"])
    st.write(f"歌手: {current_song['artist']}")
    st.write(f"时长: {current_song['duration']}")

# 切歌按钮
col_prev, col_next = st.columns(2)
with col_prev:
    if st.button("⏮️ 上一首"):
        st.session_state.current_song_idx = (st.session_state.current_song_idx - 1) % len(songs)
        st.rerun()  # 重新运行页面刷新内容
with col_next:
    if st.button("⏭️ 下一首"):
        st.session_state.current_song_idx = (st.session_state.current_song_idx + 1) % len(songs)
        st.rerun()

# 播放音频
st.audio(current_song["audio_url"], format="audio/mp3")
