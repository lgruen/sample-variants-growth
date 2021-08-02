import hail as hl

hl.init(default_reference='GRCh38')

mt = hl.read_matrix_table('gs://gcp-public-data--gnomad/release/3.1/mt/genomes/gnomad.genomes.v3.1.hgdp_1kg_subset_dense.mt')

results = []
for col_prob in (0.001, 0.0025, 0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0):
    smt = mt.sample_cols(col_prob, seed=5784)
    smt = smt.annotate_rows(is_non_ref=hl.agg.any(smt.GT.is_non_ref()))
    num_cols = smt.count_cols()
    variants = smt.aggregate_rows(hl.agg.count_where(smt.is_non_ref))
    print(f'prob: {col_prob}, n_cols: {num_cols}, variants: {variants}')
    results.append((num_cols, variants))

for num_cols, variants in results:
    print(f'{num_cols}, {variants}')

