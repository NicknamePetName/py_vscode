import logging
import os
import traceback
# 设置日志记录器
logging.basicConfig(filename='yixin.log',level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', encoding='utf-8')

try:
    logging.info(f'print')
    print(a)
except Exception:
    logging.exception("发生异常")
    print(f"\n\n商品信息 发生异常!")
    traceback.print_exc()
    os.system('pause')


