import sys

admin_username = sys.argv[0]
admin_password = sys.argv[1]

if AdminTask.isGlobalSecurityEnabled() != "true":
    AdminTask.applyWizardSettings('[-secureApps true -secureLocalResources false -adminPassword ' + admin_password + ' -userRegistryType WIMUserRegistry -adminName ' + admin_username + ' ]')
    AdminConfig.save()
