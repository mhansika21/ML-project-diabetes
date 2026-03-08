import os
from pathlib import Path
import importlib

BASE_DIR = Path(__file__).parent

def get_plugins():
    plugins = [
        "react_plugin",              # placeholder for react()
        "runtime_error_overlay",     # placeholder for runtimeErrorOverlay()
        "tailwindcss_plugin",        # placeholder for tailwindcss()
        "meta_images_plugin",        # placeholder for metaImagesPlugin()
    ]

    if os.getenv("NODE_ENV") != "production" and os.getenv("REPL_ID") is not None:
        cartographer_module = importlib.import_module("@replit.vite_plugin_cartographer")
        dev_banner_module = importlib.import_module("@replit.vite_plugin_dev_banner")
        plugins.extend([
            cartographer_module.cartographer(),
            dev_banner_module.devBanner(),
        ])
    return plugins

CONFIG = {
    "plugins": get_plugins(),
    "resolve": {
        "alias": {
            "@": BASE_DIR / "client" / "src",
            "@shared": BASE_DIR / "shared",
            "@assets": BASE_DIR / "attached_assets",
        }
    },
    "css": {
        "postcss": {
            "plugins": [],
        }
    },
    "root": BASE_DIR / "client",
    "build": {
        "outDir": BASE_DIR / "dist" / "public",
        "emptyOutDir": True,
    },
    "server": {
        "host": "0.0.0.0",
        "allowedHosts": True,
        "fs": {
            "strict": True,
            "deny": ["**/.*"],
        },
    },
}
