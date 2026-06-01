import functools

def retry(count=5):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for _ in range(count):
                try:
                    return func(*args, **kwargs)
                except ValueError:
                    last_exception = ValueError
                    continue
                except OSError:
                    print(f"{func.__name__} raise OsError exception.")
                    last_exception = OSError
                    continue
                except Exception as e:
                    raise e
                    
            if last_exception:
                raise last_exception
                
        return wrapper
    return decorator
