# PETRUSHKA_clinics

[![Check map](https://github.com/OxfordRSE/PETRUSHKA_clinics/actions/workflows/check-map.yml/badge.svg)](https://github.com/OxfordRSE/PETRUSHKA_clinics/actions/workflows/check-map.yml)


This repository contains mapping of clinics to CCG/ICB drug exclusion guidelines.

The PETRUSHKA tool is used by clinics operating under the auspices of different CCGs. 
Different CCGs have different rules governing which antidepressants may be prescribed. 
The purpose of this map is to clarify which antidepressants must be excluded from the PETRUSHKA tool according to the patient's clinic.

## `map.json`

The `map.json` file maps clinics to CCG antidepressant exclusion lists.

It consists of a list of CCG objects, 
each CCG having a list of excluded drugs and a list of clinics that belong to it. 

Clinics are always objects with a name and a (3-letter, capitalised) code.

**Even if a CCG does not require any antidepressants to be excluded, they must have an entry in `map.json`.** 
See `ccg_3_name` for an example of a CCG that does not require any antidepressants to be excluded.

### Example

Here is what the file would look like if we had the following structure:

| CCG           | Clinics             | Excluded antidepressants |
|-----          |---------            |--------------------------|
| `ccg_1_name`  | `ABC`, `DEF`, `HIJ` | `med_agomelatine`, `med_amitriptyline`, `med_citalopram` |
| `ccg_2_name`  | `KLM`               | `med_agomelatine`, `med_duloxetine` |
| `ccg_3_name`  | `NOP`, `QRS`        | *None*  |

```json5
[
  {
    "name": "ccg_1_name",
    "clinics": [
      { "name": "ABC", "code": "ABC" },
      { "name":  "Clinic 2", "code":  "DEF" },
      { "name":  "Another clinic", "code":  "HIJ" }
    ],
    "excluded_drugs": [
      "med_agomelatine",
      "med_amitriptyline",
      "med_citalopram"
    ]
  },
  {
    "name": "ccg_2_name",
    "clinics": [
      { "name": "", "code": "KLM" }
    ],
    "excluded_drugs": [
      "med_agomelatine",
      "med_duloxetine"
    ]
  },
  {
    "name": "ccg_3_name",
    "clinics": [
      { "name": "North Nowhere", "code": "NOP" },
      { "name": "Queensbury", "code": "QRS" }
    ],
    "excluded_drugs": []
  }
]
```

### Checking

Whenever `map.json` is updated, a script will run on GitHub Actions that checks whether it all makes sense.
If this goes wrong, the badge at the top of this README file will go red.
If that happens, get help immediately, because PETRUSHKA will not work without a proper version of this file hosted on GitHub.
