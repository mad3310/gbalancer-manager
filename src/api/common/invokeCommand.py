#!/usr/bin/env python
#-*- coding: utf-8 -*-

import subprocess
import logging
from tornado.options import options

class InvokeCommand():
    
    def _runSysCmd(self,cmdStr):
        if cmdStr == "":
            return ("",0)
        p = subprocess.Popen(cmdStr, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        ret_str = p.stdout.read()
        retval = p.wait()
        return (ret_str,retval)

#     def run_service_mysql_status_script(self):
#         i = 1
#         while i<=200:
#             status_command_result = self._runSysCmd(options.mysql_status_command)
#             if(status_command_result[1] == 0):
#                 status_command_text = status_command_result[0]
#                 logging.info(status_command_text)
#                 target_text = "mcluster-mysqld (pid"
#                 boolean_result = status_command_text.startswith(target_text)
#                 if boolean_result:
#                     break;
#                 
#             i+=1
#         
#         if i==200:    
#             return False
#         
#         return True
    
    def run_check_shell(self, check_shell_path_name):
        check_shell_result = self._runSysCmd(check_shell_path_name)
        result = check_shell_result[0]
        logging.info("check shell: " +  check_shell_path_name + " the result is: " + result)
        return result
