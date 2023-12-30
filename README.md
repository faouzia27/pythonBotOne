The bot is designed to automate the process of searching and saving images related to a list of names. Here's how it works:

1. Input from File: The bot takes as input a list of names from a file. These names serve as keywords for image searches.
2. Search on https://it.123rf.com/: Using web scraping, the bot conducts a search on https://it.123rf.com/ for each name in the list. The goal is to find the image corresponding to the name.
3. Image Saving: The bot downloads the second image related to the search and saves it in an output folder.
4. Saving Syntax: The image is saved with a specific syntax. The image's name corresponds to the name taken from the list, and the file extension is PNG. For example, if the searched name is 'water', the image will be saved as 'water.png'.

This automation streamlines the process of searching and saving images related to a specific list of names, making the management of visual resources associated with specific terms more efficient.

How to run from cmd:
```python
python main.py
```

