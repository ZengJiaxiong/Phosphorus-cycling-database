import argparse
parser = argparse.ArgumentParser(description='filter')
parser.add_argument('-s','--identity',help='identity cutoff')
parser.add_argument('-cov','--coverage',help='coverage cutoff')
parser.add_argument('-hit','--hitlength',help='hitlength')
parser.add_argument('-blast','--blastx',help='blast file')
args = parser.parse_args()

id2genemap={}
with open ('$yourpath/id2genemap.txt','r') as IDfile:
    for id in IDfile:
        id2genemap[id.split('\t')[0].strip()] = id.split('\t')[1].strip()

def filter(blastx,identity,coverage,hitlength):
    output = open (blastx.split('.')[0]+'ORF2Pgene.txt','w')
    identity = float(identity)
    coverage = float(coverage)
    hitlength = int(hitlength)
    filename = blastx.split('.')[0]
    for line in open (blastx,'r'):
        originalid = float(line.split('\t')[2])
        originalcov = float(line.split('\t')[3])
        originalhit = int(line.split('\t')[4])
        if originalid >= identity and originalcov >= coverage and originalhit >= hitlength:
            key = line.split('\t')[1]
            try:
                output.write(line.split('\t')[0] + '\t' + id2genemap[key] + '\n')
            except KeyError:
                continue
    output.close()

if __name__ == '__main__':
    print('processing: ' + args.blastx)
    filter(args.blastx,args.identity,args.coverage,args.hitlength)