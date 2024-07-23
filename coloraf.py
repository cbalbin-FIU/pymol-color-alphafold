from pymol import cmd


def AFcolors(selection="all"):

    """
    AUTHOR
    Christian Balbin 
    
    ADAPTATION
    Nicolas-Frederic Lipp
    
    DESCRIPTION
    Colors Alphafold structures by pLDDT
    An improved version of the original
    Prevent exact values of 90, 70, and 50 from not being recolored.
    Ranges were checked on AFDB to ensure that 90, 70, and 50 match their color scheme, despite the nonsensical model confidence legend available on AFDB website.
    The colors now match exactly AFDB color scheme
    Replace 'coloraf' by 'AFcolors'

    USAGE
    AFcolors sele

    PARAMETERS

    sele (string)
    The name of the selection/object to color by pLDDT. Default: all
    """

    cmd.color("0x0053D6", f"({selection}) and (b > 90 or b = 90)")
    cmd.color("0x64CBF3", f"({selection}) and ((b < 90 and b > 70) or b = 70)")
    cmd.color("0xFFDB13", f"({selection}) and ((b < 70 and b > 50) or b = 50)")
    cmd.color("0xFE7D45", f"({selection}) and b < 50")


cmd.extend("AFcolors", AFcolors)
cmd.auto_arg[0]["AFcolors"] = [cmd.object_sc, "object", ""]
