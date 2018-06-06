# Composite LeptoQuark UFO model files
This is a repository for the leptoquark model explored in [arXiv:1803.05962](http://arxiv.org/abs/arXiv:1803.05962) by A.Monteux and A.Rajaraman. Please cite the paper if you use this UFO or find this useful.

The UFO file was generated with [FeynRules](http://feynrules.irmp.ucl.ac.be/).

Examples on how to generate events with Madgraph are provided below.

## The model
In this model we introduce composite scalar leptoquarks $S\_1$ and $\tilde{S}\_1$ (in the notation of [Buchmüller, Ruckl, Wyler](http://inspirehep.net/record/235471)), as well as a scalar singlet $N$ and composite scalar color-sextets and octets. The standard leptoquark interaction Lagrangian is

![LQ lagrangian](figs/Lint_std.png)  

to which we add interactions involving the neutral scalar (here and below, all the *G*'s have dimensions of mass<sup>-1</sup>)

![LQ lagrangian](figs/Lint_LQ_N.png)  

and interactions of the sextet and octet

![LQ lagrangian](figs/Lint_68.png)

Finally, the singlet has an effective coupling to quarks and leptons  
![LQ lagrangian](figs/Lint_N.png)  


## UFO file 
[Download the UFO file here](composite_LQ_UFO.tgz), and untar it in your mg5\_aMC/models directory.

The BSM fields and the Lagrangian used as input can be found in [composite_LQ.fr](composite_LQ.fr).


##### Definitions and defaults

We have translated the lagrangians in FeynRules to generate a UFO file, keeping the names and symbols of parameters as close as possible to the nomenclature above. (parameters with a \~ have a `t` in front of their names, e.g. $\tilde{S}\_1$->`tS1`, $\tilde G$->`tG`).

| field | ![](figs/s1.png) | ![](figs/ts1.png) | ![](figs/nn.png) | ![](figs/phi6.png) | ![](figs/tphi6.png) | ![](figs/phi8.png)|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| quantum numbers | (**3**,**1**,-1/3) | (**3**,**1**,-4/3) | (**1**,**1**,0) | (**6**,**1**,-2/3) | (**3**,**1**,-8/3) | (**8**,**1**,0)
| mg5 name| S1b | tS1b | nn | six | tsix | oct
| PID | 9000010 | 9000011| 9000050 | 9000060 | 9000061 | 9000080 |

By default the leptoquarks are at 600 GeV, the sextet and octet at 1500 GeV, and the singlet scalar at 100 GeV.

Most couplings in the Lagrangian above are set to zero, apart from the entries that allow decays with c,tau or b,mu (which were the final states we were interested in the paper). For simplicity the defaults have all LH couplings set to zero and only turned on the RH couplings.

In particular, the only non-zero entries are the 23 components of the *g,G* matrices, the 32 components of *tg,tG*s, as well as *gNu*<sub>2</sub> and *gNd*<sub>3</sub>. Defaults are 1 for all non-zero dimensionless couplings, 1000 GeV (or 0.001 GeV<sup>-1</sup>) for non-zero dimensionful couplings.

## Event Generation
We considered QCD pair-production of the scalars above, followed by multiple decay steps. One can either write the whole process in Madgraph, or only produce the leptoquarks and let Pythia handle the decays (the latter is considerably faster, especially with the many final states present). For Pythia to know how to decay the new particles, we use `compute_widths` in Madgraph to calculate **all** the branching ratios.   
**NB** There is a bug/feature in `compute_widths` where it does not write partial widths of a colored particle if the width is less than the QCD scale, which can happen for some of the default parameters used. [See below for correcting this behavior in Madgraph]
(#madgraph-warning:-width-of-colored-particle-lower-than-qcd-scale).

### All Tests
All processes used in our paper are present in [composite\_LQ\_test.mg5](composite_LQ_test.mg5) and can be generated at once by running

```
bin/mg5_amc  composite_LQ_test.mg5
```

For completeness, we also list each process below.

#### Leptoquark production and decay

<img align="right" src="figs/diagram_s1_ccctau.png" width=200>
The following will produce the leptoquark $S_1$, and prepare the decay chain with c-tau, as depicted.


```
import model composite_LQ_UFO
generate p p > s1b s1b~
output lqlq_ccctau
launch
 set nevents 100
 set g1r2x3 0
 set gnnd3 0
 set gnnu2 1
 compute_widths s1b
 compute_widths nn
 done

```

<img align="right" src="figs/diagram_ts1_bbbmu.png" width=200>
The following will produce the leptoquark $\tilde{S}_1$ and prepare the decay chain with b-mu, as depicted.

```
import model composite_LQ_UFO
generate p p > ts1b ts1b~
output lqlq_bbbmu
launch
 set nevents 100
 set gt1r3x2 0
 set gnnu2 0
 set gnnd3 1
 compute_widths ts1b
 compute_widths nn
 done
```

#### Sextet production
<img align="right" src="figs/diagram_six_ccctau.png" width=200> 
The color sextet scalar can be pair-produced and then decay to two leptoquarks each, followed by the same decay chain as in the previous examples. 

```
import model composite_LQ_UFO
generate p p > six six~
output lq_sixsix_ccctau
launch
 set nevents 100
 set g1r2x3 0
 set gnnd3 0
 set gnnu2 1
 compute_widths six
 compute_widths s1b
 compute_widths nn
 done
```
<img align="right" src="figs/diagram_tsix_bbbmu.png" width=200>

```
import model composite_LQ_UFO
generate p p > tsix tsix~
output lq_sixsix_bbbmu
launch
 set nevents 100
 set gt1r3x2 0
 set gnnu2 0
 set gnnd3 1
 compute_widths tsix
 compute_widths ts1b
 compute_widths nn
 done

```

#### Octet production
<img align="right" src="figs/diagram_oct_ccctau.png" width=200> 
Finally we pair-produce the octet, each of which will decay to a quark, a lepton and a leptoquark. The two runs below will generate events with c-tau and b-mu final states.

```
import model composite_LQ_UFO
generate p p > oct  oct
output lq_octoct
launch
 set nevents 100
 set GtS8r3x2 0
 set GS8r2x3 0.001
 set g1r2x3 0
 set gnnd3 0
 set gnnu2 1
 compute_widths 9000080
 compute_widths s1b
 compute_widths nn
 done
```
<img align="right" src="figs/diagram_oct_bbbmu.png" width=200>

```
launch lq_octoct
 set nevents 100
 set GS8r2x3 0
 set GtS8r3x2 0.001
 set gt1r3x2 0
 set gnnu2 0
 set gnnd3 1
 compute_widths 9000080
 compute_widths ts1b
 compute_widths nn
 done
```

That's it!

###  Madgraph warning: "width of colored particle lower than QCD scale"
When Madgraph (in versions MG5_aMC 2.2--2.6) calculates the width of a colored particle and finds it is smaller than the QCD scale, it automatically discard that decay mode. While it is true that the correct decay should be computed between hadronized states, the decay chain is correctly captured by the undressed process, and one expects only O(1) deviations for the numerical value of the width ([see e.g. this launchpad post](https://answers.launchpad.net/mg5amcnlo/+question/257264)). 

Remembering that we are computing the widths only to fill the decay table so that pythia can use them (and we do not even care about the numerical values), we discard this warning.

One should therefore comment out three blocks in `MG5_aMC_v2_XX/madgraph/interface/madgraph_interface.py`, in the function `do_compute_widths`	where the warning appears (the only three blocks where "QCD scale" appears). In MG%_AMC 2.6.1, the blocks are reported below

```
## line 8027 of madgraph_interface.py ##
                    elif 0 < value < 0.1 and particle['color'] !=1:
                        logger.warning("partial width of particle %s lower than QCD scale:%s. Set it to zero. (%s)" \
                                   % (particle.get('name'), value, decay_to))
                        value = 0

```
```
## line 8097 of madgraph_interface.py ##
            if particle['color'] !=1 and 0 < width.real < 0.1:
                logger.warning("width of colored particle \"%s(%s)\" lower than QCD scale: %s. Set width to zero "
                               % (particle.get('name'), pid, width.real))
                width = 0
```
```
## line 8110 of madgraph_interface.py ##
                if 0 < BR.value * width <0.1 and particle['color'] !=1:
                    logger.warning("partial width of particle %s lower than QCD scale:%s. Set it to zero. (%s)" \
                                   % (particle.get('name'), BR.value * width, BR.lhacode[1:]))
                                     
                    continue

```