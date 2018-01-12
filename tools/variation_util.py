# -*- coding: utf-8 -*-
from pxr import Usd, UsdGeom, Gf, Sdf


def add_shadingVariant(input_usd_path, vset_name, new_variant_name, color, output_usd_path):

    stage = Usd.Stage.Open(input_usd_path)

    default_prim = stage.GetDefaultPrim()
    model = stage.OverridePrim(default_prim.GetPath())
    defaullt_vsets = model.GetVariantSets()
    defaullt_vset_names = defaullt_vsets.GetNames()
    
    for prm in stage.Traverse():

        if not UsdGeom.Mesh(prm):
            continue
        
        mesh = stage.OverridePrim(prm.GetPath())
        
        for _vset_name in defaullt_vset_names:
        
            if _vset_name != vset_name:
                continue
        
            vset = model.GetVariantSet(vset_name)
            variant_names = vset.GetVariantNames()
        
            if new_variant_name not in variant_names:
                vset.AppendVariant(new_variant_name) ## vset.AddVariant() <- from v0.8.2
        
            vset.SetVariantSelection(new_variant_name)
        
            with vset.GetVariantEditContext():
                UsdGeom.Gprim(mesh).CreateDisplayColorAttr([color])
    
    root_layer = stage.GetRootLayer()
    root_layer.Export(output_usd_path)


if __name__ == '__main__':
    stage_root = r""
    usd_geom_path = r"%s/assets/Book/_Book.geom.usda" % stage_root
    vset_name = "shadingVariant"
    new_variant_name = "BookRed"
    add_shadingVariant(usd_geom_path, vset_name, new_variant_name, [1,0,0])
