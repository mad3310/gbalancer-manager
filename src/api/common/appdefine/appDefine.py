#-*- coding: utf-8 -*-
import os

from tornado.options import define

join = os.path.join
dirname = os.path.dirname

base_dir = os.path.abspath(dirname(dirname(dirname(__file__))))

define('port', default = 9888, type = int, help = 'app listen port')
define('debug', default = False, type = bool, help = 'is debuging?')
define('sitename', default = "gbalancer manager", help = 'site name')
define('domain', default = "letv.com", help = 'domain name')

define('send_email_switch', default = True, type = bool, help = 'the flag of if send error email')
define('admins', default = ("Mcluster_Members <Mcluster_Members@letv.com>;",), help = 'admin email address')
define('smtp_host', default = "mail.letv.com", help = 'smtp host')
define('smtp_port', default = 25, help = 'smtp port')
define('smtp_user', default = "mcluster", help = 'smtp user')
define('smtp_password', default = "Mcl_20140903!", help = 'smtp password')
define('smtp_from_address', default='mcluster@letv.com', help = 'smtp from address')
define('smtp_duration', default = 10000, type = int, help = 'smtp duration')
define('smtp_tls', default = False, type = bool, help = 'smtp tls')


define("base_dir", default=base_dir, help="project base dir")
define("gbalancer_manager_property",default=join(base_dir, "config","gbalancerManager.property"), help="gbalancer manager config file")


define("alarm_serious", default="tel:sms:email", help="alarm level is serious")
define("alarm_general", default="sms:email", help="alarm level is general")
define("alarm_nothing", default="nothing", help="no alarm")


define("start_gbalancer",default="nohup /usr/bin/gbalancer --config=%s %s >/dev/null 2>&1 &", help="start gbalancer")
define("glb_json_file_name",default="/etc/gbalancer/%sconfiguration.json", help="gbalancer config file")
