
import random


class User_Agent:
    def getUser():
        import random

    def make_safari_user_agent():
        result = 'Mozilla/5.0 '
        platform = random.randint(0, 1)
        if platform == 0:
            result += (
                '(Macintosh; Intel Mac OS X 10_%d_%d) AppleWebKit/605.1.15 ' +
                '(KHTML, like Gecko) Version/%d.%d Safari/605.1.15'
            ) % (
                random.randint(10, 15),
                random.randint(0, 10),
                random.randint(10, 15),
                random.randint(0, 10)
            )
        else:
            result += (
                '(iPhone; CPU iPhone OS %d_%d_%d like Mac OS X) AppleWebKit/605.1.15 ' +
                '(KHTML, like Gecko) Version/%d.%d Mobile/%dE%d Safari/%d.%d'
            ) % (
                random.randint(10, 15),
                random.randint(0, 10),
                random.randint(0, 10),
                random.randint(10, 15),
                random.randint(0, 10),
                random.randint(10, 15),
                random.randint(100, 500),
                random.randint(10, 15),
                random.randint(0, 10)
            )

        return result

    def make_chrome_user_agent():
        result = 'Mozilla/5.0 '
        platform = random.randint(0, 4)
        if platform == 0:
            result += '(Macintosh; Intel Mac OS X 10_%d_%d)' % (
                random.randint(10, 15),
                random.randint(5, 10),
            )
        elif platform == 1:
            result += '(Windows NT 10.0; %s)' % random.choice(['Win64; x64', 'WOW64'])
        elif platform == 2:
            result += '(X11; Linux %s)' % random.choice(['i686', 'x86_64'])
        elif platform == 3:
            result += '(Linux; Android %d.%d; SM-A%dU)' % (
                random.randint(4, 8),
                random.randint(0, 5),
                random.randint(100, 500),
            )
        elif platform == 4:
            result += '(Linux; Android %d; SM-M%dF)' % (
                random.randint(9, 11),
                random.randint(100, 500),
            )

        result += ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/%d.0.%d.%d' % (
            random.randint(40, 100),
            random.randint(2000, 5000),
            random.randint(10, 100),
        )

        result += ' Safari/537.36'
        return result


    def make_random_user_agent():
        return User_Agent.make_chrome_user_agent() if random.randint(0, 1) == 0 else User_Agent.make_safari_user_agent()


# for i in range(1, 1):
#     print(make_random_user_agent())

