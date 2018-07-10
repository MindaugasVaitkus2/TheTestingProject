from datetime import datetime
import os


def after_step(context, step):
    if step.status == 'failed':
        filename = "login_" + datetime.now().strftime('%Y%m%d%H%M%S') + ".png"
        context.driver.save_screenshot((os.path.join(os.path.expanduser('~\\Downloads'), filename)))
