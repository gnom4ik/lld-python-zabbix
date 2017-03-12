test scripts on bash and python for zabbix lld

Репозиторий создан для работы и накопления опыта в написании обнаружений LLD Zabbix, а так же для изучения языка програмирования Python.

ВАЖНО!!!

Zabbix-agent собран из сырцов + ./configure --prefix=/. В /etc/zabbix_agentd.conf прописан Include=/etc/zabbix_agentd.conf.d/*.conf

apt install lm-sensors

cp -r ~/lld-python-zabbix/etc /etc

cp -r ~/lld-python-zabbix/share /share

chmod +x /share/zabbix/externalscripts/*


