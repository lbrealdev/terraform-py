import os

# version: v1.0.0

ENVS = "environments"
MODULES = "modules"

# Terraform files directories
DEV = "dev"
PRE = "uat"
PROD = "prod"

# Terraform modules directories
BACK = "backend"
CM = "compute"
NET = "networking"

# Files .tf

readme = "README.md"
main_f = "main.tf"
vars_f = "variables.tf"
out_f = "outputs.tf"
ignore = ".gitignore"
# cmd

touch = "copy nul"

path = input("Onde vai ser criado: ")
f_root = str(input("Nome do diretório root: "))

# n_path = (r"C:\Users\lbgoncalves\Documents\structure")
# n_path = ("{C:\\Users\\lbgoncalves\\Documents}\\{}".format(f_root))

n_path = ("{}\\{}".format(path, f_root))

real_path = os.path.realpath(n_path)
f1 = "{}\\{}".format(real_path, ENVS)
f2 = "{}\\{}".format(real_path, MODULES)

def first_action():
    if not os.path.exists(n_path):
        os.makedirs(n_path)
        if os.path.isdir(n_path):
            os.chdir(n_path)
            os.system("{} {}".format(touch, ignore))
            os.system('git init')
            os.system('cls')
        if not os.path.exists(os.path.realpath(f1)): # Create enrironments
            os.makedirs(f1)
            if os.path.isdir(f1):
                os.chdir(f1)
                os.system('mkdir {} {} {}'.format(DEV, PRE, PROD))
            if not os.path.exists(os.path.realpath(f2)): # Create modules
                os.makedirs(f2)
                if os.path.isdir(f2):
                    os.chdir(f2)
                    os.system('mkdir {} {} {}'.format(BACK, CM, NET))


def create_files():
    if os.path.isdir(f1):
        dev_path = os.path.join(f1,"{}".format(DEV))
        os.chdir(dev_path)
        os.system('{a} {main} && {b} {variables} && {c} {outputs} && {d} {read}'.format(a=touch, main=main_f, b=touch, variables=vars_f, c=touch, outputs=out_f, d=touch, read=readme))
        os.system('cls')
        uat_path = os.path.join(f1,"{}".format(PRE))
        if os.path.isdir(uat_path):
            os.chdir(uat_path)
            os.system('{a} {main} && {b} {variables} && {c} {outputs} && {d} {read}'.format(a=touch, main=main_f, b=touch, variables=vars_f, c=touch, outputs=out_f, d=touch, read=readme))
            os.system('cls')
            pro_path = os.path.join(f1,"{}".format(PROD))
            if os.path.isdir(pro_path):
                os.chdir(pro_path)
                os.system('{a} {main} && {b} {variables} && {c} {outputs} && {d} {read}'.format(a=touch, main=main_f, b=touch, variables=vars_f, c=touch, outputs=out_f, d=touch, read=readme))
                os.system('cls')

                if os.path.isdir(f2):
                    backend = os.path.join(f2, "{}".format(BACK))
                    os.chdir(backend)
                    os.system('{a} {main} && {b} {variables} && {c} {outputs} && {d} {read}'.format(a=touch, main=main_f, b=touch, variables=vars_f, c=touch, outputs=out_f, d=touch, read=readme))
                    os.system('cls')
                    cpt = os.path.join(f2, "{}".format(CM))
                    if os.path.isdir(cpt):
                        os.chdir(cpt)
                        os.system('{a} {main} && {b} {variables} && {c} {outputs} && {d} {read}'.format(a=touch, main=main_f, b=touch, variables=vars_f, c=touch, outputs=out_f, d=touch, read=readme))
                        os.system('cls')
                        network = os.path.join(f2, "{}".format(NET))
                        if os.path.isdir(network):
                            os.chdir(network)
                            os.system('{a} {main} && {b} {variables} && {c} {outputs} && {d} {read}'.format(a=touch, main=main_f, b=touch, variables=vars_f, c=touch, outputs=out_f, d=touch, read=readme))
                            os.system('cls')

                            print("Terraform structure created")

                            pass

first_action()
create_files()