#file statistics analyser
path = "Module_1/W2/assets/"

def analyze_file(filename):
    """Analyze a text file and return statistics"""
    try:
        with open(filename, 'r') as file:
            content = file.read()
            
            stats = {
                'filename': filename,
                'size_bytes': len(content.encode('utf-8')),
                'num_lines': content.count('\n') + 1,
                'num_words': len(content.split()),
                'num_chars': len(content),
                'num_sentences': content.count('.') + content.count('!') + content.count('?')
            }
            
            return stats
            
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Test the function
stats = analyze_file(path+'example.txt')
if stats:
    for key, value in stats.items():
        print(f"{key}: {value}")