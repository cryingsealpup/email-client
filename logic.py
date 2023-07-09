import smtplib
from email.mime.multipart import MIMEMultipart as mmp
from email.mime.text import MIMEText as mtext
from string import Template


# Функция для считывания шаблонов
def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
        return Template(template_file_content)


# Функция для считывания адресов из файла
# Возвращает список адресов и имён
def get_contacts(filename):
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails


def send_message(message_template='Weekend greeting.txt', provider='gmail',
                 login='', password='', from_addr='', subject="This is TEST", contacts=''):
    """
    :param message_template: txt file with template of message. Needed to be in format of string.Template
    :param provider: server name, port is 587
    :param login: email, phone number or username
    :param password: password
    :param from_addr: address which will be displaying in the section 'From'. Default empty
    :param subject: subject of message
    :param contacts: .txt file with list of contacts. Note: there needed to write in format *name email*
    """
    providers = {'gmail': 'smtp.gmail.com', 'yahoo': 'smtp.mail.yahoo.com', 'outlook': 'smtp-mail.outlook.com',
                 'yandex': 'smtp.yandex.ru', 'mail.ru': 'smtp.mail.ru'}
    try:
        s = smtplib.SMTP(host=providers[provider], port=587)
    except Exception:
        return 'connection failed, try again'
    try:
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(login, password)
    except Exception:
        return 'login failed'

    print('login succeed')
    names, emails = get_contacts(contacts)

    for name, email in zip(names, emails):
        msg = mmp()  # создаем сообщение

        try:
            # в шаблоне письма заменяем имя
            message = read_template(message_template).substitute(PERSON_NAME=name.title())
            print('setting the  params')
            # устанавливаем параметры сообщения
            # для объекта типа MIMEMultipart необходимо, чтобы это был словарь
            msg['From'] = from_addr
            print('from address placed')
            msg['To'] = email
            print('to address placed')
            msg['Subject'] = subject
            print('subject placed')

            # добавляем эту информацию (текст письма, отправителя и получателя / получателей) к сообщению)
            msg.attach(mtext(message, 'plain'))

            # отправка сообщения
            s.send_message(msg)
            print('sent')
            del msg
        except Exception:
            return 'wrong message params'
    return 'success!'


