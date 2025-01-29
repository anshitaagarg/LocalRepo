import time

def print_lyrics():
    lyrics = [
        ("I'll imagine we fell in love", 0.7, 0.035),
        ("I'll nap under moonlight skies with you", 0.6, 0.03),
        ("I think I'll picture us, you with the waves", 0.5, 0.045),
        ("The ocean's colors on your face", 0.4, 0.05),
        ("I'll leave my heart with your air", 0.5, 0.04),
        ("So let me fly with you", 0.6, 0.03),
        ("Will you be forever with me?", 0.7, 0.05),
    ]

    for text, line_delay, char_delay in lyrics:
        for c in text:
            print(c, end='', flush=True)
            time.sleep(char_delay)
        print()
        time.sleep(line_delay)

if __name__ == "__main__":
    print_lyrics()
    print("""
           *****     *****     
          ********  ********   
         ********************  
          ******************   
           ***************     
            *************      
              *********        
                *****          
                  *               
    """)
