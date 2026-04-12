from datetime import datetime


class PhrinusomyisRegistry:
    def __init__(self):
        self.institutional_profile = {
            "brand_name": "PHRINUSOMYIS",
            "hq_status": "Worldwide / Global",
            "founder_ceo": "Victor Seth A",
            "positioning": "Top-tier Luxury & Stadium-Scale Entertainment",
            "core_mission": "Engineering Legacy Moments through unparalleled luxury and world-stage production.",
            "security_status": "Glass Shield Active"
        }

        self.visual_identity = {
            "server_assets": [
                "Phrinusomyis_logo.png",
                "phrinusomyis_logo_360.png",
                "Phrinusomyis_logo 1.png",
                "phrinusomyis_logo 2.png",
                "phrinusomyis_logo 3.png"
            ],
            "visual_standard": "12K Premium Cinematic View",
            "color_palette": "Monochromatic Gold on Obsidian",
            "icon_logic": "Authoritative Lion (Left) + King (Right)"
        }

        self.languages = {
            "default": "en",
            "supported": ["en", "zh", "hi", "es", "fr", "ar", "bn", "pt", "ru", "ja", "de", "ko", "tr", "vi", "yo", "ig"],
            "translations": {
                "en": {"tagline": "Engineering Legacy Moments"},
                "zh": {"tagline": "工程传奇时刻"},
                "hi": {"tagline": "इंजीनियरिंग लेगेसी मोमेंट्स"},
                "ar": {"tagline": "هندسة لحظات الإرث"},
                "ru": {"tagline": "Создание легендарных моментов"},
                "ja": {"tagline": "レガシーな瞬間をエンジニアリングする"},
                "ko": {"tagline": "레거시 모먼트 엔지니어링"},
                "yo": {"tagline": "Ṣiṣẹ Awọn Akoko Arosọ"},
                "ig": {"tagline": "Ịrụ Oge Ezigbo Akụkọ"}
            }
        }

        self.global_metrics = {
            "weekly_impressions_target": 20000000,
            "monthly_impressions_target": 80000000,
            "active_markets": ["Global", "West Africa", "Russia", "China"]
        }

        self.products = {
            "PHRINUSOMYIS_cup": {
                "units": 50,
                "specs": "Dual-finish matte obsidian, 24K gold plate"
            },
            "exclusive_perfume": {
                "units": 500,
                "specs": "Black glass, gold stopper"
            }
        }

        self.event_registry = {
            "next_major_event": "2026-07-24",
            "status": "Confirmed",
            "system_status": "Synchronized"
        }

        self.seo = {
            "meta_title": "PHRINUSOMYIS - Engineering Legacy Moments Worldwide",
            "meta_description": "Experience luxury stadium-scale events with PHRINUSOMYIS.",
            "keywords": [
                "PHRINUSOMYIS",
                "Luxury Entertainment",
                "Global Events",
                "Stadium Show",
                "Legacy Moments"
            ],
            "open_graph": {
                "title": "PHRINUSOMYIS Global Events",
                "description": "Top-tier luxury and world-stage productions engineered to perfection.",
                "image": "https://example.com/assets/logo.png"
            },
            "twitter_card": {
                "title": "PHRINUSOMYIS - Engineering Legacy Moments",
                "description": "Luxury and world-stage entertainment.",
                "image": "https://example.com/assets/logo_360.png"
            }
        }

    # -----------------------------
    # SYSTEM FUNCTIONS
    # -----------------------------

    def get_brand(self):
        return self.institutional_profile["brand_name"]

    def get_event_date(self):
        return self.event_registry["next_major_event"]

    def language_count(self):
        return len(self.languages["supported"])

    def system_status_report(self):
        return {
            "brand": self.get_brand(),
            "security": self.institutional_profile["security_status"],
            "languages": self.language_count(),
            "markets": self.global_metrics["active_markets"],
            "event": self.get_event_date()
        }

    def export_json(self):
        """Convert full registry to JSON-ready dictionary"""
        return {
            "institutional_profile": self.institutional_profile,
            "visual_identity": self.visual_identity,
            "languages": self.languages,
            "global_metrics": self.global_metrics,
            "products": self.products,
            "event_registry": self.event_registry,
            "seo": self.seo
        }
