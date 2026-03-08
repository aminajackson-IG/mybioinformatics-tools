import csv
from Bio import SeqIO


def genbank_to_csv(gb_file, output_csv):
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Accession", "Organism", "Length", "Genes", "CDS_Locations"])

        for record in SeqIO.parse(gb_file, "genbank"):
            genes = []
            cds_locs = []

            for feature in record.features:
                if feature.type == "gene":
                    gene_name = feature.qualifiers.get("gene", ["unknown"])[0]
                    genes.append(f"{gene_name}({feature.location})")

                if feature.type == "CDS":
                    # CDS often contains protein_id or product info
                    product = feature.qualifiers.get("product", [""])[0]
                    cds_locs.append(f"{product}[{feature.location}]")

            writer.writerow([
                record.id,
                record.annotations.get("source", "N/A"),
                len(record.seq),
                "; ".join(genes),
                "; ".join(cds_locs)
            ])

    print(f"Extraction complete. Data saved to {output_csv}")


# if you are not running in the same directory as the file, provide a full path.
# You  can rename records.csv to anything of your choosing

genbank_to_csv(gb_file="records.gb", output_csv="results.csv")
