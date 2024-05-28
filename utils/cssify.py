from six import StringIO
from lesscpy import compile
from os import listdir, path


# Convert LESS to CSS
def cssify(input_path, output_path):
    try:
        with open(input_path, 'r') as less_file:
            less_content = less_file.read()

        css_content = compile(StringIO(less_content), minify=True)

        with open(output_path, 'w') as css_file:
            css_file.write(css_content)

        print(f'Successfully compiled {input_path} to {output_path}')

    except Exception as e:
        print(f'Failed to compile {input_path}: {e}')


def compile_root_less():
    static_directory = 'static'
    compile_less(static_directory)


def compile_module_less(module):
    static_directory = f'apps/{module}/static'
    compile_less(static_directory)


def compile_less(static_directory):
    less_files = listdir(f'{static_directory}/less')

    for file in less_files:
        filename = path.splitext(file)[0]
        cssify(f'{static_directory}/less/{filename}.less', f'{static_directory}/css/{filename}.css')


def create_css():
    # Get a List of All Modular Apps
    app_list = [d for d in listdir('apps') if path.isdir(path.join('apps', d))]
    if '__pycache__' in app_list:
        app_list.remove('__pycache__')

    # Generate Root CSS
    compile_root_less()

    # Compile CSS for Each Modular App
    for app in app_list:
        compile_module_less(app)