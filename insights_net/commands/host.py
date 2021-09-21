import click

from insights_net.main import maincli


@maincli.command(name="host")
@click.pass_obj
def host(ctx):
    """
    Show basic host information
    """
    data = ctx.client.evaluate("host_info")
    if not data:
        print("Command not found")
        return

    for archive, host_data in data.items():
        if not host_data:
            continue

        print("Archive: " + archive)
        print("*" * (9 + len(archive)))
        if isinstance(host_data, str):
            print(host_data)
        else:
            print_results(host_data)


def print_results(data):
    print("HostName: {}".format(data.get("hostname")))
    rh_ver = data.get("version")
    print("Red Hat Version:")
    print("  Product: {}".format(rh_ver.get("product")))
    print("  Version: {}".format(rh_ver.get("version")))
    print("  Code Name: {}".format(rh_ver.get("code_name")))

    uname = data.get("uname")
    print("Kernel:")
    print("  Version : {}".format(uname.get("version")))
    print("  Release: {}".format(uname.get("release")))
    print("  Arch: {}".format(uname.get("arch")))

    up = data.get("uptime")
    print("Uptime for {} days {} hh:mm".format(up.get("updays"), up.get("uphhmm")))

    print("Selinux: {}".format(data.get("selinux").get("selinux_status")))
    print("")
