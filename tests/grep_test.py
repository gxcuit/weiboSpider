import json
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        weibo = u"大家早点休息吧，股市不是生活的全部，应该还有诗和梦乡"
        keywords = ["大家","你好1"]
        res = any([w in weibo for w in keywords])
        print(res)

    def test_json(self):
        with open('D:/workspace/weiboSpider/config.json',encoding='utf-8') as f:
            json.load(f)
if __name__ == '__main__':
    unittest.main()
