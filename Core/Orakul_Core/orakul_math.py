"""
Orakul 2K Node
Base logic inspired by community standard, refactored and optimized for 2K+ workflow.
Protocol Oracle-60 compliant.
"""

import math

class Orakul3KResolution:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "aspect_ratio": (
                    [
                        "1:1 - 3k", "1:1 - 2K", "3:2", "2:3", "4:3", "3:4", 
                        "16:9", "9:16", "21:9", "9:21", 
                        "2:1", "1:2", "5:4", "4:5"
                    ],
                ),
            }
        }

    RETURN_TYPES = ("STRING", "INT", "INT")
    RETURN_NAMES = ("ratio", "width", "height")
    FUNCTION = "get_3k_resolution"
    CATEGORY = "Orakul"

    def get_3k_resolution(self, aspect_ratio):
        # 1:1 зафиксирован на проверенном максимуме 2752.
        # Остальные форматы идут с длинной стороной 3072 под новую плотность.
        # Все значения строго кратны 16.
        presets = {
            "1:1 - 3k":  (3072, 3072),
            "1:1 - 2k":  (2752, 2752),
            "3:2":       (3072, 2048),
            "2:3":       (2048, 3072),
            "4:3":       (3072, 2304),
            "3:4":       (2304, 3072),
            "16:9":      (3072, 1712),
            "9:16":      (1712, 3072),
            "21:9":      (3072, 1312),
            "9:21":      (1312, 3072),
            "2:1":       (3072, 1536),
            "1:2":       (1536, 3072),
            "5:4":       (3072, 2464),
            "4:5":       (2464, 3072),
        }
        
        width, height = presets.get(aspect_ratio, (2752, 2752))

        print(f"🛠️⚙️ ORAKUL STUDIO 🛠️⚙️")
        print(f"🛠️⚙️ ORAKUL 3K MONOLITH: {width}x{height} 🛠️⚙️")
        print(f"🛠️⚙️ ORAKUL STUDIO 🛠️⚙️")

        return (aspect_ratio, width, height)

        