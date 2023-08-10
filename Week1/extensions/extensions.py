m = input('File Name:').strip().lower().split('.')[-1]
match m:
    case 'gif': print('image/gif')
    case 'jpg' | 'jpeg': print('image/jpeg')
    case 'png': print('image/png')
    case 'pdf': print('application/pdf')
    case 'txt': print('text/plain')
    case 'zip': print('application/zip')
    case _: print('application/octet-stream')
    
'''
    types = {//map
        d.get('key','value') get(key)返回 key对应的值,没找到key返回value
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip",
    }
    s = input('File Name:').strip().lower().split('.')[-1]
    print(types.get(s, "application/octet-stream"))
'''