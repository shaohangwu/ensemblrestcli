import typer
from typing import List
import requests

app=typer.Typer()
@app.command()
def archive_id_get(id: str,callback=None):
  print(requests.get(f"https://rest.ensembl.org/archive/id/{id}", headers={"Content-Type": "application/json"},params=dict(callback=callback,format=format),).json())

@app.command()
def archive_id_post(id: List[str],callback=None):
  print(requests.post(f"https://rest.ensembl.org/archive/id", headers={"Content-Type": "application/json"},params=dict(callback=callback),json={"id": id},).json())

@app.command()
def cafe_tree(id: str,callback=None, compara=None, nh_format=None):
  print(requests.get(f"https://rest.ensembl.org/cafe/genetree/id/{id}", headers={"Content-Type": "application/json"},params=dict(callback=callback, compara=compara, nh_format=nh_format,format=format)).json())

@app.command()
def cafe_tree_member_id(id: str,callback=None, compara=None, db_type=None, nh_format=None, object_type=None, species=None):
  print(requests.get(f"https://rest.ensembl.org/cafe/genetree/member/id/{id}", headers={"Content-Type": "application/json"},params=dict(callback=callback, compara=compara, db_type=db_type, nh_format=nh_format, object_type=object_type, species=species,format=format),).json())

@app.command()
def cafe_tree_member_symbol(species: str, symbol: str,callback=None, compara=None, db_type=None, external_db=None, nh_format=None, object_type=None):
  print(requests.get(f"https://rest.ensembl.org/cafe/genetree/member/symbol/{species}/{symbol}", headers={"Content-Type": "application/json"},params=dict(callback=callback, compara=compara, db_type=db_type, external_db=external_db, nh_format=nh_format, object_type=object_type,format=format),).json())

@app.command()
def cafe_tree_species_member_id(id: str, species: str,callback=None, compara=None, db_type=None, nh_format=None, object_type=None):
  print(requests.get(f"https://rest.ensembl.org/cafe/genetree/member/id/{species}/{id}", headers={"Content-Type": "application/json"},params=dict(callback=callback, compara=compara, db_type=db_type, nh_format=nh_format, object_type=object_type,format=format),).json())

@app.command()
def genetree(id: str,aligned=None, callback=None, cigar_line=None, clusterset_id=None, compara=None, nh_format=None, prune_species=None, prune_taxon=None, sequence=None):
  print(requests.get(f"https://rest.ensembl.org/genetree/id/{id}", headers={"Content-Type": "application/json"},params=dict(aligned=aligned, callback=callback, cigar_line=cigar_line, clusterset_id=clusterset_id, compara=compara, nh_format=nh_format, prune_species=prune_species, prune_taxon=prune_taxon, sequence=sequence,format=format),).json())

@app.command()
def genetree_member_id(id: str,aligned=None, callback=None, cigar_line=None, clusterset_id=None, compara=None, db_type=None, nh_format=None, object_type=None, prune_species=None, prune_taxon=None, sequence=None, species=None):
  print(requests.get(f"https://rest.ensembl.org/genetree/member/id/{id}", headers={"Content-Type": "application/json"},params=dict(aligned=aligned, callback=callback, cigar_line=cigar_line, clusterset_id=clusterset_id, compara=compara, db_type=db_type, nh_format=nh_format, object_type=object_type, prune_species=prune_species, prune_taxon=prune_taxon, sequence=sequence, species=species,format=format),).json())

@app.command()
def genetree_member_symbol(species: str, symbol: str,aligned=None, callback=None, cigar_line=None, clusterset_id=None, compara=None, db_type=None, external_db=None, nh_format=None, object_type=None, prune_species=None, prune_taxon=None, sequence=None):
  print(requests.get(f"https://rest.ensembl.org/genetree/member/symbol/{species}/{symbol}", headers={"Content-Type": "application/json"},params=dict(aligned=aligned, callback=callback, cigar_line=cigar_line, clusterset_id=clusterset_id, compara=compara, db_type=db_type, external_db=external_db, nh_format=nh_format, object_type=object_type, prune_species=prune_species, prune_taxon=prune_taxon, sequence=sequence,format=format),).json())

@app.command()
def genetree_species_member_id(id: str, species: str,aligned=None, callback=None, cigar_line=None, clusterset_id=None, compara=None, db_type=None, nh_format=None, object_type=None, prune_species=None, 
prune_taxon=None, sequence=None):
  print(requests.get(f"https://rest.ensembl.org/genetree/member/id/{species}/{id}", headers={"Content-Type": "application/json"},params=dict(aligned=aligned, callback=callback, cigar_line=cigar_line, clusterset_id=clusterset_id, compara=compara, db_type=db_type, nh_format=nh_format, object_type=object_type, prune_species=prune_species, prune_taxon=prune_taxon, sequence=sequence,format=format),).json())

# print(func0(urls[10]))
@app.command()
def genomic_alignment_region(region: str, species: str,aligned=None, callback=None, compact=None, compara=None, display_species_set=None, mask=None, method=None, species_set=None, species_set_group=None):
  print(requests.get(f"https://rest.ensembl.org/alignment/region/{species}/{region}", headers={"Content-Type": "application/json"},params=dict(aligned=aligned, callback=callback, compact=compact, compara=compara, display_species_set=display_species_set, mask=mask, method=method, species_set=species_set, species_set_group=species_set_group,format=format),).json())

@app.command()
def homology_ensemblgene(id: str,aligned=None, callback=None, cigar_line=None, compara=None, format=None, sequence=None, target_species=None, target_taxon=None, type=None):
  print(requests.get(f"https://rest.ensembl.org/homology/id/{id}", headers={"Content-Type": "application/json"},params=dict(aligned=aligned, callback=callback, cigar_line=cigar_line, compara=compara, format=format, sequence=sequence, target_species=target_species, target_taxon=target_taxon, type=type),).json())

@app.command()
def homology_species_gene_id(id: str, species: str,aligned=None, callback=None, cigar_line=None, compara=None, format=None, sequence=None, target_species=None, target_taxon=None, type=None):
  print(requests.get(f"https://rest.ensembl.org/homology/id/{species}/{id}", headers={"Content-Type": "application/json"},params=dict(aligned=aligned, callback=callback, cigar_line=cigar_line, compara=compara, format=format, sequence=sequence, target_species=target_species, target_taxon=target_taxon, type=type),).json())

# print(func0(urls[13]))
@app.command()
def homology_symbol(species: str, symbol: str,aligned=None, callback=None, cigar_line=None, compara=None, external_db=None, format=None, sequence=None, target_species=None, target_taxon=None, type=None):
  print(requests.get(f"https://rest.ensembl.org/homology/symbol/{species}/{symbol}", headers={"Content-Type": "application/json"},params=dict(aligned=aligned, callback=callback, cigar_line=cigar_line, 
compara=compara, external_db=external_db, format=format, sequence=sequence, target_species=target_species, target_taxon=target_taxon, type=type),).json())

# Cross References ----14
@app.command()
def xref_external(species: str, symbol: str,callback=None, db_type=None, external_db=None, object_type=None):
  print(requests.get(f"https://rest.ensembl.org/xrefs/symbol/{species}/{symbol}", headers={"Content-Type": "application/json"},params=dict(callback=callback, db_type=db_type, external_db=external_db, object_type=object_type),).json())

@app.command()
def xref_id(id: str,all_levels=None, callback=None, db_type=None, external_db=None, object_type=None, species=None):
  print(requests.get(f"https://rest.ensembl.org/xrefs/id/{id}", headers={"Content-Type": "application/json"},params=dict(all_levels=all_levels, callback=callback, db_type=db_type, external_db=external_db, object_type=object_type, species=species),).json())

@app.command()
def xref_name(name: str, species: str,callback=None, db_type=None, external_db=None):
  print(requests.get(f"https://rest.ensembl.org/xrefs/name/{species}/{name}", headers={"Content-Type": "application/json"},params=dict(callback=callback, db_type=db_type, external_db=external_db),).json())

# Information----17
@app.command()
def analysis(species: str,callback=None):
  print(requests.get(f"https://rest.ensembl.org/info/analysis/{species}", headers={"Content-Type": "application/json"},params=dict(callback=callback),).json())

@app.command()
def assembly_info(species: str,bands=None, callback=None, synonyms=None):
  print(requests.get(f"https://rest.ensembl.org/info/assembly/{species}", headers={"Content-Type": "application/json"},params=dict(bands=bands, callback=callback, synonyms=synonyms),).json())

@app.command()
def assembly_stats(region_name: str, species: str,bands=None, callback=None, synonyms=None):
  print(requests.get(f"https://rest.ensembl.org/info/assembly/{species}/{region_name}", headers={"Content-Type": "application/json"},params=dict(bands=bands, callback=callback, synonyms=synonyms),).json())

@app.command()
def biotypes(species: str,callback=None):
  print(requests.get(f"https://rest.ensembl.org/info/biotypes/{species}", headers={"Content-Type": "application/json"},params=dict(callback=callback),).json())

# 没有必选参数
@app.command()
def biotypes_groups(callback=None, group=None, object_type=None):
  print(requests.get(f"https://rest.ensembl.org/info/biotypes/groups/", headers={"Content-Type": "application/json"},params=dict(callback=callback, group=group, object_type=object_type),).json())

@app.command()
def biotypes_name(name: str,callback=None, object_type=None):
  print(requests.get(f"https://rest.ensembl.org/info/biotypes/name/{name}/", headers={"Content-Type": "application/json"},params=dict(callback=callback, object_type=object_type),).json())

@app.command()
def compara_methods(callback=None, Class=None, compara=None):
  print(requests.get(f"https://rest.ensembl.org/info/compara/methods", headers={"Content-Type": "application/json"},params=dict(callback=callback, Class=Class, compara=compara),).json())

@app.command()
def compara_species_sets(method: str,callback=None, compara=None):
  print(requests.get(f"https://rest.ensembl.org/info/compara/species_sets/{method}", headers={"Content-Type": "application/json"},params=dict(callback=callback, compara=compara),).json())

@app.command()
def comparas(callback=None):
  print(requests.get(f"https://rest.ensembl.org/info/comparas", headers={"Content-Type": "application/json"},params=dict(callback=callback),).json())

@app.command()
def data(callback=None):
  print(requests.get(f"https://rest.ensembl.org/info/data", headers={"Content-Type": "application/json"},params=dict(callback=callback),).json())

@app.command()
def eg_version(callback=None):
  print(requests.get(f"https://rest.ensembl.org/info/eg_version", headers={"Content-Type": "application/json"},params=dict(callback=callback),).json())

@app.command()
def external_dbs(species: str,callback=None, feature=None, filter=None):
  print(requests.get(f"https://rest.ensembl.org/info/external_dbs/{species}", headers={"Content-Type": "application/json"},params=dict(callback=callback, feature=feature, filter=filter),).json())

@app.command()
def info_divisions(callback=None):
  print(requests.get(f"https://rest.ensembl.org/info/divisions", headers={"Content-Type": "application/json"},params=dict(callback=callback),).json())

@app.command()
def info_genome(name: str,callback=None, expand=None):
  print(requests.get(f"https://rest.ensembl.org/info/genomes/{name}", headers={"Content-Type": "application/json"},params=dict(callback=callback, expand=expand),).json())        

@app.command()
def info_genomes_accession(accession: str,callback=None, expand=None):
  print(requests.get(f"https://rest.ensembl.org/info/genomes/accession/{accession}", headers={"Content-Type": "application/json"},params=dict(callback=callback, expand=expand),).json())

@app.command()
def info_genomes_assembly(assembly_id: str,callback=None, expand=None):
  print(requests.get(f"https://rest.ensembl.org/info/genomes/assembly/{assembly_id}", headers={"Content-Type": "application/json"},params=dict(callback=callback, expand=expand),).json())

@app.command()
def info_genomes_division(division: str,callback=None, expand=None):
  print(requests.get(f"https://rest.ensembl.org/info/genomes/division/{division}", headers={"Content-Type": "application/json"},params=dict(callback=callback, expand=expand),).json())

# python .\test.py info-genomes-taxonomy 'Homo sapiens'
@app.command()
def info_genomes_taxonomy(taxon_name: str,callback=None, expand=None):
  print(requests.get(f"https://rest.ensembl.org/info/genomes/taxonomy/{taxon_name}", headers={"Content-Type": "application/json"},params=dict(callback=callback, expand=expand),).json())

@app.command()
def ping(callback=None):
  print(requests.get(f"https://rest.ensembl.org/info/ping", headers={"Content-Type": "application/json"},params=dict(callback=callback),).json())

@app.command()
def rest(callback=None):
  print(requests.get(f"https://rest.ensembl.org/info/rest", headers={"Content-Type": "application/json"},params=dict(callback=callback),).json())

@app.command()
def software(callback=None):
  print(requests.get(f"https://rest.ensembl.org/info/software", headers={"Content-Type": "application/json"},params=dict(callback=callback),).json())

@app.command()
def species(callback=None, division=None, hide_strain_info=None, strain_collection=None):
  print(requests.get(f"https://rest.ensembl.org/info/species", headers={"Content-Type": "application/json"},params=dict(callback=callback, division=division, hide_strain_info=hide_strain_info, strain_collection=strain_collection),).json())

@app.command()
def variation(species: str,callback=None, filter=None):
  print(requests.get(f"https://rest.ensembl.org/info/variation/{species}", headers={"Content-Type": "application/json"},params=dict(callback=callback, filter=filter),).json())

@app.command()
def variation_consequence_types(callback=None, rank=None):
  print(requests.get(f"https://rest.ensembl.org/info/variation/consequence_types", headers={"Content-Type": "application/json"},params=dict(callback=callback, rank=rank),).json())      

# -----41
# python .\test.py variation-population-name 1000GENOMES:phase_3:ASW human
@app.command()
def variation_population_name(population_name: str, species: str,callback=None):
  print(requests.get(f"https://rest.ensembl.org/info/variation/populations/{species}/{population_name}", headers={"Content-Type": "application/json"},params=dict(callback=callback),).json())

@app.command()
def variation_populations(species: str,callback=None, filter=None):
  print(requests.get(f"https://rest.ensembl.org/info/variation/populations/{species}", headers={"Content-Type": "application/json"},params=dict(callback=callback, filter=filter),).json())

# Linkage Disequilibrium----43
# python .\test.py ld-id-get rs1042779 1000GENOMES:phase_3:KHV human
@app.command()
def ld_id_get(id: str, population_name: str, species: str,attribs=None, callback=None, d_prime=None, r2=None, window_size=None):
  print(requests.get(f"https://rest.ensembl.org/ld/{species}/{id}/{population_name}", headers={"Content-Type": "application/json"},params=dict(attribs=attribs, callback=callback, d_prime=d_prime, r2=r2, window_size=window_size),).json())

# python .\test.py ld-pairwise-get rs6792369 rs1042779 human
@app.command()
def ld_pairwise_get(id1: str, id2: str, species: str,callback=None, d_prime=None, population_name=None, r2=None):
  print(requests.get(f"https://rest.ensembl.org/ld/{species}/pairwise/{id1}/{id2}", headers={"Content-Type": "application/json"},params=dict(callback=callback, d_prime=d_prime, population_name=population_name, r2=r2),).json())

@app.command()
def ld_region_get(population_name: str, region: str, species: str,callback=None, d_prime=None, r2=None):
  print(requests.get(f"https://rest.ensembl.org/ld/{species}/region/{region}/{population_name}", headers={"Content-Type": "application/json"},params=dict(callback=callback, d_prime=d_prime, r2=r2),).json())

# Lookup----46
@app.command()
def lookup(id: str,callback=None, db_type=None, expand=None, format=None, mane=None, phenotypes=None, species=None, utr=None):
  print(requests.get(f"https://rest.ensembl.org/lookup/id/{id}", headers={"Content-Type": "application/json"},params=dict(callback=callback, db_type=db_type, expand=expand, format=format, mane=mane, phenotypes=phenotypes, species=species, utr=utr),).json())

# python .\test.py lookup-post ENSG00000157764 ENSG00000248378
@app.command()
def lookup_post(id: List[str],callback=None, db_type=None, expand=None, format=None, object_type=None, species=None):
  print(requests.post(f"https://rest.ensembl.org/lookup/id", headers={"Content-Type": "application/json"},params=dict(callback=callback, db_type=db_type, expand=expand, format=format, object_type=object_type, species=species),json={"ids": id},).json())

@app.command()
def symbol_lookup(species: str, symbol: str,callback=None, expand=None, format=None):
  print(requests.get(f"https://rest.ensembl.org/lookup/symbol/{species}/{symbol}", headers={"Content-Type": "application/json"},params=dict(callback=callback, expand=expand, format=format),).json())

# python .\test.py symbol-post BRCA2 BRAF homo_sapiens
@app.command()
def symbol_post(symbol: List[str],species: str,callback=None, expand=None, format=None):
  print(requests.post(f"https://rest.ensembl.org/lookup/symbol/{species}/{symbol}", headers={"Content-Type": "application/json"},params=dict(callback=callback, expand=expand, format=format),json={"symbols": symbol},).json())


# Mapping----50
@app.command()
def assembly_cdna(id: str, region: str,callback=None, include_original_region=None, species=None):
  print(requests.get(f"https://rest.ensembl.org/map/cdna/{id}/{region}", headers={"Content-Type": "application/json"},params=dict(callback=callback, include_original_region=include_original_region, species=species),).json())

@app.command()
def assembly_cds(id: str, region: str,callback=None, include_original_region=None, species=None):
  print(requests.get(f"https://rest.ensembl.org/map/cds/{id}/{region}", headers={"Content-Type": "application/json"},params=dict(callback=callback, include_original_region=include_original_region, species=species),).json())

#  python .\test.py assembly-map GRCh37 GRCh38 X:1000000..1000100:1 homo_sapiens
@app.command()
def assembly_map(asm_one: str, asm_two: str, region: str, species: str,callback=None, coord_system=None, target_coord_system=None):
  print(requests.get(f"https://rest.ensembl.org/map/{species}/{asm_one}/{region}/{asm_two}", headers={"Content-Type": "application/json"},params=dict(callback=callback, coord_system=coord_system, target_coord_system=target_coord_system),).json())

# python .\test.py assembly-translation ENSP00000288602 100..300
@app.command()
def assembly_translation(id: str, region: str,callback=None, species=None):
  print(requests.get(f"https://rest.ensembl.org/map/translation/{id}/{region}", headers={"Content-Type": "application/json"},params=dict(callback=callback, species=species),).json())   

# Ontologies and Taxonomy----54
# python .\test.py ontology-ancestors GO:0005667
@app.command()
def ontology_ancestors(id: str,callback=None, ontology=None):
  print(requests.get(f"https://rest.ensembl.org/ontology/ancestors/{id}", headers={"Content-Type": "application/json"},params=dict(callback=callback, ontology=ontology),).json())       

@app.command()
def ontology_ancestors_chart(id: str,callback=None, ontology=None):
  print(requests.get(f"https://rest.ensembl.org/ontology/ancestors/chart/{id}", headers={"Content-Type": "application/json"},params=dict(callback=callback, ontology=ontology),).json())

@app.command()
def ontology_descendants(id: str,callback=None, closest_term=None, ontology=None, subset=None, zero_distance=None):
  print(requests.get(f"https://rest.ensembl.org/ontology/descendants/{id}", headers={"Content-Type": "application/json"},params=dict(callback=callback, closest_term=closest_term, ontology=ontology, subset=subset, zero_distance=zero_distance),).json())

@app.command()
def ontology_id(id: str,callback=None, relation=None, simple=None):
  print(requests.get(f"https://rest.ensembl.org/ontology/id/{id}", headers={"Content-Type": "application/json"},params=dict(callback=callback, relation=relation, simple=simple),).json())

# python .\test.py ontology-name 'transcription factor complex'
@app.command()
def ontology_name(name: str,callback=None, ontology=None, relation=None, simple=None):
  print(requests.get(f"https://rest.ensembl.org/ontology/name/{name}", headers={"Content-Type": "application/json"},params=dict(callback=callback, ontology=ontology, relation=relation,simple=simple),).json())

@app.command()
def taxonomy_classification(id: str,callback=None):
  print(requests.get(f"https://rest.ensembl.org/taxonomy/classification/{id}", headers={"Content-Type": "application/json"},params=dict(callback=callback),).json())

@app.command()
def taxonomy_id(id: str,callback=None, simple=None):
  print(requests.get(f"https://rest.ensembl.org/taxonomy/id/{id}", headers={"Content-Type": "application/json"},params=dict(callback=callback, simple=simple),).json())

@app.command()
def taxonomy_name(name: str,callback=None):
  print(requests.get(f"https://rest.ensembl.org/taxonomy/name/{name}", headers={"Content-Type": "application/json"},params=dict(callback=callback),).json())


# Overlap----62
# python .\test.py overlap-id ENSG00000157764
# feature默认了gene
@app.command()
def overlap_id(id: str,feature="gene",biotype=None, callback=None, db_type=None, logic_name=None, misc_set=None, object_type=None, so_term=None, species=None, species_set=None, variant_set=None):
  print(requests.get(f"https://rest.ensembl.org/overlap/id/{id}", headers={"Content-Type": "application/json"},params=dict(biotype=biotype, callback=callback, db_type=db_type, logic_name=logic_name, misc_set=misc_set, object_type=object_type, so_term=so_term, species=species, species_set=species_set, variant_set=variant_set,feature=feature),).json())

# python .\test.py overlap-region X:1..1000 homo_sapiens
@app.command()
def overlap_region(region: str, species: str,feature="gene", biotype=None, callback=None, db_type=None, logic_name=None, misc_set=None, so_term=None, species_set=None, trim_downstream=None, trim_upstream=None, variant_set=None):
  print(requests.get(f"https://rest.ensembl.org/overlap/region/{species}/{region}", headers={"Content-Type": "application/json"},params=dict(biotype=biotype, feature=feature,
callback=callback, db_type=db_type, logic_name=logic_name, misc_set=misc_set, so_term=so_term, species_set=species_set, trim_downstream=trim_downstream, trim_upstream=trim_upstream, variant_set=variant_set),).json())

@app.command()
def overlap_translation(id: str,callback=None, db_type=None, feature=None, so_term=None, species=None, type=None):
  print(requests.get(f"https://rest.ensembl.org/overlap/translation/{id}", headers={"Content-Type": "application/json"},params=dict(callback=callback, db_type=db_type, feature=feature, so_term=so_term, species=species, type=type),).json())

# Phenotype annotations----65
@app.command()
def phenotype_accession(accession: str, species: str,callback=None, include_children=None, include_pubmed_id=None, include_review_status=None, source=None):  
  print(requests.get(f"https://rest.ensembl.org//phenotype/accession/{species}/{accession}", headers={"Content-Type": "application/json"},params=dict(callback=callback, include_children=include_children, include_pubmed_id=include_pubmed_id, include_review_status=include_review_status, source=source),).json())      

@app.command()
def phenotype_gene(gene: str, species: str,callback=None, include_associated=None, include_overlap=None, include_pubmed_id=None, include_review_status=None, include_submitter=None, non_specified=None, trait=None, tumour=None):
  print(requests.get(f"https://rest.ensembl.org//phenotype/gene/{species}/{gene}", headers={"Content-Type": "application/json"},params=dict(callback=callback, include_associated=include_associated, include_overlap=include_overlap, include_pubmed_id=include_pubmed_id, include_review_status=include_review_status, include_submitter=include_submitter, non_specified=non_specified, trait=trait, tumour=tumour),).json())

@app.command()
def phenotype_region(region: str, species: str,callback=None, feature_type=None, include_pubmed_id=None, include_review_status=None, include_submitter=None, non_specified=None, only_phenotypes=None, trait=None, tumour=None):
  print(requests.get(f"https://rest.ensembl.org//phenotype/region/{species}/{region}", headers={"Content-Type": "application/json"},params=dict(callback=callback, feature_type=feature_type, include_pubmed_id=include_pubmed_id, include_review_status=include_review_status, include_submitter=include_submitter, non_specified=non_specified, only_phenotypes=only_phenotypes, trait=trait, tumour=tumour),).json())

# python .\test.py phenotype-term homo_sapiens 'coffee consumption'
@app.command()
def phenotype_term(species: str, term: str,callback=None, include_children=None, include_pubmed_id=None, include_review_status=None, source=None):
  print(requests.get(f"https://rest.ensembl.org//phenotype/term/{species}/{term}", headers={"Content-Type": "application/json"},params=dict(callback=callback, include_children=include_children, include_pubmed_id=include_pubmed_id, include_review_status=include_review_status, source=source),).json())

# Regulation----69
# python .\test.py array HumanWG_6_V3 homo_sapiens illumina
@app.command()
def array(microarray: str, species: str, vendor: str,callback=None):
  print(requests.get(f"https://rest.ensembl.org/regulatory/species/{species}/microarray/{microarray}/vendor/{vendor}", headers={"Content-Type": "application/json"},params=dict(callback=callback),).json())

@app.command()
def fetch_all_epigenomes(species: str,callback=None):
  print(requests.get(f"https://rest.ensembl.org/regulatory/species/{species}/epigenome", headers={"Content-Type": "application/json"},params=dict(callback=callback),).json())

# python .\test.py get-binding-matrix ENSPFM0001 homo_sapiens
@app.command()
def get_binding_matrix(binding_matrix: str, species: str,callback=None, unit=None):
  print(requests.get(f"https://rest.ensembl.org/species/{species}/binding_matrix/{binding_matrix}/", headers={"Content-Type": "application/json"},params=dict(callback=callback, unit=unit),).json())

@app.command()
def list_all_microarrays(species: str,callback=None):
  print(requests.get(f"https://rest.ensembl.org/regulatory/species/{species}/microarray", headers={"Content-Type": "application/json"},params=dict(callback=callback),).json())

# python .\test.py probe HumanWG_6_V3 ILMN_1910180 homo_sapiens
@app.command()
def probe(microarray: str, probe: str, species: str,callback=None, gene=None, transcripts=None):
  print(requests.get(f"https://rest.ensembl.org/regulatory/species/{species}/microarray/{microarray}/probe/{probe}", headers={"Content-Type": "application/json"},params=dict(callback=callback, gene=gene, transcripts=transcripts),).json())

@app.command()
def probe_set(microarray: str, probe_set: str, species: str,callback=None, gene=None, transcripts=None):
  print(requests.get(f"https://rest.ensembl.org/regulatory/species/{species}/microarray/{microarray}/probe_set/{probe_set}", headers={"Content-Type": "application/json"},params=dict(callback=callback, gene=gene, transcripts=transcripts),).json())

@app.command()
def regulatory_id(id: str, species: str,activity=None, callback=None):
  print(requests.get(f"https://rest.ensembl.org/regulatory/species/{species}/id/{id}", headers={"Content-Type": "application/json"},params=dict(activity=activity, callback=callback),).json())

# Sequence----76
@app.command()
def sequence_id(id: str,callback=None, db_type=None, end=None, expand_3prime=None, expand_5prime=None, format=None, mask=None, mask_feature=None, multiple_sequences=None, object_type=None, species=None, start=None, type=None):
  print(requests.get(f"https://rest.ensembl.org/sequence/id/{id}", headers={"Content-Type": "application/json"},params=dict(callback=callback, db_type=db_type, end=end, expand_3prime=expand_3prime, expand_5prime=expand_5prime, format=format, mask=mask, mask_feature=mask_feature, multiple_sequences=multiple_sequences, object_type=object_type, species=species, start=start, type=type),).json())

# python .\test.py sequence-id-post ENSG00000157764 ENSG00000248378
@app.command()
def sequence_id_post(id: List[str],callback=None, db_type=None, end=None, expand_3prime=None, expand_5prime=None, format=None, mask=None, mask_feature=None, object_type=None, species=None, start=None, type=None):
  print(requests.post(f"https://rest.ensembl.org/sequence/id", headers={"Content-Type": "application/json"},params=dict(callback=callback, db_type=db_type, end=end, expand_3prime=expand_3prime, expand_5prime=expand_5prime, format=format, mask=mask, mask_feature=mask_feature, object_type=object_type, species=species, start=start, type=type),json={"ids": id},).json())

@app.command()
def sequence_region(region: str, species: str,callback=None, coord_system=None, coord_system_version=None, expand_3prime=None, expand_5prime=None, format=None, mask=None, mask_feature=None):
  print(requests.get(f"https://rest.ensembl.org/sequence/region/{species}/{region}", headers={"Content-Type": "application/json"},params=dict(callback=callback, coord_system=coord_system, coord_system_version=coord_system_version, expand_3prime=expand_3prime, expand_5prime=expand_5prime, format=format, mask=mask, mask_feature=mask_feature),).json())

# python .\test.py sequence-region-post X:1000000..1000100:1 ABBA01004489.1:1..100 human
# {'error': 'No results found'}
@app.command()
def sequence_region_post(region: List[str],species: str,callback=None, coord_system=None, coord_system_version=None, expand_3prime=None, expand_5prime=None, format=None, mask=None, mask_feature=None):
  print(requests.post(f"https://rest.ensembl.org/sequence/region/{species}", headers={"Content-Type": "application/json"},params=dict(callback=callback, coord_system=coord_system, coord_system_version=coord_system_version, expand_3prime=expand_3prime, expand_5prime=expand_5prime, format=format, mask=mask, mask_feature=mask_feature),json={"regionss": region},).json())

# Transcript Haplotypes----80
@app.command()
def transcript_haplotypes_get(id: str, species: str,aligned_sequences=None, callback=None, samples=None, sequence=None):
  print(requests.get(f"https://rest.ensembl.org/transcript_haplotypes/{species}/{id}", headers={"Content-Type": "application/json"},params=dict(aligned_sequences=aligned_sequences, callback=callback, samples=samples, sequence=sequence),).json())

# VEP----81
@app.command()
def vep_hgvs_get(hgvs_notation: str, species: str,AncestralAllele=None, Blosum62=None, CADD=None, Conservation=None, DisGeNET=None, EVE=None, GO=None, GeneSplicer=None, Geno2MP=None, IntAct=None, LoF=None, Mastermind=None, MaveDB=None, MaxEntScan=None, NMD=None, Phenotypes=None, SpliceAI=None, UTRAnnotator=None, ambiguous_hgvs=None, appris=None, callback=None, canonical=None, ccds=None, dbNSFP=None, dbscSNV=None, distance=None, domains=None, failed=None, flag_pick=None, flag_pick_allele=None, flag_pick_allele_gene=None, ga4gh_vrs=None, gencode_basic=None, hgvs=None, mane=None, merged=None, minimal=None, mirna=None, mutfunc=None, numbers=None, per_gene=None, pick=None, pick_allele=None, pick_allele_gene=None, pick_order=None, protein=None, refseq=None, shift_3prime=None, shift_genomic=None, transcript_id=None, transcript_version=None, tsl=None, uniprot=None, variant_class=None, vcf_string=None, xref_refseq=None):
  print(requests.get(f"https://rest.ensembl.org/vep/{species}/hgvs/{hgvs_notation}", headers={"Content-Type": "application/json"},params=dict(AncestralAllele=AncestralAllele, Blosum62=Blosum62, CADD=CADD, Conservation=Conservation, DisGeNET=DisGeNET, EVE=EVE, GO=GO, GeneSplicer=GeneSplicer, Geno2MP=Geno2MP, IntAct=IntAct, LoF=LoF, Mastermind=Mastermind, MaveDB=MaveDB, MaxEntScan=MaxEntScan, NMD=NMD, Phenotypes=Phenotypes, SpliceAI=SpliceAI, UTRAnnotator=UTRAnnotator, ambiguous_hgvs=ambiguous_hgvs, appris=appris, callback=callback, canonical=canonical, ccds=ccds, dbNSFP=dbNSFP, dbscSNV=dbscSNV, distance=distance, domains=domains, failed=failed, flag_pick=flag_pick, flag_pick_allele=flag_pick_allele, flag_pick_allele_gene=flag_pick_allele_gene, ga4gh_vrs=ga4gh_vrs, gencode_basic=gencode_basic, hgvs=hgvs, mane=mane, merged=merged, minimal=minimal, mirna=mirna, mutfunc=mutfunc, numbers=numbers, per_gene=per_gene, pick=pick, pick_allele=pick_allele, pick_allele_gene=pick_allele_gene, pick_order=pick_order, protein=protein, refseq=refseq, shift_3prime=shift_3prime, shift_genomic=shift_genomic, transcript_id=transcript_id, transcript_version=transcript_version, tsl=tsl, uniprot=uniprot, variant_class=variant_class, vcf_string=vcf_string, xref_refseq=xref_refseq),).json())

# python .\test.py vep-hgvs-post ENST00000366667:c.803C>T 9:g.22125504G>C homo_sapiens
@app.command()
def vep_hgvs_post(hgvs_notation: List[str],species: str,
                  AncestralAllele=None, Blosum62=None, CADD=None, DisGeNET=None, EVE=None, GO=None, GeneSplicer=None, Geno2MP=None, IntAct=None, 
                  LoF=None, Mastermind=None, MaveDB=None, MaxEntScan=None, NMD=None, 
                  Phenotypes=None, SpliceAI=None, UTRAnnotator=None, ambiguous_hgvs=None, appris=None, callback=None, canonical=None, ccds=None, dbNSFP=None, dbscSNV=None, distance=None, domains=None, failed=None, flag_pick=None, flag_pick_allele=None, flag_pick_allele_gene=None, ga4gh_vrs=None, gencode_basic=None, hgvs=None, mane=None, merged=None, minimal=None, mirna=None, mutfunc=None, numbers=None, per_gene=None, pick=None, pick_allele=None, pick_allele_gene=None, pick_order=None, protein=None, refseq=None, shift_3prime=None, shift_genomic=None, transcript_id=None, transcript_version=None, tsl=None, uniprot=None, variant_class=None, vcf_string=None, xref_refseq=None):
  print(requests.post(f"https://rest.ensembl.org/vep/{species}/hgvs", 
                      headers={"Content-Type": "application/json"},
                      params=dict(AncestralAllele=AncestralAllele, Blosum62=Blosum62, CADD=CADD, DisGeNET=DisGeNET, EVE=EVE, GO=GO, GeneSplicer=GeneSplicer, Geno2MP=Geno2MP, IntAct=IntAct, LoF=LoF, Mastermind=Mastermind, MaveDB=MaveDB, MaxEntScan=MaxEntScan, NMD=NMD, Phenotypes=Phenotypes, SpliceAI=SpliceAI, UTRAnnotator=UTRAnnotator, ambiguous_hgvs=ambiguous_hgvs, appris=appris, callback=callback, canonical=canonical, ccds=ccds, dbNSFP=dbNSFP, dbscSNV=dbscSNV, distance=distance, domains=domains, failed=failed, flag_pick=flag_pick, flag_pick_allele=flag_pick_allele, flag_pick_allele_gene=flag_pick_allele_gene, ga4gh_vrs=ga4gh_vrs, gencode_basic=gencode_basic, hgvs=hgvs, mane=mane, merged=merged, minimal=minimal, mirna=mirna, mutfunc=mutfunc, numbers=numbers, per_gene=per_gene, pick=pick, pick_allele=pick_allele, pick_allele_gene=pick_allele_gene, pick_order=pick_order, protein=protein, refseq=refseq, shift_3prime=shift_3prime, shift_genomic=shift_genomic, transcript_id=transcript_id, transcript_version=transcript_version, tsl=tsl, uniprot=uniprot, variant_class=variant_class, vcf_string=vcf_string, xref_refseq=xref_refseq),
                      json={"hgvs_notations": hgvs_notation},).json())

@app.command()
def vep_id_get(id: str, species: str,
               AncestralAllele=None, Blosum62=None, CADD=None, Conservation=None, DisGeNET=None, EVE=None, GO=None, GeneSplicer=None, Geno2MP=None, IntAct=None, LoF=None, Mastermind=None, MaveDB=None, MaxEntScan=None, NMD=None, Phenotypes=None, SpliceAI=None, UTRAnnotator=None, appris=None, callback=None, canonical=None, ccds=None, dbNSFP=None, dbscSNV=None, distance=None, domains=None, failed=None, flag_pick=None, flag_pick_allele=None, flag_pick_allele_gene=None, ga4gh_vrs=None, gencode_basic=None, hgvs=None, mane=None, merged=None, minimal=None, mirna=None, mutfunc=None, numbers=None, per_gene=None, pick=None, pick_allele=None, pick_allele_gene=None, pick_order=None, protein=None, refseq=None, shift_3prime=None, shift_genomic=None, transcript_id=None, transcript_version=None, tsl=None, uniprot=None, variant_class=None, vcf_string=None, xref_refseq=None):
  print(requests.get(f"https://rest.ensembl.org/vep/{species}/id/{id}", 
                     headers={"Content-Type": "application/json"},
                     params=dict(AncestralAllele=AncestralAllele, Blosum62=Blosum62, CADD=CADD, Conservation=Conservation, DisGeNET=DisGeNET, EVE=EVE, GO=GO, GeneSplicer=GeneSplicer, Geno2MP=Geno2MP, IntAct=IntAct, LoF=LoF, Mastermind=Mastermind, MaveDB=MaveDB, MaxEntScan=MaxEntScan, NMD=NMD, Phenotypes=Phenotypes, SpliceAI=SpliceAI, UTRAnnotator=UTRAnnotator, appris=appris, callback=callback, canonical=canonical, ccds=ccds, dbNSFP=dbNSFP, dbscSNV=dbscSNV, distance=distance, domains=domains, failed=failed, flag_pick=flag_pick, flag_pick_allele=flag_pick_allele, flag_pick_allele_gene=flag_pick_allele_gene, ga4gh_vrs=ga4gh_vrs, gencode_basic=gencode_basic, hgvs=hgvs, mane=mane, merged=merged, minimal=minimal, mirna=mirna, mutfunc=mutfunc, numbers=numbers, per_gene=per_gene, pick=pick, pick_allele=pick_allele, pick_allele_gene=pick_allele_gene, pick_order=pick_order, protein=protein, refseq=refseq, shift_3prime=shift_3prime, shift_genomic=shift_genomic, transcript_id=transcript_id, transcript_version=transcript_version, tsl=tsl, uniprot=uniprot, variant_class=variant_class, vcf_string=vcf_string, xref_refseq=xref_refseq),).json())

# python .\test.py vep-id-post rs56116432 COSM476 homo_sapiens
@app.command()
def vep_id_post(id: List[str],species: str,AncestralAllele=None, Blosum62=None, CADD=None, DisGeNET=None, EVE=None, GO=None, GeneSplicer=None, Geno2MP=None, IntAct=None, LoF=None, Mastermind=None, MaveDB=None, MaxEntScan=None, NMD=None, Phenotypes=None, SpliceAI=None, UTRAnnotator=None, appris=None, callback=None, canonical=None, ccds=None, dbNSFP=None, dbscSNV=None, 
distance=None, domains=None, failed=None, flag_pick=None, flag_pick_allele=None, flag_pick_allele_gene=None, ga4gh_vrs=None, gencode_basic=None, hgvs=None, mane=None, merged=None, minimal=None, mirna=None, mutfunc=None, numbers=None, per_gene=None, pick=None, pick_allele=None, pick_allele_gene=None, pick_order=None, protein=None, refseq=None, shift_3prime=None, shift_genomic=None, transcript_id=None, transcript_version=None, tsl=None, uniprot=None, variant_class=None, vcf_string=None, xref_refseq=None):
  print(requests.post(f"https://rest.ensembl.org/vep/{species}/id", 
                      headers={"Content-Type": "application/json"},
                      params=dict(AncestralAllele=AncestralAllele, Blosum62=Blosum62, CADD=CADD, DisGeNET=DisGeNET, EVE=EVE, GO=GO, GeneSplicer=GeneSplicer, Geno2MP=Geno2MP, IntAct=IntAct, LoF=LoF, Mastermind=Mastermind, MaveDB=MaveDB, MaxEntScan=MaxEntScan, NMD=NMD, Phenotypes=Phenotypes, SpliceAI=SpliceAI, UTRAnnotator=UTRAnnotator, appris=appris, callback=callback, canonical=canonical, ccds=ccds, dbNSFP=dbNSFP, dbscSNV=dbscSNV, distance=distance, domains=domains, failed=failed, flag_pick=flag_pick, flag_pick_allele=flag_pick_allele, flag_pick_allele_gene=flag_pick_allele_gene, ga4gh_vrs=ga4gh_vrs, gencode_basic=gencode_basic, hgvs=hgvs, mane=mane, merged=merged, minimal=minimal, mirna=mirna, mutfunc=mutfunc, numbers=numbers, per_gene=per_gene, pick=pick, pick_allele=pick_allele, pick_allele_gene=pick_allele_gene, pick_order=pick_order, protein=protein, refseq=refseq, shift_3prime=shift_3prime, shift_genomic=shift_genomic, transcript_id=transcript_id, transcript_version=transcript_version, tsl=tsl, uniprot=uniprot, variant_class=variant_class, vcf_string=vcf_string, xref_refseq=xref_refseq),
                      json={"ids": id},).json())

@app.command()
def vep_region_get(allele: str, region: str, species: str,
                   AncestralAllele=None, Blosum62=None, CADD=None, Conservation=None, DisGeNET=None, EVE=None, GO=None, GeneSplicer=None, Geno2MP=None, IntAct=None, LoF=None, Mastermind=None, MaveDB=None, MaxEntScan=None, NMD=None, Phenotypes=None, SpliceAI=None, UTRAnnotator=None, appris=None, callback=None, canonical=None, ccds=None, dbNSFP=None, dbscSNV=None, distance=None, domains=None, failed=None, flag_pick=None, flag_pick_allele=None, flag_pick_allele_gene=None, ga4gh_vrs=None, gencode_basic=None, hgvs=None, mane=None, merged=None, minimal=None, mirna=None, mutfunc=None, numbers=None, per_gene=None, pick=None, pick_allele=None, pick_allele_gene=None, pick_order=None, protein=None, refseq=None, shift_3prime=None, shift_genomic=None, transcript_id=None, transcript_version=None, tsl=None, uniprot=None, variant_class=None, vcf_string=None, xref_refseq=None):
  print(requests.get(f"https://rest.ensembl.org/vep/{species}/region/{region}/{allele}/", headers={"Content-Type": "application/json"},params=dict(AncestralAllele=AncestralAllele, Blosum62=Blosum62, CADD=CADD, Conservation=Conservation, DisGeNET=DisGeNET, EVE=EVE, GO=GO, GeneSplicer=GeneSplicer, Geno2MP=Geno2MP, IntAct=IntAct, LoF=LoF, Mastermind=Mastermind, MaveDB=MaveDB, MaxEntScan=MaxEntScan, NMD=NMD, Phenotypes=Phenotypes, SpliceAI=SpliceAI, UTRAnnotator=UTRAnnotator, appris=appris, callback=callback, canonical=canonical, ccds=ccds, dbNSFP=dbNSFP, dbscSNV=dbscSNV, distance=distance, domains=domains, failed=failed, flag_pick=flag_pick, flag_pick_allele=flag_pick_allele, flag_pick_allele_gene=flag_pick_allele_gene, ga4gh_vrs=ga4gh_vrs, gencode_basic=gencode_basic, hgvs=hgvs, mane=mane, merged=merged, minimal=minimal, mirna=mirna, mutfunc=mutfunc, numbers=numbers, per_gene=per_gene, pick=pick, pick_allele=pick_allele, pick_allele_gene=pick_allele_gene, pick_order=pick_order, protein=protein, refseq=refseq, shift_3prime=shift_3prime, shift_genomic=shift_genomic, transcript_id=transcript_id, transcript_version=transcript_version, tsl=tsl, uniprot=uniprot, variant_class=variant_class, vcf_string=vcf_string, xref_refseq=xref_refseq),).json())

#  python .\test.py vep-region-post 21 26960070 rs116645811 G A . . . 21 26965148 rs1135638 G A . . . homo_sapiens
@app.command()
def vep_region_post(variant: List[str],species: str,
                    AncestralAllele=None, Blosum62=None, CADD=None, DisGeNET=None, EVE=None, GO=None, GeneSplicer=None, Geno2MP=None, IntAct=None, LoF=None, Mastermind=None, MaveDB=None, MaxEntScan=None, NMD=None, Phenotypes=None, SpliceAI=None, UTRAnnotator=None, appris=None, callback=None, canonical=None, ccds=None, dbNSFP=None, dbscSNV=None, distance=None, domains=None, failed=None, flag_pick=None, flag_pick_allele=None, flag_pick_allele_gene=None, ga4gh_vrs=None, gencode_basic=None, hgvs=None, mane=None, merged=None, minimal=None, mirna=None, mutfunc=None, numbers=None, per_gene=None, pick=None, pick_allele=None, pick_allele_gene=None, pick_order=None, protein=None, refseq=None, shift_3prime=None, shift_genomic=None, transcript_id=None, transcript_version=None, tsl=None, uniprot=None, variant_class=None, vcf_string=None, xref_refseq=None):
  print(requests.post(f"https://rest.ensembl.org/vep/{species}/region", 
                      headers={"Content-Type": "application/json"},
                      params=dict(AncestralAllele=AncestralAllele, Blosum62=Blosum62, CADD=CADD, DisGeNET=DisGeNET, EVE=EVE, GO=GO, GeneSplicer=GeneSplicer, Geno2MP=Geno2MP, IntAct=IntAct, LoF=LoF, Mastermind=Mastermind, MaveDB=MaveDB, MaxEntScan=MaxEntScan, NMD=NMD, Phenotypes=Phenotypes, SpliceAI=SpliceAI, UTRAnnotator=UTRAnnotator, appris=appris, callback=callback, canonical=canonical, ccds=ccds, dbNSFP=dbNSFP, dbscSNV=dbscSNV, distance=distance, domains=domains, failed=failed, flag_pick=flag_pick, flag_pick_allele=flag_pick_allele, flag_pick_allele_gene=flag_pick_allele_gene, ga4gh_vrs=ga4gh_vrs, gencode_basic=gencode_basic, hgvs=hgvs, mane=mane, merged=merged, minimal=minimal, mirna=mirna, mutfunc=mutfunc, numbers=numbers, per_gene=per_gene, pick=pick, pick_allele=pick_allele, pick_allele_gene=pick_allele_gene, pick_order=pick_order, protein=protein, refseq=refseq, shift_3prime=shift_3prime, shift_genomic=shift_genomic, transcript_id=transcript_id, transcript_version=transcript_version, tsl=tsl, uniprot=uniprot, variant_class=variant_class, vcf_string=vcf_string, xref_refseq=xref_refseq),
                      json={"variants": variant},).json())

# Variation----87
@app.command()
def variant_recoder(id: str, species: str,callback=None, failed=None, fields=None, ga4gh_vrs=None, gencode_basic=None, minimal=None, var_synonyms=None, vcf_string=None):
  print(requests.get(f"https://rest.ensembl.org/variant_recoder/{species}/{id}", headers={"Content-Type": "application/json"},params=dict(callback=callback, failed=failed, fields=fields, ga4gh_vrs=ga4gh_vrs, gencode_basic=gencode_basic, minimal=minimal, var_synonyms=var_synonyms, vcf_string=vcf_string),).json())

# python .\test.py variant-recoder-post rs56116432 rs1042779 homo_sapiens
@app.command()
def variant_recoder_post(id: List[str],species: str,callback=None, failed=None, fields=None, ga4gh_vrs=None, gencode_basic=None, minimal=None, var_synonyms=None, vcf_string=None):      
  print(requests.post(f"https://rest.ensembl.org/variant_recoder/{species}", headers={"Content-Type": "application/json"},params=dict(callback=callback, failed=failed, fields=fields, ga4gh_vrs=ga4gh_vrs, gencode_basic=gencode_basic, minimal=minimal, var_synonyms=var_synonyms, vcf_string=vcf_string),json={"ids": id},).json())

@app.command()
def variation_id(id: str, species: str,callback=None, genotypes=None, genotyping_chips=None, phenotypes=None, pops=None, population_genotypes=None):
  print(requests.get(f"https://rest.ensembl.org/variation/{species}/{id}", headers={"Content-Type": "application/json"},params=dict(callback=callback, genotypes=genotypes, genotyping_chips=genotyping_chips, phenotypes=phenotypes, pops=pops, population_genotypes=population_genotypes),).json())

@app.command()
def variation_pmcid_get(pmcid: str, species: str,callback=None):
  print(requests.get(f"https://rest.ensembl.org/variation/{species}/pmcid/{pmcid}", headers={"Content-Type": "application/json"},params=dict(callback=callback),).json())

@app.command()
def variation_pmid_get(pmid: str, species: str,callback=None):
  print(requests.get(f"https://rest.ensembl.org/variation/{species}/pmid/{pmid}", headers={"Content-Type": "application/json"},params=dict(callback=callback),).json())

# python .\test.py variation-post rs56116432 COSM476 homo_sapiens
@app.command()
def variation_post(id: List[str],species: str,callback=None, genotypes=None, phenotypes=None, pops=None, population_genotypes=None):
  print(requests.post(f"https://rest.ensembl.org/variation/{species}/", headers={"Content-Type": "application/json"},params=dict(callback=callback, genotypes=genotypes, phenotypes=phenotypes, pops=pops, population_genotypes=population_genotypes),json={"ids": id},).json())

# Variation GA4GH----93
# python .\test.py beacon-get
@app.command()
def beacon_get(callback=None):
  print(requests.get(f"https://rest.ensembl.org/ga4gh/beacon", headers={"Content-Type": "application/json"},params=dict(callback=callback),).json())

# python .\test.py beacon-query-get C GRCh38 '__VAR(GA4GH_beacon_end)__' G 9 22125503 '__VAR(GA4GH_beacon_variantType)__'
# 运行有问题--94
@app.command()
def beacon_query_get(alternateBases: str, assemblyId: str, end: str, referenceBases: str, referenceName: str, start: str, variantType: str,callback=None, datasetIds=None, includeResultsetResponses=None):
  print(requests.get(f"https://rest.ensembl.org/ga4gh/beacon/query", headers={"Content-Type": "application/json"},params=dict(callback=callback, datasetIds=datasetIds, includeResultsetResponses=includeResultsetResponses),).json())

# python .\test.py beacon-query-post --referencename 9
@app.command()
def beacon_query_post(alternateBases=None, assemblyId=None, end=None, referenceBases=None, referenceName=None, start=None, variantType=None,callback=None, datasetIds=None, includeResultsetResponses=None):
  print(requests.post(f"https://rest.ensembl.org/ga4gh/beacon/query", headers={"Content-Type": "application/json"},
                      params=dict(alternateBases=alternateBases, assemblyId=assemblyId, end=end, referenceBases=referenceBases, referenceName=referenceName, start=start, variantType=variantType,
                        callback=callback, datasetIds=datasetIds, includeResultsetResponses=includeResultsetResponses),
                      json={"alternateBases": alternateBases,"assemblyId":assemblyId,"referenceName":referenceName,"start":start,"referenceBases":referenceBases,"end":end,"variantType":variantType},).json())

@app.command()
def features_id(id: str,callback=None):
  print(requests.get(f"https://rest.ensembl.org/ga4gh/features/{id}", headers={"Content-Type": "application/json"},params=dict(callback=callback),).json())

# python .\test.py features-post --parentid ENST00000408937.7  --featuresetid Ensembl --referencename X  --start 197859 --end 220023
@app.command()
def features_post(end=None, referenceName=None, start=None,callback=None, featureTypes=None, featuresetId=None, pageSize=None, pageToken=None, parentId=None):
  print(requests.post(f"https://rest.ensembl.org/ga4gh/features/search", headers={"Content-Type": "application/json"},
                      params=dict(end=end, referenceName=referenceName, start=start,callback=callback, featureTypes=featureTypes, featuresetId=featuresetId, pageSize=pageSize, pageToken=pageToken, parentId=parentId),
                      json={"pageSize": pageSize,"parentId":parentId,"featuresetId":featuresetId,"featureTypes":featureTypes,"referenceName":referenceName,"start":start,"end":end},).json())


# python .\test.py gacallset --variantsetid 1 --pagesize 2
@app.command()
def gacallSet(variantSetId=None,callback=None, name=None, pageSize=None, pageToken=None):  
  print(requests.post(f"https://rest.ensembl.org/ga4gh/callsets/search", headers={"Content-Type": "application/json"},
                      params=dict(variantSetId=variantSetId,callback=callback, name=name, pageSize=pageSize, pageToken=pageToken),
                      json={"variantSetId":variantSetId,"name":name,"pageToken":pageToken,"pageSize":pageSize},).json())

# python .\test.py gacallset-id 1
@app.command()
def gacallset_id(id: str,callback=None):
  print(requests.get(f"https://rest.ensembl.org/ga4gh/callsets/{id}", headers={"Content-Type": "application/json"},params=dict(callback=callback),).json())

# python .\test.py gadataset --pagesize 3
@app.command()
def gadataset(callback=None, pageSize=None, pageToken=None):
  print(requests.post(f"https://rest.ensembl.org/ga4gh/datasets/search", headers={"Content-Type": "application/json"},params=dict(callback=callback, pageSize=pageSize, pageToken=pageToken),
                      json={"pageToken": pageToken,"pageSize":pageSize},).json())

# python .\test.py gadataset-id 6e340c4d1e333c7a676b1710d2e3953c
@app.command()
def gadataset_id(id: str,callback=None):
  print(requests.get(f"https://rest.ensembl.org/ga4gh/datasets/{id}", headers={"Content-Type": "application/json"},params=dict(callback=callback),).json())

# python .\test.py gafeatureset --datasetid Ensembl  --pagesize 2
@app.command()
def gafeatureset(datasetId=None,callback=None, pageSize=None, pageToken=None):
  print(requests.post(f"https://rest.ensembl.org/ga4gh/featuresets/search", headers={"Content-Type": "application/json"},
                      params=dict(datasetId=datasetId,callback=callback, pageSize=pageSize, pageToken=pageToken),
                      json={"datasetId":datasetId,"pageToken":pageToken,"pageSize":pageSize},).json())

# python .\test.py gafeatureset-id Ensembl
@app.command()
def gafeatureset_id(id: str,callback=None):
  print(requests.get(f"https://rest.ensembl.org/ga4gh/featuresets/{id}", headers={"Content-Type": "application/json"},params=dict(callback=callback),).json())

@app.command()
def gavariant_id(id: str,callback=None):
  print(requests.get(f"https://rest.ensembl.org/ga4gh/variants/{id}", headers={"Content-Type": "application/json"},params=dict(callback=callback),).json())

# 有问题---105
@app.command()
def gavariantannotations(variantAnnotationSetId=None,callback=None, effects=None, end=None, pageSize=None, pageToken=None, referenceId=None, referenceName=None, start=None):
  print(requests.post(f"https://rest.ensembl.org/ga4gh/variantannotations/search", headers={"Content-Type": "application/json"},
                      params=dict(variantAnnotationSetId=variantAnnotationSetId,callback=callback, effects=effects, end=end, pageSize=pageSize, pageToken=pageToken, referenceId=referenceId, referenceName=referenceName, start=start),
                      json={"variantAnnotationSetId":variantAnnotationSetId,"pageSize":pageSize,"referenceId":referenceId,"referenceName":referenceName,"start":start,"end":end},).json())
# python .\test.py gavariants --variantsetid 1  --referencename 22 --end 17671934 --start 17190024
@app.command()
def gavariants(end=None, referenceName=None, start=None, variantSetId=None,callSetIds=None, callback=None, pageSize=None, pageToken=None):
  print(requests.post(f"https://rest.ensembl.org/ga4gh/variants/search", headers={"Content-Type": "application/json"},
                      params=dict(end=end, referenceName=referenceName, start=start, variantSetId=variantSetId,callSetIds=callSetIds, callback=callback, pageSize=pageSize, pageToken=pageToken),
                      json={"end":end,"referenceName":referenceName,"variantSetId":variantSetId,"callSetIds":callSetIds,"start":start,"pageToken":pageToken,"pageSize":pageSize},).json())
#  python .\test.py gavariantset --datasetid 6e340c4d1e333c7a676b1710d2e3953c
@app.command()
def gavariantset(datasetId=None,callback=None, pageSize=None, pageToken=None):
  print(requests.post(f"https://rest.ensembl.org/ga4gh/variantsets/search", headers={"Content-Type": "application/json"},
                      params=dict(datasetId=datasetId,callback=callback, pageSize=pageSize, pageToken=pageToken),
                      json={"datasetId": datasetId,"pageSize":pageSize,"pageToken":pageToken},).json())

@app.command()
def gavariantset_id(id: str,callback=None):
  print(requests.get(f"https://rest.ensembl.org/ga4gh/variantsets/{id}", headers={"Content-Type": "application/json"},params=dict(callback=callback),).json())

# python .\test.py references  --referencesetid GRCh38  --pagesize 10
@app.command()
def references(referenceSetId=None,accession=None, callback=None, md5checksum=None, pageSize=None, pageToken=None):
  print(requests.post(f"https://rest.ensembl.org/ga4gh/references/search", headers={"Content-Type": "application/json"},
                      params=dict(referenceSetId=referenceSetId,accession=accession, callback=callback, md5checksum=md5checksum, pageSize=pageSize, pageToken=pageToken),
                      json={"referenceSetId":referenceSetId,"md5checksum":md5checksum,"accession":accession,"pageSize":pageSize,"pageToken":pageToken},).json())

@app.command()
def references_id(id: str,callback=None):
  print(requests.get(f"https://rest.ensembl.org/ga4gh/references/{id}", headers={"Content-Type": "application/json"},params=dict(callback=callback),).json())

# python .\test.py referencesets --accession 1
@app.command()
def referenceSets(accession=None, callback=None, pageSize=None, pageToken=None):
  print(requests.post(f"https://rest.ensembl.org/ga4gh/referencesets/search", headers={"Content-Type": "application/json"},params=dict(accession=accession, callback=callback, pageSize=pageSize, pageToken=pageToken),
                      json={},).json())

# python .\test.py referencesets-id GRCh38?
@app.command()
def referenceSets_id(id: str,callback=None):
  print(requests.get(f"https://rest.ensembl.org/ga4gh/referencesets/{id}", headers={"Content-Type": "application/json"},params=dict(callback=callback),).json())

# python .\test.py variantannotationset --variantsetid Ensembl
@app.command()
def VariantAnnotationSet(variantSetId=None,callback=None, pageSize=None, pageToken=None):  
  print(requests.post(f"https://rest.ensembl.org/ga4gh/variantannotationsets/search", headers={"Content-Type": "application/json"},
                      params=dict(variantSetId=variantSetId,callback=callback, pageSize=pageSize, pageToken=pageToken),
                      json={"variantSetId": variantSetId,"pageSize":pageSize,"pageToken":pageToken},).json())

@app.command()
def VariantAnnotationSet_id(id: str,callback=None):
  print(requests.get(f"https://rest.ensembl.org/ga4gh/variantannotationsets/{id}", headers={"Content-Type": "application/json"},params=dict(callback=callback),).json())

if __name__ == "__main__":
    app()
