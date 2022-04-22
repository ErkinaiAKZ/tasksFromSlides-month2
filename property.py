# 1. Считать файл
# 2. Объявить атрибуты host, ip, port, password
# 3. Написать проверку валидности данных
# 4. Написать property геттеры и сеттеры для этих атрибутов

class HostError(Exception):
    pass


class Hack:
    def __init__(self, host, ip, port, password):

        # Hack.validate_network_address(host)
        # Hack.validate_network_address(ip)
        # Hack.check_port(port)
        # Hack.check_password(password)

        self.host = host
        self.ip = ip
        self.port = port
        self.password = password


    @classmethod
    def validate_network_address(cls, network_address: str):
        if type(network_address) != str:
            raise HostError('Input value not equal str')

        network_address = network_address.split('.')

        if len(network_address) != 4:
            raise HostError(f'{network_address} must be more than 4 elements')

        for ip_section in network_address:
            if not ip_section.isdigit():
                print(ip_section)
                raise HostError(f'{ip_section} input value not equal to str')
            elif 255 > int(ip_section) < 0:
                raise HostError(f'{ip_section} input ip_section more than 255 or less than 0')


    @classmethod
    def check_port(cls, port):
        if type(port) != str:
            raise TypeError('Must be integers.')

        if 1024 > int(port) > 9999:
            raise Exception('invalid numbers')

    @classmethod
    def check_password(cls, password):
        if type(password) != str and len(password) > 5:
            raise TypeError('Must be integers and consist of five integers')


    @property
    def host(self):
        return self.__host

    @host.setter
    def host(self, host):
        self.validate_network_address(host)
        self.__host = host

    @property
    def ip(self):
        return self.__ip

    @ip.setter
    def ip(self, ip):
        self.validate_network_address(ip)
        self.__ip = ip

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, port):
        self.check_port(port)
        self.__port = port

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, password):
        self.check_password(password)
        self.__password = password

file = open('/Users/erkaakzholova/Desktop/data.txt', 'r')
lines = file.readlines()

config = dict()

for line in lines:
    key, value = line.split('=')
    config[key.strip()] = value.strip()


def print_data(ip, host, port, password):
    print(ip)
    print(host)
    print(port)
    print(password)

# print_data(config['ip'], config['host'], config['port'], config['password'])
#print_data(**config)
#d = Hack(**config)
#d = Hack('127.0.0.1', '127.0.0.1', '8080', '12345')


d = Hack('127.0', '127.0.0.1', '80uy', '125')      #checking the code

print(d.__dict__)




