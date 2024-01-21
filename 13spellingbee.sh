 gunzip -c dictionary.gz | grep "r" | grep -v "[^zoncair]" | grep -E ".{4}" | wc
