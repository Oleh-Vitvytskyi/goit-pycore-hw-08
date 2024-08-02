def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e)
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Give me name and phone please."
        except Exception as e:
            return str(e)
    return inner

def parse_input(user_input):
    parts = user_input.strip().split()
    command = parts[0].strip().lower()
    args = parts[1:]
    return command, args