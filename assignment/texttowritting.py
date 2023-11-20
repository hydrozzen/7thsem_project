from handwritten_image import HandWrite
hand = HandWrite()
hand.convert_to_image('C:\\Users\\hario\\OneDrive\\Desktop\\nathkhat india\\assignment\\text') # or .doc and .txt file
hand.convert_to_image('C:\\Users\\hario\\OneDrive\\Desktop\\nathkhat india\\assignment\\text', save_dir='images')
hand.to_txt('C:\\Users\\hario\\OneDrive\\Desktop\\nathkhat india\\assignment\\text', edit=True) # or .doc and .txt file
hand.convert_to_image('your-edited-file.txt', random_select=False)
hand.to_txt('C:\\Users\\hario\\OneDrive\\Desktop\\nathkhat india\\assignment\\text', random_select=False)
hand.to_txt('C:\\Users\\hario\\OneDrive\\Desktop\\nathkhat india\\assignment\\text', save_path='file.txt')