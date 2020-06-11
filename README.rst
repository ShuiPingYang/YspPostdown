YspPostdown
=========

|Python Version| |PyPI version|

    *Generate markdown API document from Postman.*

Installation
-------------

.. code:: shell

    pip install ysp_postdown


Usage
------

* **Export JSON from postman**
    Export your collection from Postman(Only support to Collection v2 for now).
    You could get a JSON file.

    .. figure:: https://raw.githubusercontent.com/YangShuiPing/YspPostdown/master/imgs/step-1.png

        Step One: Select the collection which you wanna export.


    .. figure:: https://raw.githubusercontent.com/YangShuiPing/YspPostdown/master/imgs/step-2.png

        Step Two: Find the import button and click it.


    .. figure:: https://raw.githubusercontent.com/YangShuiPing/YspPostdown/master/imgs/step-3.png

        Step Three: Export your collection as *collection v2*.



* **Run** ``ysp_postdown`` **to generate markdown document**::

        ysp_postdown xxx.json xxx.md


And you will get your API document which is markdown formatting.



`Click here to see an example generated. <https://github.com/YangShuiPing/YspPostdown/tree/master/demo>`_





.. |Python Version| image:: https://img.shields.io/badge/python-2&3-brightgreen.svg?style=flat-square
    :target: https://pypi.python.org/pypi/YspPostdown
.. |PyPI version| image:: https://img.shields.io/pypi/v/YspPostdown.svg?style=flat-square
    :target: https://pypi.python.org/pypi/YspPostdown

