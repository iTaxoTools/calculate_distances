# Explicit namespace package, required by maturin
__path__ = __import__("pkgutil").extend_path(__path__, __name__)
