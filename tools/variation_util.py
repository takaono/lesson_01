# -*- coding: utf-8 -*-
from pxr import Usd, UsdGeom, Gf


def add_shadingVariant(usd_path, vset_name, new_variant_name, color):
    stage = Usd.Stage.Open(usd_path)
    root_layer = stage.GetRootLayer()
    model = stage.OverridePrim('/%s' % (root_layer.defaultPrim))
    mesh = stage.OverridePrim('/%s/Geom/%s' % (root_layer.defaultPrim, root_layer.defaultPrim))
    vsets = model.GetVariantSets()
    vset_names = vsets.GetNames()
    for _vset_name in vset_names:
        if vset_name == _vset_name:
            vset = vsets.GetVariantSet(vset_name)
            variant_names = vset.GetVariantNames()
            if new_variant_name in variant_names:
                continue
            vset.AddVariant(new_variant_name)
            vset.SetVariantSelection(new_variant_name)
            with vset.GetVariantEditContext():
                UsdGeom.Gprim(mesh).CreateDisplayColorAttr([color])
    print root_layer.ExportToString()


if __name__ == '__main__':
    stage_root = r""
    usd_geom_path = r"%s/assets/Book/_Book.geom.usda" % stage_root
    vset_name = "shadingVariant"
    new_variant_name = "BookRed"
    add_shadingVariant(usd_geom_path, vset_name, new_variant_name, [1,0,0])
