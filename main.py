import random


def print_results(dictionary, name):
    result = dictionary.get(name)
    print(f"Name: {name}")
    print(f"Right hand: {result[0]}")
    print(f"Notes: {result[1]}")
    print(f"Left Hand: {result[2]}")
    print('----------------------------------------------')


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

    Result_arpeggio = random.choice(list(Arpeggio))
    print_results(Arpeggio, Result_arpeggio)

    Result_Major_Scales = random.choice(list(Major_Scales))
    print_results(Major_Scales, Result_Major_Scales)

    Result_Minor_Scales_Harmonic = random.choice(list(Minor_Scales_Harmonic))
    print_results(Minor_Scales_Harmonic, Result_Minor_Scales_Harmonic)

    Result_Minor_Scales_Melodic = random.choice(list(Minor_Scales_Melodic))
    print_results(Minor_Scales_Melodic, Result_Minor_Scales_Melodic)