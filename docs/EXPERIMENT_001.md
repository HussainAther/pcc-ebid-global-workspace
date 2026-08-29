# Experiment 001: Broadcast Ablation and Competition Sweep

## Objective

Test whether global broadcast causally reduces disagreement and improves stable
task selection.

## Conditions

### Baseline

- moderate ignition threshold;
- moderate competition;
- broadcast enabled.

### High threshold

- increased ignition threshold;
- broadcast enabled.

Prediction:
fewer successful ignitions and weaker coordination.

### High competition

- increased module noise / competition;
- broadcast enabled.

Prediction:
less stable winners and increased switching.

### Broadcast disabled

- same local module dynamics as baseline;
- global broadcast removed.

Prediction:
local modules remain active, but downstream agreement and task performance
decline.

## Primary outcomes

- ignition rate;
- winner stability;
- module agreement;
- action entropy;
- switching rate;
- reward.

## PCC-EBID analysis

No PCC labels are assigned prospectively in Experiment 001.

The purpose of this experiment is to establish causal workspace dynamics first.
