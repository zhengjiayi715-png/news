from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_hash_password(password: str):
    # 将密码编码为 UTF-8 字节，截取前 72 个字节，然后再解码回字符串进行哈希
    # 注意：这里用 .encode('utf-8')[:72] 才是真正的按字节截断
    safe_password = password.encode('utf-8')[:72]
    return pwd_context.hash(safe_password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)