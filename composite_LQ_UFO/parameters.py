# This file was automatically created by FeynRules 2.3.27
# Mathematica version: 10.4.1 for Mac OS X x86 (64-bit) (April 11, 2016)
# Date: Tue 5 Jun 2018 20:47:02



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
GS8L1x1 = Parameter(name = 'GS8L1x1',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{GS8L1x1}',
                    lhablock = 'GS8L',
                    lhacode = [ 1, 1 ])

GS8L1x2 = Parameter(name = 'GS8L1x2',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{GS8L1x2}',
                    lhablock = 'GS8L',
                    lhacode = [ 1, 2 ])

GS8L1x3 = Parameter(name = 'GS8L1x3',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{GS8L1x3}',
                    lhablock = 'GS8L',
                    lhacode = [ 1, 3 ])

GS8L2x1 = Parameter(name = 'GS8L2x1',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{GS8L2x1}',
                    lhablock = 'GS8L',
                    lhacode = [ 2, 1 ])

GS8L2x2 = Parameter(name = 'GS8L2x2',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{GS8L2x2}',
                    lhablock = 'GS8L',
                    lhacode = [ 2, 2 ])

GS8L2x3 = Parameter(name = 'GS8L2x3',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{GS8L2x3}',
                    lhablock = 'GS8L',
                    lhacode = [ 2, 3 ])

GS8L3x1 = Parameter(name = 'GS8L3x1',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{GS8L3x1}',
                    lhablock = 'GS8L',
                    lhacode = [ 3, 1 ])

GS8L3x2 = Parameter(name = 'GS8L3x2',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{GS8L3x2}',
                    lhablock = 'GS8L',
                    lhacode = [ 3, 2 ])

GS8L3x3 = Parameter(name = 'GS8L3x3',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{GS8L3x3}',
                    lhablock = 'GS8L',
                    lhacode = [ 3, 3 ])

GS8R1x1 = Parameter(name = 'GS8R1x1',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{GS8R1x1}',
                    lhablock = 'GS8R',
                    lhacode = [ 1, 1 ])

GS8R1x2 = Parameter(name = 'GS8R1x2',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{GS8R1x2}',
                    lhablock = 'GS8R',
                    lhacode = [ 1, 2 ])

GS8R1x3 = Parameter(name = 'GS8R1x3',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{GS8R1x3}',
                    lhablock = 'GS8R',
                    lhacode = [ 1, 3 ])

GS8R2x1 = Parameter(name = 'GS8R2x1',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{GS8R2x1}',
                    lhablock = 'GS8R',
                    lhacode = [ 2, 1 ])

GS8R2x2 = Parameter(name = 'GS8R2x2',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{GS8R2x2}',
                    lhablock = 'GS8R',
                    lhacode = [ 2, 2 ])

GS8R2x3 = Parameter(name = 'GS8R2x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.001,
                    texname = '\\text{GS8R2x3}',
                    lhablock = 'GS8R',
                    lhacode = [ 2, 3 ])

GS8R3x1 = Parameter(name = 'GS8R3x1',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{GS8R3x1}',
                    lhablock = 'GS8R',
                    lhacode = [ 3, 1 ])

GS8R3x2 = Parameter(name = 'GS8R3x2',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{GS8R3x2}',
                    lhablock = 'GS8R',
                    lhacode = [ 3, 2 ])

GS8R3x3 = Parameter(name = 'GS8R3x3',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{GS8R3x3}',
                    lhablock = 'GS8R',
                    lhacode = [ 3, 3 ])

GtS8R1x1 = Parameter(name = 'GtS8R1x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{GtS8R1x1}',
                     lhablock = 'GtS8R',
                     lhacode = [ 1, 1 ])

GtS8R1x2 = Parameter(name = 'GtS8R1x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{GtS8R1x2}',
                     lhablock = 'GtS8R',
                     lhacode = [ 1, 2 ])

GtS8R1x3 = Parameter(name = 'GtS8R1x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{GtS8R1x3}',
                     lhablock = 'GtS8R',
                     lhacode = [ 1, 3 ])

GtS8R2x1 = Parameter(name = 'GtS8R2x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{GtS8R2x1}',
                     lhablock = 'GtS8R',
                     lhacode = [ 2, 1 ])

GtS8R2x2 = Parameter(name = 'GtS8R2x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{GtS8R2x2}',
                     lhablock = 'GtS8R',
                     lhacode = [ 2, 2 ])

GtS8R2x3 = Parameter(name = 'GtS8R2x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{GtS8R2x3}',
                     lhablock = 'GtS8R',
                     lhacode = [ 2, 3 ])

GtS8R3x1 = Parameter(name = 'GtS8R3x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{GtS8R3x1}',
                     lhablock = 'GtS8R',
                     lhacode = [ 3, 1 ])

GtS8R3x2 = Parameter(name = 'GtS8R3x2',
                     nature = 'external',
                     type = 'real',
                     value = 0.001,
                     texname = '\\text{GtS8R3x2}',
                     lhablock = 'GtS8R',
                     lhacode = [ 3, 2 ])

GtS8R3x3 = Parameter(name = 'GtS8R3x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{GtS8R3x3}',
                     lhablock = 'GtS8R',
                     lhacode = [ 3, 3 ])

gNNd1 = Parameter(name = 'gNNd1',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{gNNd1}',
                  lhablock = 'LQCOUPLINGexoNNd',
                  lhacode = [ 1 ])

gNNd2 = Parameter(name = 'gNNd2',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{gNNd2}',
                  lhablock = 'LQCOUPLINGexoNNd',
                  lhacode = [ 2 ])

gNNd3 = Parameter(name = 'gNNd3',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{gNNd3}',
                  lhablock = 'LQCOUPLINGexoNNd',
                  lhacode = [ 3 ])

gNNl1 = Parameter(name = 'gNNl1',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{gNNl1}',
                  lhablock = 'LQCOUPLINGexoNNl',
                  lhacode = [ 1 ])

gNNl2 = Parameter(name = 'gNNl2',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{gNNl2}',
                  lhablock = 'LQCOUPLINGexoNNl',
                  lhacode = [ 2 ])

gNNl3 = Parameter(name = 'gNNl3',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{gNNl3}',
                  lhablock = 'LQCOUPLINGexoNNl',
                  lhacode = [ 3 ])

gNNu1 = Parameter(name = 'gNNu1',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{gNNu1}',
                  lhablock = 'LQCOUPLINGexoNNu',
                  lhacode = [ 1 ])

gNNu2 = Parameter(name = 'gNNu2',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{gNNu2}',
                  lhablock = 'LQCOUPLINGexoNNu',
                  lhacode = [ 2 ])

gNNu3 = Parameter(name = 'gNNu3',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{gNNu3}',
                  lhablock = 'LQCOUPLINGexoNNu',
                  lhacode = [ 3 ])

GS1Nl1x1 = Parameter(name = 'GS1Nl1x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{GS1Nl1x1}',
                     lhablock = 'LQCOUPLINGexoS1L',
                     lhacode = [ 1, 1 ])

GS1Nl1x2 = Parameter(name = 'GS1Nl1x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{GS1Nl1x2}',
                     lhablock = 'LQCOUPLINGexoS1L',
                     lhacode = [ 1, 2 ])

GS1Nl1x3 = Parameter(name = 'GS1Nl1x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{GS1Nl1x3}',
                     lhablock = 'LQCOUPLINGexoS1L',
                     lhacode = [ 1, 3 ])

GS1Nl2x1 = Parameter(name = 'GS1Nl2x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{GS1Nl2x1}',
                     lhablock = 'LQCOUPLINGexoS1L',
                     lhacode = [ 2, 1 ])

GS1Nl2x2 = Parameter(name = 'GS1Nl2x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{GS1Nl2x2}',
                     lhablock = 'LQCOUPLINGexoS1L',
                     lhacode = [ 2, 2 ])

GS1Nl2x3 = Parameter(name = 'GS1Nl2x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{GS1Nl2x3}',
                     lhablock = 'LQCOUPLINGexoS1L',
                     lhacode = [ 2, 3 ])

GS1Nl3x1 = Parameter(name = 'GS1Nl3x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{GS1Nl3x1}',
                     lhablock = 'LQCOUPLINGexoS1L',
                     lhacode = [ 3, 1 ])

GS1Nl3x2 = Parameter(name = 'GS1Nl3x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{GS1Nl3x2}',
                     lhablock = 'LQCOUPLINGexoS1L',
                     lhacode = [ 3, 2 ])

GS1Nl3x3 = Parameter(name = 'GS1Nl3x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{GS1Nl3x3}',
                     lhablock = 'LQCOUPLINGexoS1L',
                     lhacode = [ 3, 3 ])

GS1Nr1x1 = Parameter(name = 'GS1Nr1x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{GS1Nr1x1}',
                     lhablock = 'LQCOUPLINGexoS1R',
                     lhacode = [ 1, 1 ])

GS1Nr1x2 = Parameter(name = 'GS1Nr1x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{GS1Nr1x2}',
                     lhablock = 'LQCOUPLINGexoS1R',
                     lhacode = [ 1, 2 ])

GS1Nr1x3 = Parameter(name = 'GS1Nr1x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{GS1Nr1x3}',
                     lhablock = 'LQCOUPLINGexoS1R',
                     lhacode = [ 1, 3 ])

GS1Nr2x1 = Parameter(name = 'GS1Nr2x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{GS1Nr2x1}',
                     lhablock = 'LQCOUPLINGexoS1R',
                     lhacode = [ 2, 1 ])

GS1Nr2x2 = Parameter(name = 'GS1Nr2x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{GS1Nr2x2}',
                     lhablock = 'LQCOUPLINGexoS1R',
                     lhacode = [ 2, 2 ])

GS1Nr2x3 = Parameter(name = 'GS1Nr2x3',
                     nature = 'external',
                     type = 'real',
                     value = 0.001,
                     texname = '\\text{GS1Nr2x3}',
                     lhablock = 'LQCOUPLINGexoS1R',
                     lhacode = [ 2, 3 ])

GS1Nr3x1 = Parameter(name = 'GS1Nr3x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{GS1Nr3x1}',
                     lhablock = 'LQCOUPLINGexoS1R',
                     lhacode = [ 3, 1 ])

GS1Nr3x2 = Parameter(name = 'GS1Nr3x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{GS1Nr3x2}',
                     lhablock = 'LQCOUPLINGexoS1R',
                     lhacode = [ 3, 2 ])

GS1Nr3x3 = Parameter(name = 'GS1Nr3x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{GS1Nr3x3}',
                     lhablock = 'LQCOUPLINGexoS1R',
                     lhacode = [ 3, 3 ])

GtS1Nr1x1 = Parameter(name = 'GtS1Nr1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{GtS1Nr1x1}',
                      lhablock = 'LQCOUPLINGexotS1R',
                      lhacode = [ 1, 1 ])

GtS1Nr1x2 = Parameter(name = 'GtS1Nr1x2',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{GtS1Nr1x2}',
                      lhablock = 'LQCOUPLINGexotS1R',
                      lhacode = [ 1, 2 ])

GtS1Nr1x3 = Parameter(name = 'GtS1Nr1x3',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{GtS1Nr1x3}',
                      lhablock = 'LQCOUPLINGexotS1R',
                      lhacode = [ 1, 3 ])

GtS1Nr2x1 = Parameter(name = 'GtS1Nr2x1',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{GtS1Nr2x1}',
                      lhablock = 'LQCOUPLINGexotS1R',
                      lhacode = [ 2, 1 ])

GtS1Nr2x2 = Parameter(name = 'GtS1Nr2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{GtS1Nr2x2}',
                      lhablock = 'LQCOUPLINGexotS1R',
                      lhacode = [ 2, 2 ])

GtS1Nr2x3 = Parameter(name = 'GtS1Nr2x3',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{GtS1Nr2x3}',
                      lhablock = 'LQCOUPLINGexotS1R',
                      lhacode = [ 2, 3 ])

GtS1Nr3x1 = Parameter(name = 'GtS1Nr3x1',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{GtS1Nr3x1}',
                      lhablock = 'LQCOUPLINGexotS1R',
                      lhacode = [ 3, 1 ])

GtS1Nr3x2 = Parameter(name = 'GtS1Nr3x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.001,
                      texname = '\\text{GtS1Nr3x2}',
                      lhablock = 'LQCOUPLINGexotS1R',
                      lhacode = [ 3, 2 ])

GtS1Nr3x3 = Parameter(name = 'GtS1Nr3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{GtS1Nr3x3}',
                      lhablock = 'LQCOUPLINGexotS1R',
                      lhacode = [ 3, 3 ])

g1L1x1 = Parameter(name = 'g1L1x1',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{g1L1x1}',
                   lhablock = 'LQCOUPLINGS1L',
                   lhacode = [ 1, 1 ])

g1L1x2 = Parameter(name = 'g1L1x2',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{g1L1x2}',
                   lhablock = 'LQCOUPLINGS1L',
                   lhacode = [ 1, 2 ])

g1L1x3 = Parameter(name = 'g1L1x3',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{g1L1x3}',
                   lhablock = 'LQCOUPLINGS1L',
                   lhacode = [ 1, 3 ])

g1L2x1 = Parameter(name = 'g1L2x1',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{g1L2x1}',
                   lhablock = 'LQCOUPLINGS1L',
                   lhacode = [ 2, 1 ])

g1L2x2 = Parameter(name = 'g1L2x2',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{g1L2x2}',
                   lhablock = 'LQCOUPLINGS1L',
                   lhacode = [ 2, 2 ])

g1L2x3 = Parameter(name = 'g1L2x3',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{g1L2x3}',
                   lhablock = 'LQCOUPLINGS1L',
                   lhacode = [ 2, 3 ])

g1L3x1 = Parameter(name = 'g1L3x1',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{g1L3x1}',
                   lhablock = 'LQCOUPLINGS1L',
                   lhacode = [ 3, 1 ])

g1L3x2 = Parameter(name = 'g1L3x2',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{g1L3x2}',
                   lhablock = 'LQCOUPLINGS1L',
                   lhacode = [ 3, 2 ])

g1L3x3 = Parameter(name = 'g1L3x3',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{g1L3x3}',
                   lhablock = 'LQCOUPLINGS1L',
                   lhacode = [ 3, 3 ])

g1R1x1 = Parameter(name = 'g1R1x1',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{g1R1x1}',
                   lhablock = 'LQCOUPLINGS1R',
                   lhacode = [ 1, 1 ])

g1R1x2 = Parameter(name = 'g1R1x2',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{g1R1x2}',
                   lhablock = 'LQCOUPLINGS1R',
                   lhacode = [ 1, 2 ])

g1R1x3 = Parameter(name = 'g1R1x3',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{g1R1x3}',
                   lhablock = 'LQCOUPLINGS1R',
                   lhacode = [ 1, 3 ])

g1R2x1 = Parameter(name = 'g1R2x1',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{g1R2x1}',
                   lhablock = 'LQCOUPLINGS1R',
                   lhacode = [ 2, 1 ])

g1R2x2 = Parameter(name = 'g1R2x2',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{g1R2x2}',
                   lhablock = 'LQCOUPLINGS1R',
                   lhacode = [ 2, 2 ])

g1R2x3 = Parameter(name = 'g1R2x3',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{g1R2x3}',
                   lhablock = 'LQCOUPLINGS1R',
                   lhacode = [ 2, 3 ])

g1R3x1 = Parameter(name = 'g1R3x1',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{g1R3x1}',
                   lhablock = 'LQCOUPLINGS1R',
                   lhacode = [ 3, 1 ])

g1R3x2 = Parameter(name = 'g1R3x2',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{g1R3x2}',
                   lhablock = 'LQCOUPLINGS1R',
                   lhacode = [ 3, 2 ])

g1R3x3 = Parameter(name = 'g1R3x3',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{g1R3x3}',
                   lhablock = 'LQCOUPLINGS1R',
                   lhacode = [ 3, 3 ])

gt1R1x1 = Parameter(name = 'gt1R1x1',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{gt1R1x1}',
                    lhablock = 'LQCOUPLINGtS1R',
                    lhacode = [ 1, 1 ])

gt1R1x2 = Parameter(name = 'gt1R1x2',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{gt1R1x2}',
                    lhablock = 'LQCOUPLINGtS1R',
                    lhacode = [ 1, 2 ])

gt1R1x3 = Parameter(name = 'gt1R1x3',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{gt1R1x3}',
                    lhablock = 'LQCOUPLINGtS1R',
                    lhacode = [ 1, 3 ])

gt1R2x1 = Parameter(name = 'gt1R2x1',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{gt1R2x1}',
                    lhablock = 'LQCOUPLINGtS1R',
                    lhacode = [ 2, 1 ])

gt1R2x2 = Parameter(name = 'gt1R2x2',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{gt1R2x2}',
                    lhablock = 'LQCOUPLINGtS1R',
                    lhacode = [ 2, 2 ])

gt1R2x3 = Parameter(name = 'gt1R2x3',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{gt1R2x3}',
                    lhablock = 'LQCOUPLINGtS1R',
                    lhacode = [ 2, 3 ])

gt1R3x1 = Parameter(name = 'gt1R3x1',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{gt1R3x1}',
                    lhablock = 'LQCOUPLINGtS1R',
                    lhacode = [ 3, 1 ])

gt1R3x2 = Parameter(name = 'gt1R3x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{gt1R3x2}',
                    lhablock = 'LQCOUPLINGtS1R',
                    lhacode = [ 3, 2 ])

gt1R3x3 = Parameter(name = 'gt1R3x3',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{gt1R3x3}',
                    lhablock = 'LQCOUPLINGtS1R',
                    lhacode = [ 3, 3 ])

mu6 = Parameter(name = 'mu6',
                nature = 'external',
                type = 'real',
                value = 1000,
                texname = '\\text{mu6}',
                lhablock = 'MU6',
                lhacode = [ 1 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

tmu6 = Parameter(name = 'tmu6',
                 nature = 'external',
                 type = 'real',
                 value = 1000,
                 texname = '\\text{tmu6}',
                 lhablock = 'FRBlock',
                 lhacode = [ 1 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

MSIX = Parameter(name = 'MSIX',
                 nature = 'external',
                 type = 'real',
                 value = 1500,
                 texname = '\\text{MSIX}',
                 lhablock = 'MASS',
                 lhacode = [ 9000060 ])

MTISX = Parameter(name = 'MTISX',
                  nature = 'external',
                  type = 'real',
                  value = 1500,
                  texname = '\\text{MTISX}',
                  lhablock = 'MASS',
                  lhacode = [ 9000061 ])

MOCT = Parameter(name = 'MOCT',
                 nature = 'external',
                 type = 'real',
                 value = 1500,
                 texname = '\\text{MOCT}',
                 lhablock = 'MASS',
                 lhacode = [ 9000080 ])

MS1 = Parameter(name = 'MS1',
                nature = 'external',
                type = 'real',
                value = 600,
                texname = '\\text{MS1}',
                lhablock = 'MASS',
                lhacode = [ 9000010 ])

MtS1 = Parameter(name = 'MtS1',
                 nature = 'external',
                 type = 'real',
                 value = 600,
                 texname = '\\text{MtS1}',
                 lhablock = 'MASS',
                 lhacode = [ 9000011 ])

MNN = Parameter(name = 'MNN',
                nature = 'external',
                type = 'real',
                value = 100,
                texname = '\\text{MNN}',
                lhablock = 'MASS',
                lhacode = [ 9000050 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

WSIX = Parameter(name = 'WSIX',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{WSIX}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000060 ])

WTSIX = Parameter(name = 'WTSIX',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{WTSIX}',
                  lhablock = 'DECAY',
                  lhacode = [ 9000061 ])

WOCT = Parameter(name = 'WOCT',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{WOCT}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000080 ])

WS1 = Parameter(name = 'WS1',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{WS1}',
                lhablock = 'DECAY',
                lhacode = [ 9000010 ])

WtS1 = Parameter(name = 'WtS1',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{WtS1}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000011 ])

WNN = Parameter(name = 'WNN',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{WNN}',
                lhablock = 'DECAY',
                lhacode = [ 9000050 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

I1a33 = Parameter(name = 'I1a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb',
                  texname = '\\text{I1a33}')

I10a11 = Parameter(name = 'I10a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'GS8L1x1',
                   texname = '\\text{I10a11}')

I10a12 = Parameter(name = 'I10a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'GS8L1x2',
                   texname = '\\text{I10a12}')

I10a13 = Parameter(name = 'I10a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'GS8L1x3',
                   texname = '\\text{I10a13}')

I10a21 = Parameter(name = 'I10a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'GS8L2x1',
                   texname = '\\text{I10a21}')

I10a22 = Parameter(name = 'I10a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'GS8L2x2',
                   texname = '\\text{I10a22}')

I10a23 = Parameter(name = 'I10a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'GS8L2x3',
                   texname = '\\text{I10a23}')

I10a31 = Parameter(name = 'I10a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'GS8L3x1',
                   texname = '\\text{I10a31}')

I10a32 = Parameter(name = 'I10a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'GS8L3x2',
                   texname = '\\text{I10a32}')

I10a33 = Parameter(name = 'I10a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'GS8L3x3',
                   texname = '\\text{I10a33}')

I2a33 = Parameter(name = 'I2a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt',
                  texname = '\\text{I2a33}')

I3a33 = Parameter(name = 'I3a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt',
                  texname = '\\text{I3a33}')

I4a33 = Parameter(name = 'I4a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb',
                  texname = '\\text{I4a33}')

I5a11 = Parameter(name = 'I5a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'g1L1x1',
                  texname = '\\text{I5a11}')

I5a12 = Parameter(name = 'I5a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'g1L1x2',
                  texname = '\\text{I5a12}')

I5a13 = Parameter(name = 'I5a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'g1L1x3',
                  texname = '\\text{I5a13}')

I5a21 = Parameter(name = 'I5a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'g1L2x1',
                  texname = '\\text{I5a21}')

I5a22 = Parameter(name = 'I5a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'g1L2x2',
                  texname = '\\text{I5a22}')

I5a23 = Parameter(name = 'I5a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'g1L2x3',
                  texname = '\\text{I5a23}')

I5a31 = Parameter(name = 'I5a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'g1L3x1',
                  texname = '\\text{I5a31}')

I5a32 = Parameter(name = 'I5a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'g1L3x2',
                  texname = '\\text{I5a32}')

I5a33 = Parameter(name = 'I5a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'g1L3x3',
                  texname = '\\text{I5a33}')

I6a11 = Parameter(name = 'I6a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'GS1Nl1x1',
                  texname = '\\text{I6a11}')

I6a12 = Parameter(name = 'I6a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'GS1Nl1x2',
                  texname = '\\text{I6a12}')

I6a13 = Parameter(name = 'I6a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'GS1Nl1x3',
                  texname = '\\text{I6a13}')

I6a21 = Parameter(name = 'I6a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'GS1Nl2x1',
                  texname = '\\text{I6a21}')

I6a22 = Parameter(name = 'I6a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'GS1Nl2x2',
                  texname = '\\text{I6a22}')

I6a23 = Parameter(name = 'I6a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'GS1Nl2x3',
                  texname = '\\text{I6a23}')

I6a31 = Parameter(name = 'I6a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'GS1Nl3x1',
                  texname = '\\text{I6a31}')

I6a32 = Parameter(name = 'I6a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'GS1Nl3x2',
                  texname = '\\text{I6a32}')

I6a33 = Parameter(name = 'I6a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'GS1Nl3x3',
                  texname = '\\text{I6a33}')

I7a11 = Parameter(name = 'I7a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'g1L1x1',
                  texname = '\\text{I7a11}')

I7a12 = Parameter(name = 'I7a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'g1L1x2',
                  texname = '\\text{I7a12}')

I7a13 = Parameter(name = 'I7a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'g1L1x3',
                  texname = '\\text{I7a13}')

I7a21 = Parameter(name = 'I7a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'g1L2x1',
                  texname = '\\text{I7a21}')

I7a22 = Parameter(name = 'I7a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'g1L2x2',
                  texname = '\\text{I7a22}')

I7a23 = Parameter(name = 'I7a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'g1L2x3',
                  texname = '\\text{I7a23}')

I7a31 = Parameter(name = 'I7a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'g1L3x1',
                  texname = '\\text{I7a31}')

I7a32 = Parameter(name = 'I7a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'g1L3x2',
                  texname = '\\text{I7a32}')

I7a33 = Parameter(name = 'I7a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'g1L3x3',
                  texname = '\\text{I7a33}')

I8a11 = Parameter(name = 'I8a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'GS1Nl1x1',
                  texname = '\\text{I8a11}')

I8a12 = Parameter(name = 'I8a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'GS1Nl1x2',
                  texname = '\\text{I8a12}')

I8a13 = Parameter(name = 'I8a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'GS1Nl1x3',
                  texname = '\\text{I8a13}')

I8a21 = Parameter(name = 'I8a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'GS1Nl2x1',
                  texname = '\\text{I8a21}')

I8a22 = Parameter(name = 'I8a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'GS1Nl2x2',
                  texname = '\\text{I8a22}')

I8a23 = Parameter(name = 'I8a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'GS1Nl2x3',
                  texname = '\\text{I8a23}')

I8a31 = Parameter(name = 'I8a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'GS1Nl3x1',
                  texname = '\\text{I8a31}')

I8a32 = Parameter(name = 'I8a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'GS1Nl3x2',
                  texname = '\\text{I8a32}')

I8a33 = Parameter(name = 'I8a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'GS1Nl3x3',
                  texname = '\\text{I8a33}')

I9a11 = Parameter(name = 'I9a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'GS8L1x1',
                  texname = '\\text{I9a11}')

I9a12 = Parameter(name = 'I9a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'GS8L1x2',
                  texname = '\\text{I9a12}')

I9a13 = Parameter(name = 'I9a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'GS8L1x3',
                  texname = '\\text{I9a13}')

I9a21 = Parameter(name = 'I9a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'GS8L2x1',
                  texname = '\\text{I9a21}')

I9a22 = Parameter(name = 'I9a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'GS8L2x2',
                  texname = '\\text{I9a22}')

I9a23 = Parameter(name = 'I9a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'GS8L2x3',
                  texname = '\\text{I9a23}')

I9a31 = Parameter(name = 'I9a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'GS8L3x1',
                  texname = '\\text{I9a31}')

I9a32 = Parameter(name = 'I9a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'GS8L3x2',
                  texname = '\\text{I9a32}')

I9a33 = Parameter(name = 'I9a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'GS8L3x3',
                  texname = '\\text{I9a33}')

