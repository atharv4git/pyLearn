story = "hi I'am trying to find double  spaces in this string"
print(story.find("  "))

story = story.replace("  " , " ")
print(story)
print(story.find("  "))