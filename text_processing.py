import re


class Normalizing:
    
    def __init__(self, text):
        self.text = text
    
    def lower_case(self):
        text = self.text.lower()
        return text

    def strip_white_space_middle(self):
        text = re.sub("\s+", " ", self.text)
        return text
    
    def strip_white_space_start_end(self):
        text = self.text.strip()
        return text
    
    def replace_new_line_and_tab(self):
        text = re.sub("\n|\t", "", self.text)
        return text
    
    def remove_url(self):
        text = re.sub(r"https?:\/\/\S*", "", self.text)
        return text

    def remove_punctuation(self):
        text = re.sub("[^\w\s]", "", self.text) # r'\.:!،؛؟»\]\)\}', r'«\[\(\{'
        return text
    
    def elongation(self):
        text = re.sub(r'(\w)\1{2,}', r'\1', self.text)
        return text
    
    def remove_stop_words(self):
        stop_words = ["و", "در", "به", "از", "که", "این", "را", "با", "است", "برای", "آن", "یک", "خود", "تا", "کرد", "بر", "هم", "نیز", "گفت", "شد"]
        words = [word for word in self.text.split() if word not in stop_words]
        new_text = " ".join(words)
        return(new_text)

    def character_variation(self):
        characters = {
            "ۀ" : "ه",
            "ة" : "ه",
            "ي" : "ی",
            "ئ" : "ی",
            "ٱ" : "ا",
            "أ" : "ا",
            "إ" : "ا",
            "ك" : "ک",
            "ؤ" : "و"
        }
        
        for a, p in characters.items():
            self.text = self.text.replace(a, p)
        
        return self.text    

    @staticmethod
    def convert_persian_to_english_numbers(text):
        persian_numbers = '۰۱۲۳۴۵۶۷۸۹'
        english_numbers = '0123456789'
        converter = text.maketrans(persian_numbers, english_numbers)
        result = text.translate(converter)
        return int(result)

    @staticmethod
    def convert_persian_to_english_numbers_second(text):
        numbers = {
            "۰" : "0",
            "۱" : "1",
            "۲" : "2",
            "۳" : "3",
            "۴" : "4",
            "۵" : "5",
            "۶" : "6",
            "۷" : "7",
            "۸" : "8",
            "۹" : "9",
        }
        
        for p, e in numbers.items():
            text = text.replace(p, e)
        
        return int(text)

    @staticmethod
    def int_to_str(num):

        if type(num) == str:
            num = Normalizing.convert_persian_to_english_numbers(num)
            
        numbers_list = { 
            0 : 'صفر', 1 : 'یک', 2 : 'دو', 3 : 'سه', 4 : 'چهار', 5 : 'پنج',
            6 : 'شش', 7 : 'هفت', 8 : 'هشت', 9 : 'نه', 10 : 'ده',
            11 : 'یازده', 12 : 'دوازده', 13 : 'سیزده', 14 : 'چهارده',
            15 : 'پانزده', 16 : 'شانزده', 17 : 'هفده', 18 : 'هجده',
            19 : 'نوزده', 20 : 'بیست',
            30 : 'سی', 40 : 'چهل', 50 : 'پنجاه', 60 : 'شصت',
            70 : 'هفتاد', 80 : 'هشتاد', 90 : 'نود' 
            }

        k = 1000
        m = k * 1000
        b = m * 1000
        t = b * 1000
        
        assert(0 <= num)

        if (num < 20):
            return numbers_list[num]

        if (num < 100):
            if num % 10 == 0: 
                return numbers_list[num]
            else: 
                return numbers_list[num // 10 * 10] + 'و ' + numbers_list[num % 10]

        if (num < k):
            if num == 100 : 
                return 'صد'
            elif num == 200: 
                return 'دویست'
            elif num == 300: 
                return 'سیصد'
            elif num == 400: 
                return 'چهارصد'
            elif num == 500: 
                return 'پانصد'
            elif num == 600: 
                return 'ششصد'
            elif num == 700: 
                return 'هفصد'
            elif num == 800: 
                return 'هشصد'
            elif num == 900: 
                return 'نه صد'
            elif num > 199 and num < 300:
                return 'دویستو ' + Normalizing.int_to_str(num % 100)
            elif num > 299 and num < 400:
                return 'سیصدو ' + Normalizing.int_to_str(num % 100)
            elif num > 499 and num < 600:
                return 'پانصدو ' + Normalizing.int_to_str(num % 100)
            else: 
                return numbers_list[num // 100] + ' صدو ' + Normalizing.int_to_str(num % 100)
        
        if (num < m):
            if num % k == 0: 
                return Normalizing.int_to_str(num // k) + ' هزار '
            else: 
                return Normalizing.int_to_str(num // k) + ' هزارو ' + Normalizing.int_to_str(num % k)

        if (num < b):
            if (num % m) == 0: 
                return Normalizing.int_to_str(num // m) + ' میلیون'
            else: 
                return Normalizing.int_to_str(num // m) + ' میلیونو ' + Normalizing.int_to_str(num % m)

        if (num < t):
            if (num % b) == 0: 
                return Normalizing.int_to_str(num // b) + ' میلیارد'
            else: 
                return Normalizing.int_to_str(num // b) + ' میلیاردو ' + Normalizing.int_to_str(num % b)

        if (num % t == 0): 
            return Normalizing.int_to_str(num // t) + ' تریلیارد'
        else: 
            return Normalizing.int_to_str(num // t) + ' تریلیاردو ' + Normalizing.int_to_str(num % t)

        raise AssertionError('num is too large: %s' % str(num))

    def number_to_string(self):
        new_list = []
        new_text = ""
        for word in self.text.split():
            if word.isdigit():
                new_list.append(Normalizing.int_to_str(word))
            else:
                new_list.append(word)

        new_text = " ".join(new_list)
        
        return(new_text)


object1 = Normalizing('۱۲۳ hi ۲۱۳ whats up')

print(object1.text)
print(object1.number_to_string())