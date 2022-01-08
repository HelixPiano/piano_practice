import random
from colorama import Fore, Style

def print_results(dictionary, name):
    result = dictionary.get(name)
    print(f"Name: {Fore.RED + name}")
    print(Style.RESET_ALL)
    print(f"Right hand: {result[0]}")
    print(f"Notes: {result[1]}")
    print(f"Left Hand: {result[2]}")
    print('----------------------------------------------')


def print_harmonic_melodic_info():
    print(f"Harmonic: Siebten Ton um einen Halbtonschritt erhöhen.")
    print(f"Melodic: Sechsten und siebten Ton um einen Halbtonschritt erhöhen beim Aufstieg. Beim Abstieg beide wieder ohne Erhöhung.")
    print('----------------------------------------------')


def print_vorzeichen_dur(name):
    print(f"Tonart: {Fore.RED + name} Major/Dur")
    print(Style.RESET_ALL)
    if name == 'C':
        print(f"Ohne Vorzeichen")
    elif name == 'F':
        print(f"Vorzeichen: B")
    elif name == 'G':
        print(f"Vorzeichen: Fis")
    elif name == 'D':
        print(f"Vorzeichen: Fis Cis")
    elif name == 'A':
        print(f"Vorzeichen: Fis Cis Gis")
    elif name == 'E':
        print(f"Vorzeichen: Fis Cis Gis Dis")
    elif name == 'B':
        print(f"Vorzeichen: Fis Cis Gis Dis Ais")
    elif name == 'D Flat':
        print(f"Vorzeichen: B Es As Des Ges")
    elif name == 'E Flat':
        print(f"Vorzeichen: B Es As")
    elif name == 'F Sharp':
        print(f"Vorzeichen: Fis Cis Gid Dis Ais Eis")
    elif name == 'A Flat':
        print(f"Vorzeichen: Gis Ais His Cis Dis Eis Fisis(!)")
    elif name == 'B Flat':
        print(f"Vorzeichen: B Es")
    else:
        assert False, "Kann Vorzeichen für Dur nicht finden"
    print('----------------------------------------------')


def print_vorzeichen_moll(name):
    print(f"Parallele Molltonart: {Fore.RED + name}/Moll")
    print(Style.RESET_ALL)
    if name == 'A Minor':
        print(f"Ohne Vorzeichen")
    elif name == 'D Minor':
        print(f"Vorzeichen: B")
    elif name == 'E Minor':
        print(f"Vorzeichen: Fis")
    elif name == 'B Minor':
        print(f"Vorzeichen: Fis Cis")
    elif name == 'F Sharp Minor':
        print(f"Vorzeichen: Fis Cis Gis")
    elif name == 'C Sharp Minor':
        print(f"Vorzeichen: Fis Cis Gis Dis")
    elif name == 'G Sharp Minor':
        print(f"Vorzeichen: Fis Cis Gid Dis Ais")
    elif name == 'B Flat Minor':
        print(f"Vorzeichen: B Es As Des Ges")
    elif name == 'C Minor':
        print(f"Vorzeichen: B Es As")
    elif name == 'E Flat Minor':
        print(f"Vorzeichen: B Es As Des Ges Ces")
    elif name == 'F Minor':
        print(f"Vorzeichen: B Es As Des")
    elif name == 'G Minor':
        print(f"Vorzeichen: B Es")
    else:
        assert False, "Kann Vorzeichen für Moll nicht finden"
    print('----------------------------------------------')


def pick_relative_key(name):
    if name == 'C':
        return f"A Minor"
    elif name == 'F':
        return f"D Minor"
    elif name == 'G':
        return f"E Minor"
    elif name == 'D':
        return f"B Minor"
    elif name == 'A':
        return f"F Sharp Minor"
    elif name == 'E':
        return f"C Sharp Minor"
    elif name == 'B':
        return f"G Sharp Minor"
    elif name == 'D Flat':
        return f"B Flat Minor"
    elif name == 'E Flat':
        return f"C Minor"
    elif name == 'F Sharp':
        print('Redirect to D Sharp Minor to E Flat Minor')
        return f"E Flat Minor"
    elif name == 'A Flat':
        return f"F Minor"
    elif name == 'B Flat':
        return f"G Minor"
    else:
        assert False, "Can't find parallel key"


if __name__ == '__main__':
    Arpeggio = {
        # https://mypianoteacher.net/resources/learn-to-play-scales/all-major-arpeggios/
        'C Major Arpeggio': [[1, 2, 3, 1, 2, 3, 5], ['C', 'E', 'G', 'C', 'E', 'G', 'C'], [5, 3, 2, 1, 3, 2, 1]],
        'D Major Arpeggio': [[1, 2, 3, 1, 2, 3, 5], ['D', 'Fis', 'A', 'D', 'Fis', 'D'], [5, 3, 2, 1, 3, 2, 1]],
        'E Major Arpeggio': [[1, 2, 3, 1, 2, 3, 5], ['E', 'Gis', 'H', 'E', 'Gis', 'H', 'E'], [5, 3, 2, 1, 3, 2, 1]],
        'F Major Arpeggio': [[1, 2, 3, 1, 2, 3, 5], ['F', 'A', 'C', 'F', 'A', 'C', 'F'], [5, 3, 2, 1, 3, 2, 1]],
        'G Major Arpeggio': [[1, 2, 3, 1, 2, 3, 5], ['G', 'H', 'D', 'G', 'H', 'D', 'G'], [5, 3, 2, 1, 3, 2, 1]],
        'A Major Arpeggio': [[1, 2, 3, 1, 2, 3, 5], ['A', 'Cis', 'E', 'A', 'Cis', 'E', 'A'], [5, 3, 2, 1, 3, 2, 1]],
        'B Major Arpeggio': [[1, 2, 3, 1, 2, 3, 5], ['H', 'Dis', 'Fis', 'H', 'Dis', 'Fis', 'H'], [5, 3, 2, 1, 3, 2, 1]],
        'D Flat Major Arpeggio': [[2, 1, 2, 4, 1, 2, 4], ['Des', 'F', 'As', 'Des', 'F', 'As', 'Des'], [2, 1, 4, 2, 1, 4, 2]],
        'E Flat Major Arpeggio': [[2, 1, 2, 4, 1, 2, 4], ['Es', 'G', 'B', 'Es', 'G', 'B', 'Es'], [2, 1, 4, 2, 1, 4, 2]],
        'F Sharp Major Arpeggio': [[1, 2, 3, 1, 2, 3, 5], ['Fis', 'Ais', 'Cis', 'Fis', 'Ais', 'Cis', 'Fis'], [5, 3, 2, 1, 3, 2, 1]],
        'A Flat Major Arpeggio': [[2, 1, 2, 4, 1, 2, 4], ['As', 'C', 'Es', 'As', 'C', 'Es', 'As'], [2, 1, 4, 2, 1, 4, 2]],
        'B Flat Major Arpeggio': [[3, 2, 1, 3, 2, 1, 2], ['B', 'D', 'F', 'B', 'D', 'F', 'B'], [3, 2, 1, 3, 2, 1, 2]],

        # https://mypianoteacher.net/resources/learn-to-play-scales/all-minor-arpeggios/
        'C Minor Arpeggio': [[1, 2, 3, 1, 2, 3, 5], ['C', 'Es', 'G', 'C', 'Es', 'G', 'C'], [5, 3, 2, 1, 3, 2, 1]],
        'D Minor Arpeggio': [[1, 2, 3, 1, 2, 3, 5], ['D', 'F', 'A', 'D', 'F', 'A', 'D'], [5, 3, 2, 1, 3, 2, 1]],
        'E Minor Arpeggio': [[1, 2, 3, 1, 2, 3, 5], ['E', 'G', 'H', 'E', 'G', 'H', 'E'], [5, 3, 2, 1, 3, 2, 1]],
        'F Minor Arpeggio': [[1, 2, 3, 1, 2, 3, 5], ['F', 'As', 'C', 'F', 'As', 'C', 'F'], [5, 4, 2, 1, 4, 2, 1]],
        'G Minor Arpeggio': [[1, 2, 3, 1, 2, 3, 5], ['G', 'B', 'D', 'G', 'B', 'D', 'G'], [5, 3, 2, 1, 3, 2, 1]],
        'A Minor Arpeggio': [[1, 2, 3, 1, 2, 3, 5], ['A', 'C', 'E', 'A', 'C', 'E', 'A'], [5, 3, 2, 1, 3, 2, 1]],
        'B Minor Arpeggio': [[1, 2, 3, 1, 2, 3, 5], ['H', 'D', 'Fis', 'H', 'D', 'Fis', 'H'], [5, 4, 2, 1, 4, 2, 1]],
        'C Sharp Minor Arpeggio': [[2, 1, 2, 4, 1, 2, 4], ['Cis', 'E', 'Gis', 'Cis', 'E', 'Gis', 'Cis'], [5, 3, 2, 1, 3, 2, 1]],
        'E Flat Minor Arpeggio': [[1, 2, 3, 1, 2, 3, 5], ['Es', 'Ges', 'B', 'Es', 'Ges', 'B', 'Es'], [5, 4, 2, 1, 4, 2, 1]],
        'F Sharp Minor Arpeggio': [[2, 1, 2, 4, 1, 2, 4], ['Fis', 'A', 'Cis', 'Fis', 'A', 'Cis', 'Fis'], [2, 1, 4, 2, 1, 4, 2]],
        'G Sharp Minor Arpeggio': [[2, 1, 2, 4, 1, 2, 4], ['Gis', 'H', 'Dis', 'Gis', 'H', 'Dis', 'Gis'], [2, 1, 4, 2, 1, 4, 2]],
        'B Flat Minor Arpeggio': [[2, 3, 1, 2, 3, 1, 2], ['B', 'Des', 'F', 'B', 'Des', 'F', 'B'], [3, 2, 1, 3, 2, 1, 2]],

    }

    Major_Scales = {
        # https://mypianoteacher.net/resources/learn-to-play-scales/all-major-scales/
        'C Major Scale': [[1, 2, 3, 1, 2, 3, 4], ['C', 'D', 'E', 'F', 'G', 'A', 'H', 'C'], [5, 4, 3, 2, 1, 3, 2, 1]],
        'D Major Scale': [[1, 2, 3, 1, 2, 3, 4], ['D', 'E', 'Fis', 'G', 'A', 'H', 'Cis', 'D'], [5, 4, 3, 2, 1, 3, 2, 1]],
        'E Major Scale': [[1, 2, 3, 1, 2, 3, 4], ['E', 'Fis', 'Gis', 'A', 'H', 'Cis', 'Dis', 'E'], [5, 4, 3, 2, 1, 3, 2, 1]],
        'F Major Scale': [[1, 2, 3, 4, 1, 2, 3], ['F', 'G', 'A', 'B', 'C', 'D', 'E', 'F'], [5, 4, 3, 2, 1, 3, 2, 1]],
        'G Major Scale': [[1, 2, 3, 1, 2, 3, 4], ['G', 'A', 'H', 'C', 'D', 'E', 'Fis', 'G'], [5, 4, 3, 2, 1, 3, 2, 1]],
        'A Major Scale': [[1, 2, 3, 1, 2, 3, 4], ['A', 'H', 'Cis', 'D', 'E', 'Fis', 'Gis', 'A'], [5, 4, 3, 2, 1, 3, 2, 1]],
        'B Major Scale': [[1, 2, 3, 1, 2, 3, 4], ['H', 'Cis', 'Dis', 'E', 'Fis', 'Gis', 'Ais', 'H'], [4, 3, 2, 1, 4, 3, 2, 1, 3, 2, 1, 4]],
        'D Flat Major Scale': [[2, 3, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 4], ['Des', 'Es', 'F', 'Ges', 'As', 'B', 'C', 'Des'],
                               [3, 2, 1, 4, 3, 2, 1, 3, 2]],
        'E Flat Major Scale': [[2, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 4], ['Es', 'F', 'G', 'As', 'B', 'C', 'D', 'Es'],
                               [3, 2, 1, 4, 3, 2, 1, 3, 2, 1, 4]],
        'F Sharp Major Scale': [[2, 3, 4, 1, 2, 3, 1, 2], ['Fis', 'Gis', 'Ais', 'H', 'Cis', 'Dis', 'Eis', 'Fis'], [4, 3, 2, 1, 3, 2, 1, 4]],
        'A Flat Major Scale': [[2, 3, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3], ['As', 'B', 'C', 'Des', 'Es', 'F', 'G', 'As'],
                               [3, 2, 1, 4, 3, 2, 1, 3, 2, 1, 4, 3, 2, 1, 2]],
        'B Flat Major Scale': [[2, 1, 2, 3, 1, 2, 3, 4, 1], ['B', 'C', 'D', 'Es', 'F', 'G', 'A', 'B'], [3, 2, 1, 4, 3, 2, 1, 3]],
    }

    Minor_Scales_Harmonic = {
        # https://mypianoteacher.net/resources/learn-to-play-scales/all-minor-scales-harmonic/
        'C Harmonic Minor Scale': [[1, 2, 3, 1, 2, 3, 4], ['C', 'D', 'Es', 'F', 'G', 'As', 'H', 'C'], [5, 4, 3, 2, 1, 3, 2, 1]],
        'D Harmonic Minor Scale': [[1, 2, 3, 1, 2, 3, 4], ['D', 'E', 'F', 'G', 'A', 'B', 'Cis', 'D'], [5, 4, 3, 2, 1, 3, 2, 1]],
        'E Harmonic Minor Scale': [[1, 2, 3, 1, 2, 3, 4], ['E', 'Fis', 'G', 'A', 'H', 'C', 'Dis', 'E'], [5, 4, 3, 2, 1, 3, 2, 1]],
        'F Harmonic Minor Scale': [[1, 2, 3, 4, 1, 2, 3], ['F', 'G', 'As', 'B', 'C', 'Des', 'E', 'F'], [5, 4, 3, 2, 1, 3, 2, 1]],
        'G Harmonic Minor Scale': [[1, 2, 3, 1, 2, 3, 4], ['G', 'A', 'B', 'C', 'D', 'Es', 'Fis', 'G'], [5, 4, 3, 2, 1, 3, 2, 1]],
        'A Harmonic Minor Scale': [[1, 2, 3, 1, 2, 3, 4], ['A', 'H', 'C', 'D', 'E', 'F', 'Gis', 'A'], [5, 4, 3, 2, 1, 3, 2, 1]],
        'B Harmonic Minor Scale': [[1, 2, 3, 1, 2, 3, 4], ['H', 'Cis', 'D', 'E', 'Fis', 'G', 'Ais', 'H'], [4, 3, 2, 1, 4, 3, 2, 1, 3, 2, 1]],
        'C Sharp Harmonic Minor Scale': [[2, 3, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3], ['Cis', 'Dis', 'E', 'Fis', 'Gis', 'A', 'His', 'Cis'],
                                         [3, 2, 1, 4, 3, 2, 1, 3, 2, 1, 4, 3, 2, 1]],
        'E Flat Harmonic Minor Scale': [[2, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3], ['Es', 'F', 'Ges', 'As', 'B', 'Ces', 'D', 'Es'],
                                        [2, 1, 4, 3, 2, 1, 3, 2, 1, 4, 3, 2, 1, 3, 2]],
        'F Sharp Harmonic Minor Scale': [[2, 3, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3], ['Fis', 'Gis', 'A', 'H', 'Cis', 'D', 'Eis', 'Fis'],
                                         [4, 3, 2, 1, 3, 2, 1, 4, 3, 2, 1, 3, 2, 1, 2]],
        'G Sharp Harmonic Minor Scale': [[2, 3, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3],
                                         ['Gis', 'Ais', 'H', 'Cis', 'Dis', 'E', 'Fisis(!)', 'Gis'],
                                         [3, 2, 1, 4, 3, 2, 1, 3, 2, 1, 4, 3, 2, 1, 2]],
        'B Flat Harmonic Minor Scale': [[2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 4], ['B', 'C', 'Des', 'Es', 'F', 'Ges', 'A', 'B'],
                                        [2, 1, 3, 2, 1, 4, 3, 2, 1, 3, 2, 1, 4, 3, 2]],

    }

    Minor_Scales_Melodic = {
        # https://mypianoteacher.net/resources/learn-to-play-scales/all-minor-scales-melodic/
        'C Melodic Minor Scale': [[1, 2, 3, 1, 2, 3, 4], ['C', 'D', 'Es', 'F', 'G', 'A', 'H', 'C', 'B', 'As', 'G', 'F', 'Es', 'D', 'C'],
                                  [5, 4, 3, 2, 1, 3, 2, 1]],
        'D Melodic Minor Scale': [[1, 2, 3, 1, 2, 3, 4], ['D', 'E', 'F', 'G', 'A', 'H', 'Cis', 'D', 'C', 'B', 'A', 'G', 'F', 'E', 'D'],
                                  [5, 4, 3, 2, 1, 3, 2, 1]],
        'E Melodic Minor Scale': [[1, 2, 3, 1, 2, 3, 4], ['E', 'Fis', 'G', 'A', 'H', 'Cis', 'Dis', 'E', 'D', 'C', 'H', 'A', 'G', 'F', 'E'],
                                  [5, 4, 3, 2, 1, 3, 2, 1]],
        'F Melodic Minor Scale': [[1, 2, 3, 4, 1, 2, 3], ['F', 'G', 'As', 'B', 'C', 'D', 'E', 'F', 'Es', 'Des', 'C', 'B', 'As', 'G', 'F'],
                                  [5, 4, 3, 2, 1, 3, 2, 1]],
        'G Melodic Minor Scale': [[1, 2, 3, 1, 2, 3, 4], ['G', 'A', 'B', 'C', 'D', 'E', 'Fis', 'G', 'F', 'Es', 'D', 'C', 'B', 'A', 'G'],
                                  [5, 4, 3, 2, 1, 3, 2, 1]],
        'A Melodic Minor Scale': [[1, 2, 3, 1, 2, 3, 4], ['A', 'H', 'C', 'D', 'E', 'Fis', 'Gis', 'A', 'G', 'F', 'E', 'D', 'C', 'H', 'A'],
                                  [5, 4, 3, 2, 1, 3, 2, 1]],
        'B Melodic Minor Scale': [[1, 2, 3, 1, 2, 3, 4], ['H', 'Cis', 'D', 'E', 'Fis', 'Gis', 'Ais', 'H', 'A', 'G', 'Fis', 'D', 'Cis', 'H'],
                                  [4, 3, 2, 1, 4, 3, 2, 1, 3, 2, 1]],
        'C Sharp Melodic Minor Scale': [
            [2, 3, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 4, 1, 'Cis = 3 start descend', 2, 1, 3, 2, 1, 4, 3, 2, 1, 3, 2, 1, 3, 2],
            ['Cis', 'Dis', 'E', 'Fis', 'Gis', 'Ais', 'His', 'Cis', 'H', 'A', 'Gis', 'Fis', 'E', 'Dis', 'Cis'],
            [3, 2, 1, 4, 3, 2, 1, 3, 2, 1, 4, 3, 2, 1, 'Cis = 2 start descend', 1, 2, 3, 4, 1, 3, 2, 1, 2, 3, 4, 1, 2, 3]],
        'E Flat Melodic Minor Scale': [[2, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3],
                                       ['Es', 'F', 'Ges', 'As', 'B', 'C', 'D', 'Es', 'Des', 'Ces', 'B', 'As', 'Ges', 'F', 'Es'],
                                       [2, 1, 4, 3, 2, 1, 3, 2, 1, 4, 3, 2, 1, 3, 2]],
        'F Sharp Melodic Minor Scale': [
            [2, 3, 12, 3, 4, 1, 2, 3, 1, 2, 3, 4, 1, 'Fis = 3 start descend', 2, 1, 3, 2, 1, 4, 3, 2, 1, 3, 2, 1, 3, 2],
            ['Fis', 'Gis', 'A', 'H', 'Cis', 'Dis', 'Eis', 'Fis', 'E', 'D', 'Cis', 'H', 'A', 'Gis', 'Fis'],
            [4, 3, 2, 1, 3, 2, 1, 4, 3, 2, 1, 3, 2, 1, 'Fis=2 start descend', 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 4]],
        'G Sharp Melodic Minor Scale': [
            [2, 3, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 1, 2, 'Gis = 3 start descend', 2, 1, 3, 2, 1, 4, 3, 2, 1, 3, 2, 1, 3, 2],
            ['Gis', 'Ais', 'H', 'Cis', 'Dis', 'Eis', 'Fisis(!)', 'Gis', 'Fis', 'E', 'Dis', 'Cis', 'H', 'Ais', 'Gis'],
            [3, 2, 1, 4, 3, 2, 1, 3, 2, 1, 4, 3, 2, 1, 'Gis = 2 start descend', 3, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3]],
        'B Flat Melodic Minor Scale': [[2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 4],
                                       ['B', 'C', 'Des', 'Es', 'F', 'G', 'A', 'B', 'As', 'Ges', 'F', 'Es', 'Des', 'C', 'B'],
                                       [2, 1, 3, 2, 1, 4, 3, 2, 1, 3, 2, 1, 4, 3, 2]],

    }

    picked_arpeggio = random.choice(list(Arpeggio))
    print_results(dictionary=Arpeggio, name=picked_arpeggio)

    list_of_scales = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'D Flat', 'E Flat', 'F Sharp', 'A Flat', 'B Flat']
    picked_scale = random.choice(list_of_scales)

    print_vorzeichen_dur(picked_scale)
    print_results(Major_Scales, f"{picked_scale} Major Scale")
    relative_key = pick_relative_key(picked_scale)
    print_vorzeichen_moll(relative_key)
    relative_key=relative_key.replace(" Minor","")
    print_results(Minor_Scales_Harmonic, f"{relative_key} Harmonic Minor Scale")
    print_results(Minor_Scales_Melodic, f"{relative_key} Melodic Minor Scale")
    print_harmonic_melodic_info()
