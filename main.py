import base64
import os
import secrets
import string
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def generate_secret_code(length=7):
  """Génère un code aléatoire de 7 caractères mélangeant majuscules,

  minuscules, chiffres et symboles spéciaux.
  """
  alphabet = string.ascii_letters + string.digits + string.punctuation
  return "".join(secrets.choice(alphabet) for _ in range(length))


def code_to_key(code: str, salt: bytes) -> bytes:
  """Transforme ton code de 7 caractères en une clé cryptographique robuste."""
  kdf = PBKDF2HMAC(
      algorithm=hashes.SHA256(),
      length=32,
      salt=salt,
      iterations=100_000,
  )
  return base64.urlsafe_b64encode(kdf.derive(code.encode()))


def encrypt_message(message: str, code: str) -> str:
  """Chiffre le message à l'aide du code secret."""
  salt = os.urandom(16)
  key = code_to_key(code, salt)
  f = Fernet(key)

  encrypted_bytes = f.encrypt(message.encode())
  payload = salt + encrypted_bytes
  return base64.urlsafe_b64encode(payload).decode()


def decrypt_message(payload_b64: str, code: str) -> str:
  """Déchiffre le message."""
  try:
    decoded_payload = base64.urlsafe_b64decode(payload_b64.encode())
    salt = decoded_payload[:16]
    encrypted_bytes = decoded_payload[16:]

    key = code_to_key(code, salt)
    f = Fernet(key)
    decrypted_bytes = f.decrypt(encrypted_bytes)
    return decrypted_bytes.decode()
  except Exception:
    raise ValueError(
        "Déchiffrement impossible : le code secret est erroné ou le message a"
        " été altéré."
    )


if __name__ == "__main__":
  print("=========================================")
  print("     SECURE CLI CIPHER - 7 CHARS (SYM)   ")
  print("=========================================")

  choix = input("Voulez-vous (1) Chiffrer ou (2) Déchiffrer ? : ").strip()

  if choix == "1":
    message = input("\nEntrez votre message secret : ")
    code = generate_secret_code(7)

    cipher_text = encrypt_message(message, code)

    print("\n[✔] Message chiffré généré avec succès !")
    print(
        f"🔑 Code secret à 7 caractères (avec symboles) à transmettre : {code}"
    )
    print(
        f"📦 Bloc de texte chiffré (à copier-coller et envoyer) :\n{cipher_text}"
    )

  elif choix == "2":
    cipher_text = input("\nCollez le message chiffré : ").strip()
    code = input(
        "Entrez le code secret à 7 caractères fourni par l'expéditeur : "
    ).strip()

    try:
      original_message = decrypt_message(cipher_text, code)
      print(f"\n[✔] Message décrypté avec succès :\n{original_message}")
    except ValueError as e:
      print(f"\n[❌ ERREUR] {e}")
  else:
    print("Choix invalide.")
