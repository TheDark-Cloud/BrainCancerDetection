import matplotlib.pyplot as plt

# plotting training history
def history_plot(history):
    # Plotting the metrics (accuracy, loss, val_accuracy, val_loss)
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    # Training Loss and Validation Loss plot
    axes[0].plot(history['loss'], label='Training Loss')
    axes[0].plot(history['val_loss'], label='Validation Loss')
    axes[0].set_title('Training Vs Validation Loss')
    axes[0].set_xlabel('Epochs')
    axes[0].set_ylabel('Loss')
    axes[0].legend()
    axes[0].grid(True)

    # Training Accuracy and Validation Accuracy plot
    axes[1].plot(history['accuracy'], label='Training Accuracy')
    axes[1].plot(history['val_accuracy'], label='Validation Accuracy')
    axes[1].set_title('Training Vs Validation Accuracy')
    axes[1].set_xlabel('Epochs')
    axes[1].set_ylabel('Accuracy')
    axes[1].legend()
    axes[1].grid(True)

    # Show both plots together
    plt.tight_layout()
    plt.show()