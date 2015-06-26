from .node_bridge import exec_script

def get_dependents(options):
    if 'root' in options:
        args = ['--directory=' + options['root']]

    if 'config' in options:
        args.append('--config=' + options['config'])

    if 'exclude' in options:
        args.append('--exclude=' + options['exclude'])

    if 'filename' in options:
        args.append(options['filename'])

    return exec_script('dependents', 'dependents.js', args).split('\n')
