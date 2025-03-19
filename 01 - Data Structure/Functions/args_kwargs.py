'''
 * ARGS = returns as a tuple (values separated by commas)
** KWARGS = returns as a dictionary
'''

def display_poem(full_date, *args, **kwargs):
    text = "\n".join(args)
    data = "\n".join([f"{key.title()}: {value}" for key, value in kwargs.items()])
    message = f"{full_date}\n\n{text}\n\n{data}"
    print(message)


display_poem(
    "Saturday, August 26, 2023",
    "Zen of Python",
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!",
    author="Tim Peters",
    year=1999,
)
