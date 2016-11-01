#!/bin/bash

pid() {
    echo `ps axu | grep -i $1 | sed -e "s/  */ /g" | cut -d" " -f2`
}

killp() {
    echo $1
    kill $1
}

killp `pid "[s]tartup\.py"`
killp `pid "[d]etector\.py"`
killp `pid "[d]etector\.sh"`
killp `pid "[g]runt"`
killp `pid "[p]ython.*app\.py"`

