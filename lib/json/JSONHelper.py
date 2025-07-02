import json
import threading

class JSONHelper:
    _cache = {}
    _lock = threading.Lock()

    @staticmethod
    def load_language(lang_code):
        lang_code = lang_code.lower()

        with JSONHelper._lock:
            if lang_code in JSONHelper._cache:
                return JSONHelper._cache[lang_code]

            try:
                with open(f'languages/{lang_code}.json', 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    JSONHelper._cache[lang_code] = data
                    return data
            except FileNotFoundError:
                return {}