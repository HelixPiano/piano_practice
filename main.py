import random
from colorama import init, Fore, Style

init(convert=True)

def print_results(dictionary, name):
    result = dictionary.get(name)
    print(f"Name: {Fore.GREEN + name}")
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
    print(f"Tonart: {Fore.GREEN + name} Dur")
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
    elif name == 'Des':
        print(f"Vorzeichen: B Es As Des Ges")
    elif name == 'Es':
        print(f"Vorzeichen: B Es As")
    elif name == 'Fis':
        print(f"Vorzeichen: Fis Cis Gid Dis Ais Eis")
    elif name == 'As':
        print(f"Vorzeichen: Gis Ais His Cis Dis Eis Fisis(!)")
    elif name == 'B':
        print(f"Vorzeichen: B Es")
    else:
        assert False, "Kann Vorzeichen für Dur nicht finden"
    print('----------------------------------------------')


def print_vorzeichen_moll(name):
    print(f"Parallele Molltonart: {Fore.GREEN + name}/Moll")
    print(Style.RESET_ALL)
    if name == 'A Moll':
        print(f"Ohne Vorzeichen")
    elif name == 'D Moll':
        print(f"Vorzeichen: B")
    elif name == 'E Moll':
        print(f"Vorzeichen: Fis")
    elif name == 'H Moll':
        print(f"Vorzeichen: Fis Cis")
    elif name == 'Fis Moll':
        print(f"Vorzeichen: Fis Cis Gis")
    elif name == 'Cis Moll':
        print(f"Vorzeichen: Fis Cis Gis Dis")
    elif name == 'Gis Moll':
        print(f"Vorzeichen: Fis Cis Gid Dis Ais")
    elif name == 'H Moll':
        print(f"Vorzeichen: B Es As Des Ges")
    elif name == 'C Moll':
        print(f"Vorzeichen: B Es As")
    elif name == 'Es Moll':
        print(f"Vorzeichen: B Es As Des Ges Ces")
    elif name == 'F Moll':
        print(f"Vorzeichen: B Es As Des")
    elif name == 'G Moll':
        print(f"Vorzeichen: B Es")
    else:
        assert False, "Kann Vorzeichen für Moll nicht finden"
    print('----------------------------------------------')


def pick_relative_key(name):
    if name == 'C':
        return f"A Moll"
    elif name == 'F':
        return f"D Moll"
    elif name == 'G':
        return f"E Moll"
    elif name == 'D':
        return f"H Moll"
    elif name == 'A':
        return f"Fis Moll"
    elif name == 'E':
        return f"Cis Moll"
    elif name == 'H':
        return f"Gis Moll"
    elif name == 'Des':
        return f"H Moll"
    elif name == 'Es':
        return f"C Moll"
    elif name == 'Fis':
        print('Redirectirect to D Sharp Moll to Es Moll')
        return f"Es Moll"
    elif name == 'As':
        return f"F Moll"
    elif name == 'B':
        return f"G Moll"
    else:
        assert False, "Can't find parallel key"


if __name__ == '__main__':
    Arpeggio = {
        # https://mypianoteacher.net/resources/learn-to-play-scales/all-major-arpeggios/
        'C-Dur Arpeggio': [[1, 2, 3, 1, 2, 3, 5], ['C', 'E', 'G', 'C', 'E', 'G', 'C'], [5, 3, 2, 1, 3, 2, 1]],
        'D-Dur Arpeggio': [[1, 2, 3, 1, 2, 3, 5], ['D', 'Fis', 'A', 'D', 'Fis', 'D'], [5, 3, 2, 1, 3, 2, 1]],
        'E-Dur Arpeggio': [[1, 2, 3, 1, 2, 3, 5], ['E', 'Gis', 'H', 'E', 'Gis', 'H', 'E'], [5, 3, 2, 1, 3, 2, 1]],
        'F-Dur Arpeggio': [[1, 2, 3, 1, 2, 3, 5], ['F', 'A', 'C', 'F', 'A', 'C', 'F'], [5, 3, 2, 1, 3, 2, 1]],
        'G-Dur Arpeggio': [[1, 2, 3, 1, 2, 3, 5], ['G', 'H', 'D', 'G', 'H', 'D', 'G'], [5, 3, 2, 1, 3, 2, 1]],
        'A-Dur Arpeggio': [[1, 2, 3, 1, 2, 3, 5], ['A', 'Cis', 'E', 'A', 'Cis', 'E', 'A'], [5, 3, 2, 1, 3, 2, 1]],
        'H-Dur Arpeggio': [[1, 2, 3, 1, 2, 3, 5], ['H', 'Dis', 'Fis', 'H', 'Dis', 'Fis', 'H'], [5, 3, 2, 1, 3, 2, 1]],
        'Des-Dur Arpeggio': [[2, 1, 2, 4, 1, 2, 4], ['Des', 'F', 'As', 'Des', 'F', 'As', 'Des'], [2, 1, 4, 2, 1, 4, 2]],
        'Es-Dur Arpeggio': [[2, 1, 2, 4, 1, 2, 4], ['Es', 'G', 'B', 'Es', 'G', 'B', 'Es'], [2, 1, 4, 2, 1, 4, 2]],
        'Fis-Dur Arpeggio': [[1, 2, 3, 1, 2, 3, 5], ['Fis', 'Ais', 'Cis', 'Fis', 'Ais', 'Cis', 'Fis'], [5, 3, 2, 1, 3, 2, 1]],
        'As-Dur Arpeggio': [[2, 1, 2, 4, 1, 2, 4], ['As', 'C', 'Es', 'As', 'C', 'Es', 'As'], [2, 1, 4, 2, 1, 4, 2]],
        'B-Dur Arpeggio': [[3, 2, 1, 3, 2, 1, 2], ['B', 'D', 'F', 'B', 'D', 'F', 'B'], [3, 2, 1, 3, 2, 1, 2]],

        # https://mypianoteacher.net/resources/learn-to-play-scales/all-minor-arpeggios/
        'C Moll Arpeggio': [[1, 2, 3, 1, 2, 3, 5], ['C', 'Es', 'G', 'C', 'Es', 'G', 'C'], [5, 3, 2, 1, 3, 2, 1]],
        'D Moll Arpeggio': [[1, 2, 3, 1, 2, 3, 5], ['D', 'F', 'A', 'D', 'F', 'A', 'D'], [5, 3, 2, 1, 3, 2, 1]],
        'E Moll Arpeggio': [[1, 2, 3, 1, 2, 3, 5], ['E', 'G', 'H', 'E', 'G', 'H', 'E'], [5, 3, 2, 1, 3, 2, 1]],
        'F Moll Arpeggio': [[1, 2, 3, 1, 2, 3, 5], ['F', 'As', 'C', 'F', 'As', 'C', 'F'], [5, 4, 2, 1, 4, 2, 1]],
        'G Moll Arpeggio': [[1, 2, 3, 1, 2, 3, 5], ['G', 'B', 'D', 'G', 'B', 'D', 'G'], [5, 3, 2, 1, 3, 2, 1]],
        'A Moll Arpeggio': [[1, 2, 3, 1, 2, 3, 5], ['A', 'C', 'E', 'A', 'C', 'E', 'A'], [5, 3, 2, 1, 3, 2, 1]],
        'H Moll Arpeggio': [[1, 2, 3, 1, 2, 3, 5], ['H', 'D', 'Fis', 'H', 'D', 'Fis', 'H'], [5, 4, 2, 1, 4, 2, 1]],
        'Cis Moll Arpeggio': [[2, 1, 2, 4, 1, 2, 4], ['Cis', 'E', 'Gis', 'Cis', 'E', 'Gis', 'Cis'], [5, 3, 2, 1, 3, 2, 1]],
        'Es Moll Arpeggio': [[1, 2, 3, 1, 2, 3, 5], ['Es', 'Ges', 'B', 'Es', 'Ges', 'B', 'Es'], [5, 4, 2, 1, 4, 2, 1]],
        'Fis Moll Arpeggio': [[2, 1, 2, 4, 1, 2, 4], ['Fis', 'A', 'Cis', 'Fis', 'A', 'Cis', 'Fis'], [2, 1, 4, 2, 1, 4, 2]],
        'Gis Moll Arpeggio': [[2, 1, 2, 4, 1, 2, 4], ['Gis', 'H', 'Dis', 'Gis', 'H', 'Dis', 'Gis'], [2, 1, 4, 2, 1, 4, 2]],
        'B Moll Arpeggio': [[2, 3, 1, 2, 3, 1, 2], ['B', 'Des', 'F', 'B', 'Des', 'F', 'B'], [3, 2, 1, 3, 2, 1, 2]],

    }

    Major_Scales = {
        # https://mypianoteacher.net/resources/learn-to-play-scales/all-major-scales/
        'C-Dur Tonleiter': [[1, 2, 3, 1, 2, 3, 4], ['C', 'D', 'E', 'F', 'G', 'A', 'H', 'C'], [5, 4, 3, 2, 1, 3, 2, 1]],
        'D-Dur Tonleiter': [[1, 2, 3, 1, 2, 3, 4], ['D', 'E', 'Fis', 'G', 'A', 'H', 'Cis', 'D'], [5, 4, 3, 2, 1, 3, 2, 1]],
        'E-Dur Tonleiter': [[1, 2, 3, 1, 2, 3, 4], ['E', 'Fis', 'Gis', 'A', 'H', 'Cis', 'Dis', 'E'], [5, 4, 3, 2, 1, 3, 2, 1]],
        'F-Dur Tonleiter': [[1, 2, 3, 4, 1, 2, 3], ['F', 'G', 'A', 'B', 'C', 'D', 'E', 'F'], [5, 4, 3, 2, 1, 3, 2, 1]],
        'G-Dur Tonleiter': [[1, 2, 3, 1, 2, 3, 4], ['G', 'A', 'H', 'C', 'D', 'E', 'Fis', 'G'], [5, 4, 3, 2, 1, 3, 2, 1]],
        'A-Dur Tonleiter': [[1, 2, 3, 1, 2, 3, 4], ['A', 'H', 'Cis', 'D', 'E', 'Fis', 'Gis', 'A'], [5, 4, 3, 2, 1, 3, 2, 1]],
        'H-Dur Tonleiter': [[1, 2, 3, 1, 2, 3, 4], ['H', 'Cis', 'Dis', 'E', 'Fis', 'Gis', 'Ais', 'H'], [4, 3, 2, 1, 4, 3, 2, 1, 3, 2, 1, 4]],
        'Des-Dur Tonleiter': [[2, 3, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 4], ['Des', 'Es', 'F', 'Ges', 'As', 'B', 'C', 'Des'],
                               [3, 2, 1, 4, 3, 2, 1, 3, 2]],
        'Es-Dur Tonleiter': [[2, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 4], ['Es', 'F', 'G', 'As', 'B', 'C', 'D', 'Es'],
                               [3, 2, 1, 4, 3, 2, 1, 3, 2, 1, 4]],
        'Fis-Dur Tonleiter': [[2, 3, 4, 1, 2, 3, 1, 2], ['Fis', 'Gis', 'Ais', 'H', 'Cis', 'Dis', 'Eis', 'Fis'], [4, 3, 2, 1, 3, 2, 1, 4]],
        'As-Dur Tonleiter': [[2, 3, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3], ['As', 'B', 'C', 'Des', 'Es', 'F', 'G', 'As'],
                               [3, 2, 1, 4, 3, 2, 1, 3, 2, 1, 4, 3, 2, 1, 2]],
        'B-Dur Tonleiter': [[2, 1, 2, 3, 1, 2, 3, 4, 1], ['B', 'C', 'D', 'Es', 'F', 'G', 'A', 'B'], [3, 2, 1, 4, 3, 2, 1, 3]],
    }

    Minor_Scales_Harmonic = {
        # https://mypianoteacher.net/resources/learn-to-play-scales/all-minor-scales-harmonic/
        'C Moll Harmonisch Tonleiter': [[1, 2, 3, 1, 2, 3, 4], ['C', 'D', 'Es', 'F', 'G', 'As', 'H', 'C'], [5, 4, 3, 2, 1, 3, 2, 1]],
        'D Moll Harmonisch Tonleiter': [[1, 2, 3, 1, 2, 3, 4], ['D', 'E', 'F', 'G', 'A', 'B', 'Cis', 'D'], [5, 4, 3, 2, 1, 3, 2, 1]],
        'E Moll Harmonisch Tonleiter': [[1, 2, 3, 1, 2, 3, 4], ['E', 'Fis', 'G', 'A', 'H', 'C', 'Dis', 'E'], [5, 4, 3, 2, 1, 3, 2, 1]],
        'F Moll Harmonisch Tonleiter': [[1, 2, 3, 4, 1, 2, 3], ['F', 'G', 'As', 'B', 'C', 'Des', 'E', 'F'], [5, 4, 3, 2, 1, 3, 2, 1]],
        'G Moll Harmonisch Tonleiter': [[1, 2, 3, 1, 2, 3, 4], ['G', 'A', 'B', 'C', 'D', 'Es', 'Fis', 'G'], [5, 4, 3, 2, 1, 3, 2, 1]],
        'A Moll Harmonisch Tonleiter': [[1, 2, 3, 1, 2, 3, 4], ['A', 'H', 'C', 'D', 'E', 'F', 'Gis', 'A'], [5, 4, 3, 2, 1, 3, 2, 1]],
        'H Moll Harmonisch Tonleiter': [[1, 2, 3, 1, 2, 3, 4], ['H', 'Cis', 'D', 'E', 'Fis', 'G', 'Ais', 'H'], [4, 3, 2, 1, 4, 3, 2, 1, 3, 2, 1]],
        'Cis Moll Harmonisch Tonleiter': [[2, 3, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3], ['Cis', 'Dis', 'E', 'Fis', 'Gis', 'A', 'His', 'Cis'],
                                         [3, 2, 1, 4, 3, 2, 1, 3, 2, 1, 4, 3, 2, 1]],
        'Es Moll Harmonisch Tonleiter': [[2, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3], ['Es', 'F', 'Ges', 'As', 'B', 'Ces', 'D', 'Es'],
                                        [2, 1, 4, 3, 2, 1, 3, 2, 1, 4, 3, 2, 1, 3, 2]],
        'Fis Moll Harmonisch Tonleiter': [[2, 3, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3], ['Fis', 'Gis', 'A', 'H', 'Cis', 'D', 'Eis', 'Fis'],
                                         [4, 3, 2, 1, 3, 2, 1, 4, 3, 2, 1, 3, 2, 1, 2]],
        'Gis Moll Harmonisch Tonleiter': [[2, 3, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3],
                                         ['Gis', 'Ais', 'H', 'Cis', 'Dis', 'E', 'Fisis(!)', 'Gis'],
                                         [3, 2, 1, 4, 3, 2, 1, 3, 2, 1, 4, 3, 2, 1, 2]],
        'B Moll Harmonisch Tonleiter': [[2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 4], ['B', 'C', 'Des', 'Es', 'F', 'Ges', 'A', 'B'],
                                        [2, 1, 3, 2, 1, 4, 3, 2, 1, 3, 2, 1, 4, 3, 2]],

    }

    Minor_Scales_Melodic = {
        # https://mypianoteacher.net/resources/learn-to-play-scales/all-minor-scales-melodic/
        'C Moll Melodisch Tonleiter': [[1, 2, 3, 1, 2, 3, 4], ['C', 'D', 'Es', 'F', 'G', 'A', 'H', 'C', 'B', 'As', 'G', 'F', 'Es', 'D', 'C'],
                                  [5, 4, 3, 2, 1, 3, 2, 1]],
        'D Moll Melodisch Tonleiter': [[1, 2, 3, 1, 2, 3, 4], ['D', 'E', 'F', 'G', 'A', 'H', 'Cis', 'D', 'C', 'B', 'A', 'G', 'F', 'E', 'D'],
                                  [5, 4, 3, 2, 1, 3, 2, 1]],
        'E Moll Melodisch Tonleiter': [[1, 2, 3, 1, 2, 3, 4], ['E', 'Fis', 'G', 'A', 'H', 'Cis', 'Dis', 'E', 'D', 'C', 'H', 'A', 'G', 'F', 'E'],
                                  [5, 4, 3, 2, 1, 3, 2, 1]],
        'F Moll Melodisch Tonleiter': [[1, 2, 3, 4, 1, 2, 3], ['F', 'G', 'As', 'B', 'C', 'D', 'E', 'F', 'Es', 'Des', 'C', 'B', 'As', 'G', 'F'],
                                  [5, 4, 3, 2, 1, 3, 2, 1]],
        'G Moll Melodisch Tonleiter': [[1, 2, 3, 1, 2, 3, 4], ['G', 'A', 'B', 'C', 'D', 'E', 'Fis', 'G', 'F', 'Es', 'D', 'C', 'B', 'A', 'G'],
                                  [5, 4, 3, 2, 1, 3, 2, 1]],
        'A Moll Melodisch Tonleiter': [[1, 2, 3, 1, 2, 3, 4], ['A', 'H', 'C', 'D', 'E', 'Fis', 'Gis', 'A', 'G', 'F', 'E', 'D', 'C', 'H', 'A'],
                                  [5, 4, 3, 2, 1, 3, 2, 1]],
        'H Moll Melodisch Tonleiter': [[1, 2, 3, 1, 2, 3, 4], ['H', 'Cis', 'D', 'E', 'Fis', 'Gis', 'Ais', 'H', 'A', 'G', 'Fis', 'D', 'Cis', 'H'],
                                  [4, 3, 2, 1, 4, 3, 2, 1, 3, 2, 1]],
        'Cis Moll Melodisch Tonleiter': [
            [2, 3, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 4, 1, 'Cis = 3 start descend', 2, 1, 3, 2, 1, 4, 3, 2, 1, 3, 2, 1, 3, 2],
            ['Cis', 'Dis', 'E', 'Fis', 'Gis', 'Ais', 'His', 'Cis', 'H', 'A', 'Gis', 'Fis', 'E', 'Dis', 'Cis'],
            [3, 2, 1, 4, 3, 2, 1, 3, 2, 1, 4, 3, 2, 1, 'Cis = 2 start descend', 1, 2, 3, 4, 1, 3, 2, 1, 2, 3, 4, 1, 2, 3]],
        'Es Moll Melodisch Tonleiter': [[2, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3],
                                       ['Es', 'F', 'Ges', 'As', 'B', 'C', 'D', 'Es', 'Des', 'Ces', 'B', 'As', 'Ges', 'F', 'Es'],
                                       [2, 1, 4, 3, 2, 1, 3, 2, 1, 4, 3, 2, 1, 3, 2]],
        'Fis Moll Melodisch Tonleiter': [
            [2, 3, 12, 3, 4, 1, 2, 3, 1, 2, 3, 4, 1, 'Fis = 3 start descend', 2, 1, 3, 2, 1, 4, 3, 2, 1, 3, 2, 1, 3, 2],
            ['Fis', 'Gis', 'A', 'H', 'Cis', 'Dis', 'Eis', 'Fis', 'E', 'D', 'Cis', 'H', 'A', 'Gis', 'Fis'],
            [4, 3, 2, 1, 3, 2, 1, 4, 3, 2, 1, 3, 2, 1, 'Fis=2 start descend', 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 4]],
        'Gis Moll Melodisch Tonleiter': [
            [2, 3, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 1, 2, 'Gis = 3 start descend', 2, 1, 3, 2, 1, 4, 3, 2, 1, 3, 2, 1, 3, 2],
            ['Gis', 'Ais', 'H', 'Cis', 'Dis', 'Eis', 'Fisis(!)', 'Gis', 'Fis', 'E', 'Dis', 'Cis', 'H', 'Ais', 'Gis'],
            [3, 2, 1, 4, 3, 2, 1, 3, 2, 1, 4, 3, 2, 1, 'Gis = 2 start descend', 3, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3]],
        'B Moll Melodisch Tonleiter': [[2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 4],
                                       ['B', 'C', 'Des', 'Es', 'F', 'G', 'A', 'B', 'As', 'Ges', 'F', 'Es', 'Des', 'C', 'B'],
                                       [2, 1, 3, 2, 1, 4, 3, 2, 1, 3, 2, 1, 4, 3, 2]],

    }

    picked_arpeggio = random.choice(list(Arpeggio))
    print_results(dictionary=Arpeggio, name=picked_arpeggio)

    list_of_scales = ['C', 'D', 'E', 'F', 'G', 'A', 'H', 'Des', 'Es', 'Fis', 'As', 'B']
    picked_scale = random.choice(list_of_scales)

    print_vorzeichen_dur(picked_scale)
    print_results(Major_Scales, f"{picked_scale}-Dur Tonleiter")
    relative_key = pick_relative_key(picked_scale)
    print_vorzeichen_moll(relative_key)
    relative_key=relative_key.replace(" Moll","")
    print_results(Minor_Scales_Harmonic, f"{relative_key} Moll Harmonisch Tonleiter")
    print_results(Minor_Scales_Melodic, f"{relative_key} Moll Melodisch Tonleiter")
    print_harmonic_melodic_info()
