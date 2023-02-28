from string import ascii_uppercase

#OBS.:ADD PARA NUM COM PARTES DECIMAIS
def conv(n, b):
      print()
      d = -1
      nold = n
      num = ""
      while d != 0:
            d = n // b
            r = n % b
            num += numChecker(r)
            print(f"d = {d} | r = {r}")
            n = d
      print(f"\nConversão de {nold} para a base {b}: {num[::-1]}")

def numChecker(val):
      if 10 <= val < 36:
            return ascii_uppercase[val - 10]
      else:
            return str(val)

def main():
      conv(int(input("\nDigite o número: ")), int(input("Digite a base: ")))

if __name__ == "__main__":
      main()
