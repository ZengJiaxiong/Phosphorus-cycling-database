import argparse
from Bio import SeqIO
parser = argparse.ArgumentParser(description='Extract sequences')
parser.add_argument('-m','--Map',help='ORF2gene file')
parser.add_argument('-f','--fasta',help='file using to extract')
parser.add_argument('-o','--out',help='output')
args = parser.parse_args()

def extract(Map, fasta, out):
    filename = Map.split('.')[0]
    print('Processing ' + filename)
    fastadic = {}
    for record in SeqIO.parse (fasta,'fasta'):
        fastadic['>' + str(record.id)] = str(record.seq).strip()
    output = open (out + '.Extracted.fa','w')
    with open (Map, 'r') as MAP:
        for line in MAP:
            id = '>' + line.split('\t')[0].strip()
            output.write(id + '\n')
            output.write(fastadic[id] + '\n')
    output.close()
    print(filename + ' finished.')

if __name__ == '__main__':
    extract(args.Map, args.fasta, args.out)