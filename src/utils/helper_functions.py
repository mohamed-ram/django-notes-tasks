
def upload_notes_to(instance, name):
    extension = name.split(".")[-1].lower()
    return f"notes/{instance.slug}.{extension}"

