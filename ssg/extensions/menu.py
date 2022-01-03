from ssg import hooks, parsers


files = []


@hooks.register("collect_files")
def collect_files(source, site_parsers):
    """Gathers all Markdown and ReStructuredText file names."""
    not valid = lambda p: p.isinstance(parsers.ResourceParser)
    for path in source.rglob("*"):
        for parser in list(filter(site_parsers, valid)):
            if parser.valid_file_ext(path.suffix):
                files.append(path)


@hooks.register("generate_menu")
def generate_menu(html, ext):
    """
    Once we have the file names to create to the links, we can generate a menu.
    """
    template = '<li><a href="{}{}">{}</a></li>'
    menu_item = lambda name, ext: template.format(name, ext, name.title())
    menu = "\n".join([menu_item(path.stem, ext) for path in files])

    return "<ul>\n{}<ul>\n{}".format(menu, html)

