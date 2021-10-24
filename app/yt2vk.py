import os
import requests

from bs4 import BeautifulSoup

yt_channel_id = os.environ.get("YT_CHANNEL_ID")
vk_access_token = os.environ.get("VK_ACCESS_TOKEN")
vk_group_id = os.environ.get("VK_GROUP_ID")


def get_source_bs(url):
    return BeautifulSoup(requests.get(url).text, 'html.parser')


def get_last_video(channel_id: str = None):
    soup = get_source_bs(
        f'https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}')

    video = soup.find_all("entry")[1] if len(soup.find_all("entry")) > 1 else False

    if not video:
        return False, False, False

    title = video.find_all("title")[0].text
    link = video.find_all("link")[0]["href"]
    published = video.find_all("published")[0].text

    return title, link, published


def post_vk(message: str, access_token: str, owner_id: int, attachments=''):
    return requests.get('https://api.vk.com/method/wall.post?', params=(
        ('v', '5.131'),
        ('access_token', access_token),
        ('owner_id', owner_id), #если нужно выкладывать в паблик параметр должен быть отрицательным
        ('message', message),
        ('attachments', attachments),
        ('friends_only', 0),
        ('from_group', 1)
    )).text


if __name__ == "__main__":
    title, link, published = get_last_video(yt_channel_id)
    respronse = post_vk(
        message=f"А ты посмотрел это видео?\n{title}\n{link}",
        access_token=vk_access_token,
        owner_id=vk_group_id,
        attachments=link
    ) if title and link and published else "Error"
    print(respronse)