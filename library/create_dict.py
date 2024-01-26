#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def parse_file_stats(file_stats):
    file_detail_list = list()

    for i in range(len(file_stats)):
        new_dict = dict()

        print(file_stats[i])
    
    return 0



def main():
    module_args = dict(
        file_stats = dict(type='list', required=True)
    )

    result = dict(
        changed=False,
        discovered_files = ''
    )

    module = AnsibleModule(
        argument_spec = module_args,
        supports_check_mode = True
    )

    if module.check_mode:
        module.exit_json(**result)

    print(type(file_stats))


    result['discovered_files'] = parse_file_stats(file_stats)


    if module.params['new']:
        result['changed'] = True

    if module.params['name'] == 'fail me':
        module.fail_json(msg='You requested this to fail', **result)

    module.exit_json(**result)

if __name__ == '__main__':
    main()