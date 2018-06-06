# This file was automatically created by FeynRules 2.3.27
# Mathematica version: 10.4.1 for Mac OS X x86 (64-bit) (April 11, 2016)
# Date: Tue 5 Jun 2018 20:47:02


from object_library import all_decays, Decay
import particles as P


Decay_b = Decay(name = 'Decay_b',
                particle = P.b,
                partial_widths = {(P.S1b,P.ve__tilde__):'((MB**2 - MS1**2)*(3*I7a31*MB**2*complexconjugate(I7a31) - 3*I7a31*MS1**2*complexconjugate(I7a31)))/(96.*cmath.pi*abs(MB)**3)',
                                  (P.S1b,P.vm__tilde__):'((MB**2 - MS1**2)*(3*I7a32*MB**2*complexconjugate(I7a32) - 3*I7a32*MS1**2*complexconjugate(I7a32)))/(96.*cmath.pi*abs(MB)**3)',
                                  (P.S1b,P.vt__tilde__):'((MB**2 - MS1**2)*(3*I7a33*MB**2*complexconjugate(I7a33) - 3*I7a33*MS1**2*complexconjugate(I7a33)))/(96.*cmath.pi*abs(MB)**3)',
                                  (P.tS1b,P.e__plus__):'((MB**2 - MtS1**2)*(3*gt1R3x1**2*MB**2 - 3*gt1R3x1**2*MtS1**2))/(96.*cmath.pi*abs(MB)**3)',
                                  (P.tS1b,P.mu__plus__):'((MB**2 - MtS1**2)*(3*gt1R3x2**2*MB**2 - 3*gt1R3x2**2*MtS1**2))/(96.*cmath.pi*abs(MB)**3)',
                                  (P.tS1b,P.ta__plus__):'((3*gt1R3x3**2*MB**2 + 3*gt1R3x3**2*MTA**2 - 3*gt1R3x3**2*MtS1**2)*cmath.sqrt(MB**4 - 2*MB**2*MTA**2 + MTA**4 - 2*MB**2*MtS1**2 - 2*MTA**2*MtS1**2 + MtS1**4))/(96.*cmath.pi*abs(MB)**3)',
                                  (P.W__minus__,P.t):'(((3*ee**2*MB**2)/(2.*sw**2) + (3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MB**4)/(2.*MW**2*sw**2) - (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MB)**3)'})

Decay_H = Decay(name = 'Decay_H',
                particle = P.H,
                partial_widths = {(P.b,P.b__tilde__):'((-12*MB**2*yb**2 + 3*MH**2*yb**2)*cmath.sqrt(-4*MB**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.t,P.t__tilde__):'((3*MH**2*yt**2 - 12*MT**2*yt**2)*cmath.sqrt(MH**4 - 4*MH**2*MT**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((MH**2*ytau**2 - 4*MTA**2*ytau**2)*cmath.sqrt(MH**4 - 4*MH**2*MTA**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.W__minus__,P.W__plus__):'(((3*ee**4*vev**2)/(4.*sw**4) + (ee**4*MH**4*vev**2)/(16.*MW**4*sw**4) - (ee**4*MH**2*vev**2)/(4.*MW**2*sw**4))*cmath.sqrt(MH**4 - 4*MH**2*MW**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.Z,P.Z):'(((9*ee**4*vev**2)/2. + (3*ee**4*MH**4*vev**2)/(8.*MZ**4) - (3*ee**4*MH**2*vev**2)/(2.*MZ**2) + (3*cw**4*ee**4*vev**2)/(4.*sw**4) + (cw**4*ee**4*MH**4*vev**2)/(16.*MZ**4*sw**4) - (cw**4*ee**4*MH**2*vev**2)/(4.*MZ**2*sw**4) + (3*cw**2*ee**4*vev**2)/sw**2 + (cw**2*ee**4*MH**4*vev**2)/(4.*MZ**4*sw**2) - (cw**2*ee**4*MH**2*vev**2)/(MZ**2*sw**2) + (3*ee**4*sw**2*vev**2)/cw**2 + (ee**4*MH**4*sw**2*vev**2)/(4.*cw**2*MZ**4) - (ee**4*MH**2*sw**2*vev**2)/(cw**2*MZ**2) + (3*ee**4*sw**4*vev**2)/(4.*cw**4) + (ee**4*MH**4*sw**4*vev**2)/(16.*cw**4*MZ**4) - (ee**4*MH**2*sw**4*vev**2)/(4.*cw**4*MZ**2))*cmath.sqrt(MH**4 - 4*MH**2*MZ**2))/(32.*cmath.pi*abs(MH)**3)'})

Decay_NN = Decay(name = 'Decay_NN',
                 particle = P.NN,
                 partial_widths = {(P.b,P.b__tilde__):'((-24*gNNd3**2*MB**2 + 6*gNNd3**2*MNN**2)*cmath.sqrt(-4*MB**2*MNN**2 + MNN**4))/(16.*cmath.pi*abs(MNN)**3)',
                                   (P.c,P.c__tilde__):'(3*gNNu2**2*MNN**4)/(8.*cmath.pi*abs(MNN)**3)',
                                   (P.d,P.d__tilde__):'(3*gNNd1**2*MNN**4)/(8.*cmath.pi*abs(MNN)**3)',
                                   (P.e__minus__,P.e__plus__):'(gNNl1**2*MNN**4)/(8.*cmath.pi*abs(MNN)**3)',
                                   (P.mu__minus__,P.mu__plus__):'(gNNl2**2*MNN**4)/(8.*cmath.pi*abs(MNN)**3)',
                                   (P.s,P.s__tilde__):'(3*gNNd2**2*MNN**4)/(8.*cmath.pi*abs(MNN)**3)',
                                   (P.t,P.t__tilde__):'((6*gNNu3**2*MNN**2 - 24*gNNu3**2*MT**2)*cmath.sqrt(MNN**4 - 4*MNN**2*MT**2))/(16.*cmath.pi*abs(MNN)**3)',
                                   (P.ta__minus__,P.ta__plus__):'((2*gNNl3**2*MNN**2 - 8*gNNl3**2*MTA**2)*cmath.sqrt(MNN**4 - 4*MNN**2*MTA**2))/(16.*cmath.pi*abs(MNN)**3)',
                                   (P.u,P.u__tilde__):'(3*gNNu1**2*MNN**4)/(8.*cmath.pi*abs(MNN)**3)'})

Decay_S1b = Decay(name = 'Decay_S1b',
                  particle = P.S1b,
                  partial_widths = {(P.b,P.ve):'((-MB**2 + MS1**2)*(-3*I5a31*MB**2*complexconjugate(I5a31) + 3*I5a31*MS1**2*complexconjugate(I5a31)))/(48.*cmath.pi*abs(MS1)**3)',
                                    (P.b,P.vm):'((-MB**2 + MS1**2)*(-3*I5a32*MB**2*complexconjugate(I5a32) + 3*I5a32*MS1**2*complexconjugate(I5a32)))/(48.*cmath.pi*abs(MS1)**3)',
                                    (P.b,P.vt):'((-MB**2 + MS1**2)*(-3*I5a33*MB**2*complexconjugate(I5a33) + 3*I5a33*MS1**2*complexconjugate(I5a33)))/(48.*cmath.pi*abs(MS1)**3)',
                                    (P.d,P.ve):'(I5a11*MS1**4*complexconjugate(I5a11))/(16.*cmath.pi*abs(MS1)**3)',
                                    (P.d,P.vm):'(I5a12*MS1**4*complexconjugate(I5a12))/(16.*cmath.pi*abs(MS1)**3)',
                                    (P.d,P.vt):'(I5a13*MS1**4*complexconjugate(I5a13))/(16.*cmath.pi*abs(MS1)**3)',
                                    (P.e__minus__,P.c):'(MS1**2*(3*g1L2x1**2*MS1**2 + 3*g1R2x1**2*MS1**2))/(48.*cmath.pi*abs(MS1)**3)',
                                    (P.e__minus__,P.t):'((MS1**2 - MT**2)*(3*g1L3x1**2*MS1**2 + 3*g1R3x1**2*MS1**2 - 3*g1L3x1**2*MT**2 - 3*g1R3x1**2*MT**2))/(48.*cmath.pi*abs(MS1)**3)',
                                    (P.e__minus__,P.u):'(MS1**2*(3*g1L1x1**2*MS1**2 + 3*g1R1x1**2*MS1**2))/(48.*cmath.pi*abs(MS1)**3)',
                                    (P.mu__minus__,P.c):'(MS1**2*(3*g1L2x2**2*MS1**2 + 3*g1R2x2**2*MS1**2))/(48.*cmath.pi*abs(MS1)**3)',
                                    (P.mu__minus__,P.t):'((MS1**2 - MT**2)*(3*g1L3x2**2*MS1**2 + 3*g1R3x2**2*MS1**2 - 3*g1L3x2**2*MT**2 - 3*g1R3x2**2*MT**2))/(48.*cmath.pi*abs(MS1)**3)',
                                    (P.mu__minus__,P.u):'(MS1**2*(3*g1L1x2**2*MS1**2 + 3*g1R1x2**2*MS1**2))/(48.*cmath.pi*abs(MS1)**3)',
                                    (P.s,P.ve):'(I5a21*MS1**4*complexconjugate(I5a21))/(16.*cmath.pi*abs(MS1)**3)',
                                    (P.s,P.vm):'(I5a22*MS1**4*complexconjugate(I5a22))/(16.*cmath.pi*abs(MS1)**3)',
                                    (P.s,P.vt):'(I5a23*MS1**4*complexconjugate(I5a23))/(16.*cmath.pi*abs(MS1)**3)',
                                    (P.ta__minus__,P.c):'((MS1**2 - MTA**2)*(3*g1L2x3**2*MS1**2 + 3*g1R2x3**2*MS1**2 - 3*g1L2x3**2*MTA**2 - 3*g1R2x3**2*MTA**2))/(48.*cmath.pi*abs(MS1)**3)',
                                    (P.ta__minus__,P.t):'((3*g1L3x3**2*MS1**2 + 3*g1R3x3**2*MS1**2 - 3*g1L3x3**2*MT**2 - 3*g1R3x3**2*MT**2 - 12*g1L3x3*g1R3x3*MT*MTA - 3*g1L3x3**2*MTA**2 - 3*g1R3x3**2*MTA**2)*cmath.sqrt(MS1**4 - 2*MS1**2*MT**2 + MT**4 - 2*MS1**2*MTA**2 - 2*MT**2*MTA**2 + MTA**4))/(48.*cmath.pi*abs(MS1)**3)',
                                    (P.ta__minus__,P.u):'((MS1**2 - MTA**2)*(3*g1L1x3**2*MS1**2 + 3*g1R1x3**2*MS1**2 - 3*g1L1x3**2*MTA**2 - 3*g1R1x3**2*MTA**2))/(48.*cmath.pi*abs(MS1)**3)'})

Decay_six = Decay(name = 'Decay_six',
                  particle = P.six,
                  partial_widths = {(P.S1b,P.S1b):'(mu6**2*cmath.sqrt(-4*MS1**2*MSIX**2 + MSIX**4))/(8.*cmath.pi*abs(MSIX)**3)'})

Decay_t = Decay(name = 'Decay_t',
                particle = P.t,
                partial_widths = {(P.S1b,P.e__plus__):'((-MS1**2 + MT**2)*(-3*g1L3x1**2*MS1**2 - 3*g1R3x1**2*MS1**2 + 3*g1L3x1**2*MT**2 + 3*g1R3x1**2*MT**2))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.S1b,P.mu__plus__):'((-MS1**2 + MT**2)*(-3*g1L3x2**2*MS1**2 - 3*g1R3x2**2*MS1**2 + 3*g1L3x2**2*MT**2 + 3*g1R3x2**2*MT**2))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.S1b,P.ta__plus__):'((-3*g1L3x3**2*MS1**2 - 3*g1R3x3**2*MS1**2 + 3*g1L3x3**2*MT**2 + 3*g1R3x3**2*MT**2 + 12*g1L3x3*g1R3x3*MT*MTA + 3*g1L3x3**2*MTA**2 + 3*g1R3x3**2*MTA**2)*cmath.sqrt(MS1**4 - 2*MS1**2*MT**2 + MT**4 - 2*MS1**2*MTA**2 - 2*MT**2*MTA**2 + MTA**4))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.W__plus__,P.b):'(((3*ee**2*MB**2)/(2.*sw**2) + (3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MB**4)/(2.*MW**2*sw**2) - (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MT)**3)'})

Decay_ta__minus__ = Decay(name = 'Decay_ta__minus__',
                          particle = P.ta__minus__,
                          partial_widths = {(P.S1b,P.c__tilde__):'((-MS1**2 + MTA**2)*(-3*g1L2x3**2*MS1**2 - 3*g1R2x3**2*MS1**2 + 3*g1L2x3**2*MTA**2 + 3*g1R2x3**2*MTA**2))/(32.*cmath.pi*abs(MTA)**3)',
                                            (P.S1b,P.t__tilde__):'((-3*g1L3x3**2*MS1**2 - 3*g1R3x3**2*MS1**2 + 3*g1L3x3**2*MT**2 + 3*g1R3x3**2*MT**2 + 12*g1L3x3*g1R3x3*MT*MTA + 3*g1L3x3**2*MTA**2 + 3*g1R3x3**2*MTA**2)*cmath.sqrt(MS1**4 - 2*MS1**2*MT**2 + MT**4 - 2*MS1**2*MTA**2 - 2*MT**2*MTA**2 + MTA**4))/(32.*cmath.pi*abs(MTA)**3)',
                                            (P.S1b,P.u__tilde__):'((-MS1**2 + MTA**2)*(-3*g1L1x3**2*MS1**2 - 3*g1R1x3**2*MS1**2 + 3*g1L1x3**2*MTA**2 + 3*g1R1x3**2*MTA**2))/(32.*cmath.pi*abs(MTA)**3)',
                                            (P.tS1b,P.b__tilde__):'((3*gt1R3x3**2*MB**2 + 3*gt1R3x3**2*MTA**2 - 3*gt1R3x3**2*MtS1**2)*cmath.sqrt(MB**4 - 2*MB**2*MTA**2 + MTA**4 - 2*MB**2*MtS1**2 - 2*MTA**2*MtS1**2 + MtS1**4))/(32.*cmath.pi*abs(MTA)**3)',
                                            (P.tS1b,P.d__tilde__):'((MTA**2 - MtS1**2)*(3*gt1R1x3**2*MTA**2 - 3*gt1R1x3**2*MtS1**2))/(32.*cmath.pi*abs(MTA)**3)',
                                            (P.tS1b,P.s__tilde__):'((MTA**2 - MtS1**2)*(3*gt1R2x3**2*MTA**2 - 3*gt1R2x3**2*MtS1**2))/(32.*cmath.pi*abs(MTA)**3)',
                                            (P.W__minus__,P.vt):'((MTA**2 - MW**2)*((ee**2*MTA**2)/(2.*sw**2) + (ee**2*MTA**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(MTA)**3)'})

Decay_tS1b = Decay(name = 'Decay_tS1b',
                   particle = P.tS1b,
                   partial_widths = {(P.b,P.e__minus__):'((-MB**2 + MtS1**2)*(-3*gt1R3x1**2*MB**2 + 3*gt1R3x1**2*MtS1**2))/(48.*cmath.pi*abs(MtS1)**3)',
                                     (P.b,P.mu__minus__):'((-MB**2 + MtS1**2)*(-3*gt1R3x2**2*MB**2 + 3*gt1R3x2**2*MtS1**2))/(48.*cmath.pi*abs(MtS1)**3)',
                                     (P.b,P.ta__minus__):'((-3*gt1R3x3**2*MB**2 - 3*gt1R3x3**2*MTA**2 + 3*gt1R3x3**2*MtS1**2)*cmath.sqrt(MB**4 - 2*MB**2*MTA**2 + MTA**4 - 2*MB**2*MtS1**2 - 2*MTA**2*MtS1**2 + MtS1**4))/(48.*cmath.pi*abs(MtS1)**3)',
                                     (P.d,P.e__minus__):'(gt1R1x1**2*MtS1**4)/(16.*cmath.pi*abs(MtS1)**3)',
                                     (P.d,P.mu__minus__):'(gt1R1x2**2*MtS1**4)/(16.*cmath.pi*abs(MtS1)**3)',
                                     (P.d,P.ta__minus__):'((-MTA**2 + MtS1**2)*(-3*gt1R1x3**2*MTA**2 + 3*gt1R1x3**2*MtS1**2))/(48.*cmath.pi*abs(MtS1)**3)',
                                     (P.s,P.e__minus__):'(gt1R2x1**2*MtS1**4)/(16.*cmath.pi*abs(MtS1)**3)',
                                     (P.s,P.mu__minus__):'(gt1R2x2**2*MtS1**4)/(16.*cmath.pi*abs(MtS1)**3)',
                                     (P.s,P.ta__minus__):'((-MTA**2 + MtS1**2)*(-3*gt1R2x3**2*MTA**2 + 3*gt1R2x3**2*MtS1**2))/(48.*cmath.pi*abs(MtS1)**3)'})

Decay_tsix = Decay(name = 'Decay_tsix',
                   particle = P.tsix,
                   partial_widths = {(P.tS1b,P.tS1b):'(tmu6**2*cmath.sqrt(MTISX**4 - 4*MTISX**2*MtS1**2))/(8.*cmath.pi*abs(MTISX)**3)'})

Decay_W__plus__ = Decay(name = 'Decay_W__plus__',
                        particle = P.W__plus__,
                        partial_widths = {(P.c,P.s__tilde__):'(ee**2*MW**4)/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.t,P.b__tilde__):'(((-3*ee**2*MB**2)/(2.*sw**2) - (3*ee**2*MT**2)/(2.*sw**2) - (3*ee**2*MB**4)/(2.*MW**2*sw**2) + (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) - (3*ee**2*MT**4)/(2.*MW**2*sw**2) + (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.u,P.d__tilde__):'(ee**2*MW**4)/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.ve,P.e__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vm,P.mu__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vt,P.ta__plus__):'((-MTA**2 + MW**2)*(-(ee**2*MTA**2)/(2.*sw**2) - (ee**2*MTA**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)'})

Decay_Z = Decay(name = 'Decay_Z',
                particle = P.Z,
                partial_widths = {(P.b,P.b__tilde__):'((-7*ee**2*MB**2 + ee**2*MZ**2 - (3*cw**2*ee**2*MB**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) - (17*ee**2*MB**2*sw**2)/(6.*cw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MB**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.c,P.c__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.d,P.d__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.e__minus__,P.e__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.mu__minus__,P.mu__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.s,P.s__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.t,P.t__tilde__):'((-11*ee**2*MT**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MT**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MT**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MT**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((-5*ee**2*MTA**2 - ee**2*MZ**2 - (cw**2*ee**2*MTA**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MTA**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*MTA**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.u,P.u__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ve,P.ve__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vm,P.vm__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vt,P.vt__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.W__minus__,P.W__plus__):'(((-12*cw**2*ee**2*MW**2)/sw**2 - (17*cw**2*ee**2*MZ**2)/sw**2 + (4*cw**2*ee**2*MZ**4)/(MW**2*sw**2) + (cw**2*ee**2*MZ**6)/(4.*MW**4*sw**2))*cmath.sqrt(-4*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)'})

