# -*- coding: utf-8 -*-

# m_softdev/src/m_softdev/m_iters.py

import json
from types import SimpleNamespace


class IterableNamespace(SimpleNamespace):
    """ Class wextending SimpleNamespace, ith additional properties"""

    def __init__(self, keys_frozen=False, frozen=False, **kwargs):
        """Constructor

        Args:
            keys_frozen (bool, optional): a flag to control if object                                has been initialized; defaults to False.
            frozen (bool, optional): flag preventing change of attributes;
                defaults to False.
            **kwargs: _description_
        """
        # To avoid recursion during initialization object.__setattr__
        # must be used:
        object.__setattr__(self, '_keys_frozen', keys_frozen)
        object.__setattr__(self, '_frozen', frozen)
        object.__setattr__(self, '_initialized', False)

        # Ustaw początkowe atrybuty przekazane do konstruktora
        for key, value in kwargs.items():
            object.__setattr__(self, key, value) # Użyj object.__setattr__
            #                do bezpiecznego ustawiania początkowych wartości

        self._indices = {i: key for i, key in enumerate(self.keys())}

        if self._indices:
            object.__setattr__(self, '_initialized', True)

    def __getattribute__(self, name):
        # IPORTANT: super().__getattribute__ must ALWAYS be used for
        # getting attribute values, to avoid infinite recursion
        try:
            return super().__getattribute__(name)
        except AttributeError:
            # __getattribute__ is to return a value always; if nothing
            # is found, it must raise AttributeError
            raise

    def __getitem__(self, key):
        return self.__getattribute__(self._indices[key])

    def __iter__(self):
        # super().__getattribute__('__dict__') is to avoid infinite recursion
        return iter(key for key in
                    super().__getattribute__('__dict__').keys()\
                    if not key.startswith('_'))

    def __len__(self):
        return len(self.items())

    def __setattr__(self, name, value):
        # Bezpieczny odczyt flag inicjalizacji i zamrożenia,
        # unikając rekurencji przez object.__getattribute__.
        loc = f"{FTITLE}.{__name__}.__setattr__"
        is_initialized = object.__getattribute__(self, '_initialized')
        is_frozen = object.__getattribute__(self, '_frozen')
        are_keys_frozen = object.__getattribute__(self, '_keys_frozen')
        name_in_dict = name in self.__dict__
        # cprintd(f"{is_initialized = }, {is_frozen = }", location=loc)

        if is_initialized and is_frozen:
            # Jeśli obiekt jest zainicjalizowany I zamrożony,
            # zabroń modyfikacji/dodawania atrybutów.
            err = (f"Cannot modify attribute '{name}' in a frozen "
                   f"{type(self).__name__} instance after initialization.")
            raise AttributeError(err)
        elif is_initialized and not name_in_dict and are_keys_frozen\
                and not is_frozen:
            err = (f"Cannot add new attribute '{name}' "
                   f"({self._keys_frozen = }).")
            raise AttributeError(err)
        else:
            # W przeciwnym razie (jeszcze nie zainicjalizowany LUB nie zamrożony),
            # pozwól na ustawienie atrybutu w standardowy sposób.
            object.__setattr__(self, name, value)

    def __str__(self) -> str:
        # return self.__class__.__name__ + "\n" + self._string()
        return (self.__class__.__name__ +
                "(" + ", ".join(f"{k}={v!r}" for k, v in self.items()
                                if not k.startswith("_")) + ")")

    def __repr__(self) -> str:
        return (self.__class__.__name__ +
                "(" + ", ".join(f"{k}={v!r}" for k, v in self.items()
                                if not k.startswith("_")) + ")")

    def freeze(self, frozen: bool | None = None, /) -> None:
        """ Freezing/unfreezing the namespace """

        frozen = frozen if frozen is not None\
                else not object.__getattribute__(self, '_frozen')
        object.__setattr__(self, '_frozen', frozen)

    def freeze_keys(self, frozen: bool | None = None, /) -> None:
        """ Freezing/unfreezing keys of the namespace """

        is_initialized = object.__getattribute__(self, '_initialized')
        is_frozen = object.__getattribute__(self, '_frozen')

        if is_initialized and is_frozen:
            # Jeśli obiekt jest zainicjalizowany I zamrożony,
            # zabroń modyfikacji/dodawania atrybutów.
            err = (f"Cannot modify attribute '_keys_frozen' in a frozen "
                   f"{type(self).__name__} instance after initialization.")
            raise AttributeError(err)

        frozen = frozen if frozen is not None\
                else not object.__getattribute__(self, '_keys_frozen')
        object.__setattr__(self, '_keys_frozen', frozen)

    @classmethod
    def from_json(cls, json_name: str):
        """Creating IterableNamespace from json file"""

        with open(json_name) as f:
            return cls(**json.load(f))


    def items(self, hidden: bool = False):
        """ Returning key-value pairs (only public attributes) """

        # return super().__getattribute__('__dict__').items()
        # return (
        #     (k, v)
        #     for k, v in super().__getattribute__('__dict__').items()
        #     if not k.startswith('_')
        # )  # generator
        return dict(
            (k, v) for k, v in super().__getattribute__('__dict__').items()
            if not k.startswith('_') or hidden
        ).items()

    def keys(self, hidden: bool = False):
        """ Returning key-value pairs """

        # return super().__getattribute__('__dict__').keys()
        return tuple(key for key in
                     super().__getattribute__('__dict__').keys()
                     if not key.startswith('_') or hidden)

    def pprint(self, name: str | None = None, hidden: bool = False) -> None:
        """ Pretty printing the namespace

            Args:
                name (str): name of the variable (or None)
                hidden (bool): whether to print hidden attributes
        """

        result = ""
        frozen = " (frozen)" if object.__getattribute__(self, '_frozen')\
                else ""
        header = f"{self.__class__.__name__}"
        if name is not None:
            header += f" '{name}'"
        header += f"{frozen}"

        if len(self.items()) > 0:
            # print(f"{header}\n{self._string(pp=True)}")
            data_dict = object.__getattribute__(self, '__dict__')
            filtered_keys = [k for k in data_dict.keys()
                             if not (k.startswith("_")) or hidden]
            # filtered_keys = [k for k in data_dict.keys()
            #                  if not (k.startswith("_"))]
            # if not filtered_keys: # Jeśli brak widocznych kluczy
            #     return ""

            tab_max = max(len(k) for k in filtered_keys)
            # tab_max = " "

            for k in sorted(filtered_keys):
                v = data_dict[k] # Bezpieczny dostęp do wartości,
                #                  bo klucz jest już w filtered_keys
                tab = (tab_max - len(k)) * " "
                # tab = tab_max
                extra_spc = " " if not isinstance(v, str) else ""
                result += f"{' '*4}{k}:{tab} {extra_spc}{v!r}\n"
                # result += f"{' '*4}{k}:{tab} {v!r}\n"

        print(f"{header}\n{result.rstrip()}")

    def values(self):
        """ Returning key-value pairs """

        return tuple(value for (key, value) in
                     super().__getattribute__('__dict__').items()
                     if not key.startswith('_'))


def chunkify(iterable, size):
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]
