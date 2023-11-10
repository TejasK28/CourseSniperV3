from plyer import notification

def display_notification(message, title="Notification"):
    """
    Display a notification using plyer.
    """
    notification.notify(title=title, message=message)

# Example usage:
display_notification("Hello, World!", "Test")
