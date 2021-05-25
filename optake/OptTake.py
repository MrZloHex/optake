from sys import argv

class OptTake:
    def __init__(self):
        self._options = {}
        self._arguments = []

    def add_argument(self, option: str, has_value: bool):
        """
        Adding arguments that is need to be parsed

        :param option: name of option e.g "-v"
        :param has_value: default - "false", but if opt is needful to get a value - "true"
        """

        self._options[option] = has_value
        self._arguments.append(option)

    def _take_opts(self) -> list:
        """

        :return: options with values
        :rtype: list of tuples
        """

        option = []
        if len(argv) == 1:
            return option
        else:
            # checking all arguments
            for opt in argv:
                i = 1
                # if arguments was described before
                if opt in self._arguments:
                    # checking for having value
                    if self._options[opt]:
                        # if dont have required value
                        if len(argv) >= i+1:
                            option.append((str(argv[i]), str(argv[i+1])))
                            i += 2
                        else:
                            print(f"There are no value for opt - {opt}")
                    else:
                        option.append((str(argv[i]), None))
                        i += 1

        return option



    def optake(self) -> list:
        """
        Discover amount of option, while call python script

        :return: amount od options
        :rtype: list
        """

        option = self._take_opts()
        return option
