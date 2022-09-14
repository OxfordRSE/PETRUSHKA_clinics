# PETRUSHKA_clinics

[![Check map](https://github.com/OxfordRSE/PETRUSHKA_clinics/actions/workflows/check-map.yml/badge.svg)](https://github.com/OxfordRSE/PETRUSHKA_clinics/actions/workflows/check-map.yml)


Mapping clinics to CCG drug exclusion guidelines

The PETRUSHKA tool is used by clinics operating under the auspices of different CCGs. 
Different CCGs have different rules governing which antidepressants may be prescribed. 
The purpose of this map is to clarify which antidepressants must be excluded from the PETRUSHKA tool according to the patient's clinic.

## `map.json`

The `map.json` file maps clinics to CCG antidepressant exclusion lists.

Each clinic a patient can belong to is assigned an identifier. 
These are the keys in the `clinic_CCGs` part of the file. 
The values for each key are the CCG names.

Each CCG has a list of antidepressants that are excluded for use in that clinic.
The CCG name is the key in the `CCG_exclusions` part of the file.
The value is always a list (specified with `[]`) which includes **zero or more** drug names as listed in the `petrushka_backend.__init__.py` file. 
They typically have the form `med_drugname`.

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
{
  "CCG_exclusions": {
    "ccg_1_name": [ 
      "med_agomelatine",
      "med_amitriptyline",
      "med_citalopram",
    ],
    "ccg_2_name": [
      "med_agomelatine",
      "med_duloxetine",
    ],
    "ccg_3_name": [
    ],
  },
  "clinic_CCGs": {
    "ABC": "ccg_1_name",
    "DEF": "ccg_1_name",
    "HIJ": "ccg_1_name",
    "KLM": "ccg_2_name",
    "NOP": "ccg_3_name",
    "QRS": "ccg_3_name",
  },
}
```

### Checking

Whenever `map.json` is updated, a script will run on GitHub Actions that checks whether it all makes sense.
If this goes wrong, the badge at the top of this README file will go red.
If that happens, get help immediately, because PETRUSHKA will not work without a proper version of this file hosted on GitHub.

