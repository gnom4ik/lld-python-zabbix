test scripts on bash and python for zabbix lld

Репозиторий создан для работы и накопления опыта в написании обнаружений LLD Zabbix, а так же для изучения языка програмирования Python.
cd ~/lld-python-zabbix/
cp -r /

chmod +x /share/zabbix/externalscripts/*

Устанавливаем lm-sensors (для debian) -

apt install lm-sensors

Выполняем команду (добавление прав на выполнение) -

echo "zabbix ALL=(ALL) NOPASSWD: /usr/sbin/smartctl,/sbin/mdadm" > /etc/sudoers.d/zabbix
