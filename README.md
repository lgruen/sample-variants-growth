# sample-variants-growth

Determines how the number of variants growths w.r.t. sample numbers, using the combined [HGDP + 1KG callset from gnomAD v3](https://gnomad.broadinstitute.org/downloads#v3-hgdp-1kg).

```bash
gcloud config set dataproc/region us-central1

hailctl dataproc start --max-age=4h --num-secondary-workers=50 sample-variants-growth && hailctl dataproc submit sample-variants-growth main.py && hailctl dataproc stop sample-variants-growth
```

