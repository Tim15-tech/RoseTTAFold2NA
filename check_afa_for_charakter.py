# fhla3x/fhla.afa
# OxysHfqFhla_pred/fhla.afa
def run():
    with open ("OxysHfqFhla_pred/fhla.afa", 'r') as a3m:
        counter = 0
        for line in a3m:
            counter += 1
            if line[0] != '>':
                for i in line:
                    if i not in ['A', 'C', 'G', 'U', '-', 'N', '0', '\n']:
                        print("i:",i, "counter:", counter)

if __name__ == "__main__":
    run()
