Web services
============

Most data in GPCRdb is available programmatically via a REST API.

API reference
-------------

Each endpoint is described in the `API reference`_.

.. _API reference: https://gpcrdb.org/services/reference/

Examples
--------

Python 3 with requests
^^^^^^^^^^^^^^^^^^^^^^

This is the recommended approach. Requires installation of the `requests library`_.

.. _requests library: https://requests.readthedocs.io

::

    import requests

    # fetch a protein
    url = 'https://gpcrdb.org/services/protein/adrb2_human/'
    response = requests.get(url)
    protein_data = response.json()
    print(protein_data)
    print(protein_data['sequence'])

    # fetch an alignment
    url = 'https://gpcrdb.org/services/alignment/protein/adrb1_human,adrb2_human,adrb3_human/TM3,TM5,TM6/'
    response = requests.get(url)
    alignment_data = response.json()
    for protein, sequence in alignment_data.items():
        print(protein)
        print(sequence)

Python 3 with urllib
^^^^^^^^^^^^^^^^^^^^

::

    from urllib.request import urlopen
    import json

    # fetch a protein
    url = 'https://gpcrdb.org/services/protein/adrb2_human/'
    response = urlopen(url)
    protein_data = json.loads(response.read().decode('utf-8'))
    print(protein_data)
    print(protein_data['sequence'])

    # fetch an alignment
    url = 'https://gpcrdb.org/services/alignment/protein/adrb1_human,adrb2_human,adrb3_human/TM3,TM5,TM6/'
    response = urlopen(url)
    alignment_data = json.loads(response.read().decode('utf-8'))
    for protein, sequence in alignment_data.items():
        print(protein)
        print(sequence)

Python 2 with urllib2
^^^^^^^^^^^^^^^^^^^^^

::

    from urllib2 import urlopen
    import json

    # fetch a protein
    url = 'https://gpcrdb.org/services/protein/adrb2_human/'
    response = urlopen(url)
    protein_data = json.loads(response.read())
    print protein_data
    print protein_data['sequence']

    # fetch an alignment
    url = 'https://gpcrdb.org/services/alignment/protein/adrb1_human,adrb2_human,adrb3_human/TM3,TM5,TM6/'
    response = urlopen(url)
    alignment_data = json.loads(response.read())
    for protein, sequence in alignment_data.iteritems():
        print protein
        print sequence
