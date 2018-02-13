import cx_Freeze
import sys

base = None

if sys.platform == 'win32':
        base = 'Win32GUI'

        executables = [cx_Freeze.Executable('cryptor.py', base=base)]

        packages = ['base64','cryptography.fernet.Fernet','cryptography.hazmat.backends.default_backend',
                    'cryptography.hazmat.primitives.hashes','cryptography.hazmat.primitives.kdf.pbkdf2.PBKDF2HMAC',
                    'sys']


        cx_Freeze.setup(
            name = 'cryptor',
                options = {'build_exe': {'packages':packages,
                        'include_files':include_files}},
                            version = '0.01',
                                description = 'encrypt and decrypts text files',
                                    executables = executables
                                        )
