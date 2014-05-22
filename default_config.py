import user_config as user

# default values
document_root = "."


# applying user config
try:
    document_root = user.document_root or document_root
except:
    pass