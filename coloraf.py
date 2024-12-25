def coloraf(selection="all"):
    """
    AUTHOR
    Christian Balbin

    DESCRIPTION
    Colors structures by pLDDT, automatically detecting if values are in [0,1] or [0,100] range
    Handles multiple objects independently

    USAGE
    coloraf sele

    PARAMETERS
    sele (string)
    The name of the selection/object to color by pLDDT. Default: all
    """
    objects = set(cmd.get_object_list(selection))
    # Process each object separately
    for obj in objects:
        stored.b = []
        cmd.iterate(obj, "stored.b.append(b)")
        max_bfactor = max(stored.b)
        print(f"Object {obj}: Maximum B-factor = {max_bfactor:.3f}")
        if max_bfactor <= 1.0:
            cmd.color("blue", f"({obj}) and b > 0.90")
            cmd.color("cyan", f"({obj}) and b < 0.90 and b > 0.70")
            cmd.color("yellow", f"({obj}) and b < 0.70 and b > 0.50")
            cmd.color("orange", f"({obj}) and b < 0.50")
        else:
            cmd.color("blue", f"({obj}) and b > 90")
            cmd.color("cyan", f"({obj}) and b < 90 and b > 70")
            cmd.color("yellow", f"({obj}) and b < 70 and b > 50")
            cmd.color("orange", f"({obj}) and b < 50")

cmd.extend("coloraf", coloraf)
cmd.auto_arg[0]["coloraf"] = [cmd.object_sc, "object", ""]
