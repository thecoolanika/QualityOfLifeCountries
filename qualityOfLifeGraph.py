from bokeh.plotting import figure, show
import math

f = open("customQuality.txt", "r")

life = {}

for line in f:
  line = line.strip()
  (country, quality) = line.split(",")
  life[country] = float(quality)

allCountries = list(life.keys())
allQualities = list(life.values())

countryData = []
qualityData = []

def ordering(key):
  return life[key]
allCountries.sort(key = ordering, reverse = True)
countryData = allCountries[:20]
for country in countryData:
  qualityData.append(life[country])


g = figure(title="Qualities of Life by Country - regular")

colors = ['#CD8987','#CD8D8A','#CD958F','#CD9C95','#CDA59C','#CDACA1','#CDADA3','#CDC1BF','#CDC7C7','#CDCACC','#CDC8C8','#CDCED1','#CDD3D9','#CDD4DA','#CDD6DD','#CCE2E7','#CCEEF2','#CCF8FB','#CCFAFD','#CCFBFE']

for i in range(20):
  g.hbar(i + 1, .95, qualityData[int(19-i)], 0, color = colors[i])
  g.text(.3, i+.75, [str(countryData[19-i]) +" - " + str(qualityData[19-i])], text_font_size = "10.5pt")
show(g)
