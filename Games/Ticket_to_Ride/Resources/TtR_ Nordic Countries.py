# Get this figure: fig = py.get_figure("https://chart-studio.plotly.com/~Nintendaro/1/")
# Get this figure's data: data = py.get_figure("https://chart-studio.plotly.com/~Nintendaro/1/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="TtR: Nordic Countries", fileopt="extend")

# Get figure documentation: https://chart-studio.plotly.com/python/get-requests/
# Add data documentation: https://chart-studio.plotly.com/python/file-options/

# If you're using unicode in your file, you may need to specify the encoding.
# You can reproduce this figure in Python with the following code!

# Learn about API authentication here: https://chart-studio.plotly.com/python/getting-started
# Find your api_key here: https://chart-studio.plotly.com/settings/api

import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('username', 'api_key')
trace1 = {
  "line": {
    "color": "rgb(208, 36, 53)", 
    "width": 4
  }, 
  "meta": {"columnNames": {
      "lat": "A", 
      "lon": "B", 
      "text": "C"
    }}, 
  "mode": "lines", 
  "name": "8-10", 
  "type": "scattergeo", 
  "lat": ["63.826294802794955", "65.82529822480663", "", "59.27453941804889", "59.912345845293885", "", "62.39027421134211", "63.826294802794955", "", "62.39027421134211", "59.27453941804889", "", "55.675499027107264", "57.711569308929455"], 
  "lon": ["20.261872288582808", "21.68354372704494", "", "15.209318701855853", "10.757642160826423", "", "17.30282447683423", "20.261872288582808", "", "17.30282447683423", "15.209318701855853", "", "12.570818866830635", "11.98031871187112"], 
  "text": ["Ålborg", "Åndalsnes", "Århus", "Bergen", "Boden", "Gōteborg", "Helsinki", "Honningsvåg", "Imatra", "Kajaani", "Karlskrona", "Kirkenes", "Kiruna", "København", "Kristiansand", "Kuopio", "Lahti", "Lieksa", "Lillehammer", "Mo I Rana", "Murmansk", "Narvik", "Norrköping", "Örebro", "Oslo", "Östersund", "Oulu", "Rovaniemi", "Stavanger", "Stockholm", "Sundsvall", "Tallinn", "Tampere", "Tornio", "Tromsø", "Trondheim", "Turku", "Umeå", "Vaasa", "Aberdeen", "Aberystwyth", "Barrow", "Belfast", "Birmingham", "Brighton", "Bristol", "Cambridge", "Cardiff", "Carlisle", "Carmarthen", "Cork", "Dover", "Dublin", "Dundalk", "Dundee", "Edinburgh", "Fort William", "France (1)", "France (2)", "Galway", "Glasgow", "Holyhead", "Hull", "Inverness", "Ipswich", "Leeds", "Limerick", "Liverpool", "Llandrindod Wells", "London", "Londonderry", "Manchester", "New York", "Newcastle", "Northampton", "Norwich", "Nottingham", "Penzance", "Plymouth", "Reading", "Rosslare", "Sligo", "Southampton", "Stornoway", "Stranraer", "Tullamore", "Ullapool", "Wick"], 
  "visible": True, 
  "hoverinfo": "none", 
  "hoverlabel": {"namelength": 0}, 
  "connectgaps": False, 
  "textposition": "middle center", 
  "hovertemplate": ""
}
trace2 = {
  "line": {
    "color": "rgb(244, 190, 73)", 
    "width": 4
  }, 
  "meta": {"columnNames": {
      "lat": "A", 
      "lon": "B"
    }}, 
  "mode": "lines", 
  "name": "6-7", 
  "type": "scattergeo", 
  "lat": ["59.328489928951704", "62.39027421134211", None, "59.328489928951704", "60.17402178556654"], 
  "lon": ["18.072681047373948", "17.30282447683423", None, "18.072681047373948", "24.94860979008052"], 
  "visible": True, 
  "hoverinfo": "none"
}
trace3 = {
  "line": {
    "color": "rgb(255, 251, 29)", 
    "width": 4
  }, 
  "meta": {"columnNames": {
      "lat": "A", 
      "lon": "B"
    }}, 
  "mode": "lines", 
  "name": "4-5", 
  "type": "scattergeo", 
  "lat": ["65.82529822480663", "67.85639904751547", "", "58.58771819476748", "59.328489928951704", "", "58.58771819476748", "57.711569308929455", "", "59.27453941804889", "59.328489928951704", "", "62.39027421134211", "63.09490958440979", "", "60.39260758540451", "59.912345845293885", "", "68.43847778002933", "69.6676915048554", "", "68.43847778002933", "67.85639904751547", "", "66.31406946239973", "63.430430273629675", "", "59.27453941804889", "57.711569308929455", "", "61.11547314339694", "59.912345845293885", "", "61.11547314339694", "63.430430273629675"], 
  "lon": ["21.68354372704494", "20.224842628607313", "", "16.200678280512555", "18.072681047373948", "", "16.200678280512555", "11.98031871187112", "", "15.209318701855853", "18.072681047373948", "", "17.30282447683423", "21.621650135612082", "", "5.304168608534294", "10.757642160826423", "", "17.42799628993811", "18.925440091913607", "", "17.42799628993811", "20.224842628607313", "", "14.141205731087945", "10.401607045729529", "", "15.209318701855853", "11.98031871187112", "", "10.466400932038008", "10.757642160826423", "", "10.466400932038008", "10.401607045729529"], 
  "visible": True, 
  "hoverinfo": "none"
}
trace4 = {
  "line": {
    "color": "rgb(86, 188, 221)", 
    "width": 4
  }, 
  "meta": {"columnNames": {
      "lat": "A", 
      "lon": "B"
    }}, 
  "mode": "lines", 
  "name": "3", 
  "type": "scattergeo", 
  "lat": ["63.826294802794955", "63.09490958440979", None, "61.50009939885583", "63.09490958440979", None, "60.45191561645681", "59.328489928951704", None, "59.912345845293885", "58.160558760539054", None, "59.912345845293885", "57.711569308929455", None, "60.9844075943206", "60.17402178556654", None, "60.9844075943206", "62.896357241162896"], 
  "lon": ["20.261872288582808", "21.621650135612082", None, "23.7272646988628", "21.621650135612082", None, "22.27638581662958", "18.072681047373948", None, "10.757642160826423", "8.01397732186328", None, "10.757642160826423", "11.98031871187112", None, "25.663365207287942", "24.94860979008052", None, "25.663365207287942", "27.687452551322547"], 
  "visible": True, 
  "hoverinfo": "none"
}
trace5 = {
  "line": {
    "color": "rgb(175, 132, 223)", 
    "width": 4
  }, 
  "meta": {"columnNames": {
      "lat": "A", 
      "lon": "B"
    }}, 
  "mode": "lines", 
  "name": "2", 
  "type": "scattergeo", 
  "lat": ["69.6676915048554", "70.98239250260706", None, "66.31406946239973", "68.43847778002933", None, "60.17402178556654", "61.50009939885583", None, "60.17402178556654", "61.17217169265381", None, "62.56747484421721", "60.39260758540451", "", "58.96951723462432", "58.160558760539054", None, "63.430430273629675", "62.56747484421721", None, "62.39027421134211", "63.17672346379236", None, "65.82529822480663", "65.84711630607462", None, "63.09490958440979", "65.03212114675763", None, "62.896357241162896", "61.17217169265381", None, "62.896357241162896", "63.51156532644846", None, "62.896357241162896", "65.03212114675763", None, "57.048838126073115", "56.16221213518473", None, "57.048838126073115", "57.711569308929455"], 
  "lon": ["18.925440091913607", "25.972728576755586", None, "14.141205731087945", "17.42799628993811", None, "24.94860979008052", "23.7272646988628", None, "24.94860979008052", "28.765364385611868", None, "7.687042937277424", "5.304168608534294", "", "5.73251963440812", "8.01397732186328", None, "10.401607045729529", "7.687042937277424", None, "17.30282447683423", "14.642541584029566", None, "21.68354372704494", "24.15246864892743", None, "21.621650135612082", "25.524905196664", None, "27.687452551322547", "28.765364385611868", None, "27.687452551322547", "30.018509865495975", None, "27.687452551322547", "25.524905196664", None, "9.922223605516605", "10.203944724356772", None, "9.922223605516605", "11.98031871187112"], 
  "visible": True, 
  "hoverinfo": "none"
}
trace6 = {
  "line": {
    "color": "rgb(254, 251, 254)", 
    "width": 4
  }, 
  "meta": {"columnNames": {
      "lat": "A", 
      "lon": "B", 
      "text": "C"
    }}, 
  "mode": "lines", 
  "name": "0-1", 
  "type": "scattergeo", 
  "lat": ["65.03212114675763", "66.53353021727351", None, "69.72704104672448", "66.53353021727351", None, "63.51156532644846", "68.973603209738", None, "69.72704104672448", "68.973603209738", None, "69.72704104672448", "70.98239250260706", None, "63.430430273629675", "63.17672346379236", None, "60.39260758540451", "58.96951723462432", None, "62.56747484421721", "61.11547314339694", None, "65.84711630607462", "65.03212114675763", None, "65.84711630607462", "66.53353021727351", None, "59.43634291532583", "59.328489928951704", None, "59.43634291532583", "60.17402178556654", None, "61.50009939885583", "60.45191561645681", None, "61.50009939885583", "60.9844075943206", None, "62.896357241162896", "63.09490958440979", None, "62.896357241162896", "64.22155420807493", None, "57.048838126073115", "59.912345845293885", None, "57.048838126073115", "58.160558760539054", None, "55.675499027107264", "56.161150630104586", None, "55.675499027107264", "56.16221213518473", None, "60.45191561645681", "60.17402178556654", None, "58.58771819476748", "56.161150630104586", None, "58.58771819476748", "59.27453941804889", None, "60.9844075943206", "61.17217169265381", None, "64.22155420807493", "65.03212114675763", None, "64.22155420807493", "63.51156532644846"], 
  "lon": ["25.524905196664", "25.745848750170378", None, "30.04613179244278", "25.745848750170378", None, "30.018509865495975", "33.087769368194586", None, "30.04613179244278", "33.087769368194586", None, "30.04613179244278", "25.972728576755586", None, "10.401607045729529", "14.642541584029566", None, "5.304168608534294", "5.73251963440812", None, "7.687042937277424", "10.466400932038008", None, "24.15246864892743", "25.524905196664", None, "24.15246864892743", "25.745848750170378", None, "24.766385293412434", "18.072681047373948", None, "24.766385293412434", "24.94860979008052", None, "23.7272646988628", "22.27638581662958", None, "23.7272646988628", "25.663365207287942", None, "27.687452551322547", "21.621650135612082", None, "27.687452551322547", "27.729347946342923", None, "9.922223605516605", "10.757642160826423", None, "9.922223605516605", "8.01397732186328", None, "12.570818866830635", "15.589838668957023", None, "12.570818866830635", "10.203944724356772", None, "22.27638581662958", "24.94860979008052", None, "16.200678280512555", "15.589838668957023", None, "16.200678280512555", "15.209318701855853", None, "25.663365207287942", "28.765364385611868", None, "27.729347946342923", "25.524905196664", None, "27.729347946342923", "30.018509865495975"], 
  "text": ["Ålborg", "Åndalsnes", "Århus", "Bergen", "Boden", "Gōteborg", "Helsinki", "Honningsvåg", "Imatra", "Kajaani", "Karlskrona", "Kirkenes", "Kiruna", "København", "Kristiansand", "Kuopio", "Lahti", "Lieksa", "Lillehammer", "Mo I Rana", "Murmansk", "Narvik", "Norrköping", "Örebro", "Oslo", "Östersund", "Oulu", "Rovaniemi", "Stavanger", "Stockholm", "Sundsvall", "Tallinn", "Tampere", "Tornio", "Tromsø", "Trondheim", "Turku", "Umeå", "Vaasa", "Aberdeen", "Aberystwyth", "Barrow", "Belfast", "Birmingham", "Brighton", "Bristol", "Cambridge", "Cardiff", "Carlisle", "Carmarthen", "Cork", "Dover", "Dublin", "Dundalk", "Dundee", "Edinburgh", "Fort William", "France (1)", "France (2)", "Galway", "Glasgow", "Holyhead", "Hull", "Inverness", "Ipswich", "Leeds", "Limerick", "Liverpool", "Llandrindod Wells", "London", "Londonderry", "Manchester", "New York", "Newcastle", "Northampton", "Norwich", "Nottingham", "Penzance", "Plymouth", "Reading", "Rosslare", "Sligo", "Southampton", "Stornoway", "Stranraer", "Tullamore", "Ullapool", "Wick"], 
  "visible": True, 
  "textfont": {
    "size": 10, 
    "color": "rgb(16, 16, 17)", 
    "family": "Arial"
  }, 
  "hoverinfo": "none", 
  "textposition": "top center"
}
trace7 = {
  "meta": {"columnNames": {
      "lat": "A", 
      "lon": "B", 
      "text": "C", 
      "marker": {"size": "E"}, 
      "textposition": "D"
    }}, 
  "mode": "markers", 
  "name": "Cities", 
  "type": "scattergeo", 
  "lat": ["57.048838126073115", "62.56747484421721", "56.16221213518473", "60.39260758540451", "65.82529822480663", "57.711569308929455", "60.17402178556654", "70.98239250260706", "61.17217169265381", "64.22155420807493", "56.161150630104586", "69.72704104672448", "67.85639904751547", "55.675499027107264", "58.160558760539054", "62.896357241162896", "60.9844075943206", "63.51156532644846", "61.11547314339694", "66.31406946239973", "68.973603209738", "68.43847778002933", "58.58771819476748", "59.27453941804889", "59.912345845293885", "63.17672346379236", "65.03212114675763", "66.53353021727351", "58.96951723462432", "59.328489928951704", "62.39027421134211", "59.43634291532583", "61.50009939885583", "65.84711630607462", "69.6676915048554", "63.430430273629675", "60.45191561645681", "63.826294802794955", "63.09490958440979", "57.149703501396736", "52.41538395316434", "54.10898120237651", "54.59624433819916", "52.486703588781516", "50.8223395340059", "51.45583992720376", "52.196214168983325", "51.484256453860205", "54.89227570867174", "51.85781129629228", "51.89809484577351", "51.127677706413735", "53.3508563016254", "53.99709555010845", "56.4628148386432", "55.953887423353336", "56.81965539202142", "", "", "53.27546679351384", "55.86806633226628", "53.30960834667442", "53.768574685826536", "57.4776813177482", "52.05719476806426", "53.80009440880148", "52.66338894246145", "53.40797098651094", "52.241351387097254", "51.505025293302154", "54.99582822638326", "53.47936876038216", "", "54.98067832990718", "52.23723275673263", "52.63097370136248", "52.955235015255575", "50.119018739310064", "50.374184748779925", "51.45413464335409", "52.254317922253996", "54.27684696325877", "50.90948402827984", "58.209217659645596", "54.90279317719651", "53.275498399825985", "57.895691343089695", "58.43912655563484"], 
  "lon": ["9.922223605516605", "7.687042937277424", "10.203944724356772", "5.304168608534294", "21.68354372704494", "11.98031871187112", "24.94860979008052", "25.972728576755586", "28.765364385611868", "27.729347946342923", "15.589838668957023", "30.04613179244278", "20.224842628607313", "12.570818866830635", "8.01397732186328", "27.687452551322547", "25.663365207287942", "30.018509865495975", "10.466400932038008", "14.141205731087945", "33.087769368194586", "17.42799628993811", "16.200678280512555", "15.209318701855853", "10.757642160826423", "14.642541584029566", "25.524905196664", "25.745848750170378", "5.73251963440812", "18.072681047373948", "17.30282447683423", "24.766385293412434", "23.7272646988628", "24.15246864892743", "18.925440091913607", "10.401607045729529", "22.27638581662958", "20.261872288582808", "21.621650135612082", "-2.0965980744914767", "-4.083176870318161", "-3.2203503010410097", "-5.926978092141603", "-1.8859545654469532", "-0.1362311113117233", "-2.5883168791363715", "0.13370342730019355", "-3.16763045779101", "-2.9323048218471928", "-4.312676112031723", "-8.474725538858953", "1.3136915736517523", "-6.2601336995931", "-6.405233799021794", "-2.973015423643524", "-3.1820527769166294", "-5.10426401682841", "", "", "-9.049092363889526", "-4.260620535940629", "-4.635181706986051", "-0.3261517783015", "-4.225793476977911", "1.1512910529776215", "-1.5518709815487344", "-8.614969725112568", "-2.9819867411301058", "-3.376084596632633", "-0.11877522664037725", "-7.30615295216364", "-2.243378099888314", "", "-1.6204536363116053", "-0.8882971703911592", "1.293701251701316", "-1.1563313993650752", "-5.537295584310239", "-4.142441723341992", "-0.9792418464399548", "-6.317813248420872", "-8.476352423781833", "-1.4078750094327217", "-6.384592603029308", "-5.02496617091827", "-7.495557493846783", "-5.1608089015686724", "-3.0935897056458237"], 
  "marker": {
    "line": {"width": 1}, 
    "meta": {"columnNames": {"size": "E"}}, 
    "color": "rgb(5, 4, 0)", 
    "sizeref": 0.06666666666666667, 
    "size": ["2", "1", "1", "6", "2", "3", "7", "1", "2", "1", "1", "1", "1", "7", "2", "1", "1", "1", "1", "2", "2", "4", "2", "1", "7", "1", "2", "1", "3", "7", "1", "2", "3", "2", "2", "2", "2", "2", "2", "2", "2", "1", "3", "4", "1", "1", "2", "5", "1", "1", "2", "1", "6", "1", "2", "4", "1", "3", "3", "2", "5", "2", "2", "2", "2", "5", "1", "3", "1", "11", "3", "6", "", "2", "1", "2", "1", "1", "2", "2", "2", "1", "4", "2", "2", "1", "1", "2"], 
    "sizemode": "area"
  }, 
  "text": ["Ålborg", "Åndalsnes", "Århus", "Bergen", "Boden", "Gōteborg", "Helsinki", "Honningsvåg", "Imatra", "Kajaani", "Karlskrona", "Kirkenes", "Kiruna", "København", "Kristiansand", "Kuopio", "Lahti", "Lieksa", "Lillehammer", "Mo I Rana", "Murmansk", "Narvik", "Norrköping", "Örebro", "Oslo", "Östersund", "Oulu", "Rovaniemi", "Stavanger", "Stockholm", "Sundsvall", "Tallinn", "Tampere", "Tornio", "Tromsø", "Trondheim", "Turku", "Umeå", "Vaasa", "Aberdeen", "Aberystwyth", "Barrow", "Belfast", "Birmingham", "Brighton", "Bristol", "Cambridge", "Cardiff", "Carlisle", "Carmarthen", "Cork", "Dover", "Dublin", "Dundalk", "Dundee", "Edinburgh", "Fort William", "France (1)", "France (2)", "Galway", "Glasgow", "Holyhead", "Hull", "Inverness", "Ipswich", "Leeds", "Limerick", "Liverpool", "Llandrindod Wells", "London", "Londonderry", "Manchester", "New York", "Newcastle", "Northampton", "Norwich", "Nottingham", "Penzance", "Plymouth", "Reading", "Rosslare", "Sligo", "Southampton", "Stornoway", "Stranraer", "Tullamore", "Ullapool", "Wick"], 
  "textfont": {
    "size": 8, 
    "color": "rgb(16, 17, 17)", 
    "family": "Arial"
  }, 
  "hoverinfo": "text", 
  "showlegend": False, 
  "hovertemplate": "", 
  "textposition": ["Middle right", "Middle right", "Middle left", "Middle left", "Middle left", "Middle right", "Middle right", "Middle left", "Middle right", "top center", "Middle right", "Middle left", "Middle right", "Middle right", "bottom left", "Middle right", "Middle right", "Middle right", "Middle right", "Middle left", "Middle right", "bottom center", "Middle right", "Middle right", "Middle left", "Middle left", "Middle left", "Middle right", "Middle left", "Middle right", "Middle right", "Middle right", "Middle left", "Middle left", "Middle right", "Middle left", "Middle left", "Middle left", "Middle right", "middle right", "middle left", "middle right", "middle right", "middle left", "middle right", "middle right", "middle top", "middle left", "middle right", "middle right", "middle right", "middle right", "middle right", "middle right", "middle right", "middle right", "middle right", "middle right", "middle right", "middle right", "middle right", "middle right", "middle right", "middle right", "middle right", "middle right", "middle right", "middle left", "middle right", "middle right", "middle right", "middle right", "middle right", "middle right", "bottom center", "middle right", "middle right", "middle right", "middle right", "middle left", "middle right", "middle right", "middle right", "middle right", "middle right", "middle right", "middle right", "middle right"]
}
trace8 = {
  "meta": {"columnNames": {
      "lat": "A", 
      "lon": "B", 
      "text": "C", 
      "marker": {"size": "E"}, 
      "textposition": "D"
    }}, 
  "mode": "markers+text", 
  "name": "Reveal/hide cities", 
  "type": "scattergeo", 
  "lat": ["57.048838126073115", "62.56747484421721", "56.16221213518473", "60.39260758540451", "65.82529822480663", "57.711569308929455", "60.17402178556654", "70.98239250260706", "61.17217169265381", "64.22155420807493", "56.161150630104586", "69.72704104672448", "67.85639904751547", "55.675499027107264", "58.160558760539054", "62.896357241162896", "60.9844075943206", "63.51156532644846", "61.11547314339694", "66.31406946239973", "68.973603209738", "68.43847778002933", "58.58771819476748", "59.27453941804889", "59.912345845293885", "63.17672346379236", "65.03212114675763", "66.53353021727351", "58.96951723462432", "59.328489928951704", "62.39027421134211", "59.43634291532583", "61.50009939885583", "65.84711630607462", "69.6676915048554", "63.430430273629675", "60.45191561645681", "63.826294802794955", "63.09490958440979", "57.149703501396736", "52.41538395316434", "54.10898120237651", "54.59624433819916", "52.486703588781516", "50.8223395340059", "51.45583992720376", "52.196214168983325", "51.484256453860205", "54.89227570867174", "51.85781129629228", "51.89809484577351", "51.127677706413735", "53.3508563016254", "53.99709555010845", "56.4628148386432", "55.953887423353336", "56.81965539202142", "", "", "53.27546679351384", "55.86806633226628", "53.30960834667442", "53.768574685826536", "57.4776813177482", "52.05719476806426", "53.80009440880148", "52.66338894246145", "53.40797098651094", "52.241351387097254", "51.505025293302154", "54.99582822638326", "53.47936876038216", "", "54.98067832990718", "52.23723275673263", "52.63097370136248", "52.955235015255575", "50.119018739310064", "50.374184748779925", "51.45413464335409", "52.254317922253996", "54.27684696325877", "50.90948402827984", "58.209217659645596", "54.90279317719651", "53.275498399825985", "57.895691343089695", "58.43912655563484"], 
  "lon": ["9.922223605516605", "7.687042937277424", "10.203944724356772", "5.304168608534294", "21.68354372704494", "11.98031871187112", "24.94860979008052", "25.972728576755586", "28.765364385611868", "27.729347946342923", "15.589838668957023", "30.04613179244278", "20.224842628607313", "12.570818866830635", "8.01397732186328", "27.687452551322547", "25.663365207287942", "30.018509865495975", "10.466400932038008", "14.141205731087945", "33.087769368194586", "17.42799628993811", "16.200678280512555", "15.209318701855853", "10.757642160826423", "14.642541584029566", "25.524905196664", "25.745848750170378", "5.73251963440812", "18.072681047373948", "17.30282447683423", "24.766385293412434", "23.7272646988628", "24.15246864892743", "18.925440091913607", "10.401607045729529", "22.27638581662958", "20.261872288582808", "21.621650135612082", "-2.0965980744914767", "-4.083176870318161", "-3.2203503010410097", "-5.926978092141603", "-1.8859545654469532", "-0.1362311113117233", "-2.5883168791363715", "0.13370342730019355", "-3.16763045779101", "-2.9323048218471928", "-4.312676112031723", "-8.474725538858953", "1.3136915736517523", "-6.2601336995931", "-6.405233799021794", "-2.973015423643524", "-3.1820527769166294", "-5.10426401682841", "", "", "-9.049092363889526", "-4.260620535940629", "-4.635181706986051", "-0.3261517783015", "-4.225793476977911", "1.1512910529776215", "-1.5518709815487344", "-8.614969725112568", "-2.9819867411301058", "-3.376084596632633", "-0.11877522664037725", "-7.30615295216364", "-2.243378099888314", "", "-1.6204536363116053", "-0.8882971703911592", "1.293701251701316", "-1.1563313993650752", "-5.537295584310239", "-4.142441723341992", "-0.9792418464399548", "-6.317813248420872", "-8.476352423781833", "-1.4078750094327217", "-6.384592603029308", "-5.02496617091827", "-7.495557493846783", "-5.1608089015686724", "-3.0935897056458237"], 
  "marker": {
    "line": {"color": "rgb(255, 255, 255)"}, 
    "meta": {"columnNames": {"size": "E"}}, 
    "color": "rgb(5, 4, 0)", 
    "opacity": 0.7, 
    "sizeref": 0.06666666666666667, 
    "size": ["2", "1", "1", "6", "2", "3", "7", "1", "2", "1", "1", "1", "1", "7", "2", "1", "1", "1", "1", "2", "2", "4", "2", "1", "7", "1", "2", "1", "3", "7", "1", "2", "3", "2", "2", "2", "2", "2", "2", "2", "2", "1", "3", "4", "1", "1", "2", "5", "1", "1", "2", "1", "6", "1", "2", "4", "1", "3", "3", "2", "5", "2", "2", "2", "2", "5", "1", "3", "1", "11", "3", "6", "", "2", "1", "2", "1", "1", "2", "2", "2", "1", "4", "2", "2", "1", "1", "2"], 
    "sizemode": "area"
  }, 
  "text": ["Ålborg", "Åndalsnes", "Århus", "Bergen", "Boden", "Gōteborg", "Helsinki", "Honningsvåg", "Imatra", "Kajaani", "Karlskrona", "Kirkenes", "Kiruna", "København", "Kristiansand", "Kuopio", "Lahti", "Lieksa", "Lillehammer", "Mo I Rana", "Murmansk", "Narvik", "Norrköping", "Örebro", "Oslo", "Östersund", "Oulu", "Rovaniemi", "Stavanger", "Stockholm", "Sundsvall", "Tallinn", "Tampere", "Tornio", "Tromsø", "Trondheim", "Turku", "Umeå", "Vaasa", "Aberdeen", "Aberystwyth", "Barrow", "Belfast", "Birmingham", "Brighton", "Bristol", "Cambridge", "Cardiff", "Carlisle", "Carmarthen", "Cork", "Dover", "Dublin", "Dundalk", "Dundee", "Edinburgh", "Fort William", "France (1)", "France (2)", "Galway", "Glasgow", "Holyhead", "Hull", "Inverness", "Ipswich", "Leeds", "Limerick", "Liverpool", "Llandrindod Wells", "London", "Londonderry", "Manchester", "New York", "Newcastle", "Northampton", "Norwich", "Nottingham", "Penzance", "Plymouth", "Reading", "Rosslare", "Sligo", "Southampton", "Stornoway", "Stranraer", "Tullamore", "Ullapool", "Wick"], 
  "visible": True, 
  "textfont": {
    "size": 8, 
    "color": "rgb(23, 24, 24)"
  }, 
  "hoverinfo": "text", 
  "textposition": ["Middle right", "Middle right", "Middle left", "Middle left", "Middle left", "Middle right", "Middle right", "Middle left", "Middle right", "top center", "Middle right", "Middle left", "Middle right", "Middle right", "bottom left", "Middle right", "Middle right", "Middle right", "Middle right", "Middle left", "Middle right", "bottom center", "Middle right", "Middle right", "Middle left", "Middle left", "Middle left", "Middle right", "Middle left", "Middle right", "Middle right", "Middle right", "Middle left", "Middle left", "Middle right", "Middle left", "Middle left", "Middle left", "Middle right", "middle right", "middle left", "middle right", "middle right", "middle left", "middle right", "middle right", "middle top", "middle left", "middle right", "middle right", "middle right", "middle right", "middle right", "middle right", "middle right", "middle right", "middle right", "middle right", "middle right", "middle right", "middle right", "middle right", "middle right", "middle right", "middle right", "middle right", "middle right", "middle left", "middle right", "middle right", "middle right", "middle right", "middle right", "middle right", "bottom center", "middle right", "middle right", "middle right", "middle right", "middle left", "middle right", "middle right", "middle right", "middle right", "middle right", "middle right", "middle right", "middle right"]
}
data = Data([trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8])
layout = {
  "geo": {
    "scope": "europe", 
    "center": {
      "lat": 64.7, 
      "lon": -6.091141166566366
    }, 
    "domain": {
      "x": [0, 1], 
      "y": [0, 1]
    }, 
    "bgcolor": "rgb(219, 242, 246)", 
    "showland": True, 
    "fitbounds": False, 
    "landcolor": "rgb(224, 223, 223)", 
    "showlakes": False, 
    "projection": {
      "type": "azimuthal equidistant", 
      "scale": 3.600000000000001, 
      "rotation": {
        "lat": 3, 
        "lon": 0, 
        "roll": 12
      }
    }, 
    "resolution": 50, 
    "countrycolor": "rgb(199, 197, 197)", 
    "showcountries": True, 
    "coastlinecolor": "rgb(138, 136, 136)", 
    "showcoastlines": True
  }, 
  "title": {"text": "Ticket to Ride: Nordic Countries – Route density of shortest paths to destination"}, 
  "xaxis": {
    "range": [-1, 6], 
    "autorange": True
  }, 
  "yaxis": {
    "range": [-1, 4], 
    "autorange": True
  }, 
  "legend": {
    "title": {
      "font": {
        "size": 10, 
        "color": "rgb(1, 5, 13)", 
        "family": "Arial"
      }, 
      "text": "Number of paths passing through route:"
    }, 
    "bgcolor": "rgb(232, 228, 228)", 
    "borderwidth": 1
  }, 
  "mapbox": {
    "zoom": 4.3925097749137665, 
    "pitch": 0, 
    "center": {
      "lat": 62.90633522366858, 
      "lon": 21.621442299215005
    }, 
    "bearing": 0
  }, 
  "autosize": True, 
  "dragmode": "pan", 
  "template": {
    "data": {
      "bar": [
        {
          "type": "bar", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "table": [
        {
          "type": "table", 
          "cells": {
            "fill": {"color": "#EBF0F8"}, 
            "line": {"color": "white"}
          }, 
          "header": {
            "fill": {"color": "#C8D4E3"}, 
            "line": {"color": "white"}
          }
        }
      ], 
      "carpet": [
        {
          "type": "carpet", 
          "aaxis": {
            "gridcolor": "#C8D4E3", 
            "linecolor": "#C8D4E3", 
            "endlinecolor": "#2a3f5f", 
            "minorgridcolor": "#C8D4E3", 
            "startlinecolor": "#2a3f5f"
          }, 
          "baxis": {
            "gridcolor": "#C8D4E3", 
            "linecolor": "#C8D4E3", 
            "endlinecolor": "#2a3f5f", 
            "minorgridcolor": "#C8D4E3", 
            "startlinecolor": "#2a3f5f"
          }
        }
      ], 
      "mesh3d": [
        {
          "type": "mesh3d", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }
        }
      ], 
      "contour": [
        {
          "type": "contour", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }, 
          "autocolorscale": True
        }
      ], 
      "heatmap": [
        {
          "type": "heatmap", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }, 
          "autocolorscale": True
        }
      ], 
      "scatter": [
        {
          "type": "scatter", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "surface": [
        {
          "type": "surface", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }
        }
      ], 
      "heatmapgl": [
        {
          "type": "heatmapgl", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }
        }
      ], 
      "histogram": [
        {
          "type": "histogram", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "parcoords": [
        {
          "line": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}, 
          "type": "parcoords"
        }
      ], 
      "scatter3d": [
        {
          "type": "scatter3d", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "scattergl": [
        {
          "type": "scattergl", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "choropleth": [
        {
          "type": "choropleth", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }
        }
      ], 
      "scattergeo": [
        {
          "type": "scattergeo", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "histogram2d": [
        {
          "type": "histogram2d", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }, 
          "autocolorscale": True
        }
      ], 
      "scatterpolar": [
        {
          "type": "scatterpolar", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "contourcarpet": [
        {
          "type": "contourcarpet", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }
        }
      ], 
      "scattercarpet": [
        {
          "type": "scattercarpet", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "scattermapbox": [
        {
          "type": "scattermapbox", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "scatterpolargl": [
        {
          "type": "scatterpolargl", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "scatterternary": [
        {
          "type": "scatterternary", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "histogram2dcontour": [
        {
          "type": "histogram2dcontour", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }, 
          "autocolorscale": True
        }
      ]
    }, 
    "layout": {
      "geo": {
        "bgcolor": "white", 
        "showland": True, 
        "lakecolor": "white", 
        "landcolor": "white", 
        "showlakes": True, 
        "subunitcolor": "#C8D4E3"
      }, 
      "font": {"color": "#2a3f5f"}, 
      "polar": {
        "bgcolor": "white", 
        "radialaxis": {
          "ticks": "", 
          "gridcolor": "#EBF0F8", 
          "linecolor": "#EBF0F8"
        }, 
        "angularaxis": {
          "ticks": "", 
          "gridcolor": "#EBF0F8", 
          "linecolor": "#EBF0F8"
        }
      }, 
      "scene": {
        "xaxis": {
          "ticks": "", 
          "gridcolor": "#DFE8F3", 
          "gridwidth": 2, 
          "linecolor": "#EBF0F8", 
          "zerolinecolor": "#EBF0F8", 
          "showbackground": True, 
          "backgroundcolor": "white"
        }, 
        "yaxis": {
          "ticks": "", 
          "gridcolor": "#DFE8F3", 
          "gridwidth": 2, 
          "linecolor": "#EBF0F8", 
          "zerolinecolor": "#EBF0F8", 
          "showbackground": True, 
          "backgroundcolor": "white"
        }, 
        "zaxis": {
          "ticks": "", 
          "gridcolor": "#DFE8F3", 
          "gridwidth": 2, 
          "linecolor": "#EBF0F8", 
          "zerolinecolor": "#EBF0F8", 
          "showbackground": True, 
          "backgroundcolor": "white"
        }
      }, 
      "title": {"x": 0.05}, 
      "xaxis": {
        "ticks": "", 
        "gridcolor": "#EBF0F8", 
        "linecolor": "#EBF0F8", 
        "automargin": True, 
        "zerolinecolor": "#EBF0F8", 
        "zerolinewidth": 2
      }, 
      "yaxis": {
        "ticks": "", 
        "gridcolor": "#EBF0F8", 
        "linecolor": "#EBF0F8", 
        "automargin": True, 
        "zerolinecolor": "#EBF0F8", 
        "zerolinewidth": 2
      }, 
      "ternary": {
        "aaxis": {
          "ticks": "", 
          "gridcolor": "#DFE8F3", 
          "linecolor": "#A2B1C6"
        }, 
        "baxis": {
          "ticks": "", 
          "gridcolor": "#DFE8F3", 
          "linecolor": "#A2B1C6"
        }, 
        "caxis": {
          "ticks": "", 
          "gridcolor": "#DFE8F3", 
          "linecolor": "#A2B1C6"
        }, 
        "bgcolor": "white"
      }, 
      "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#19d3f3", "#e763fa", "#fecb52", "#ffa15a", "#ff6692", "#b6e880"], 
      "hovermode": "closest", 
      "colorscale": {
        "diverging": [
          [0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419], 
        "sequential": [
          [0, "#0508b8"], [0.0893854748603352, "#1910d8"], [0.1787709497206704, "#3c19f0"], [0.2681564245810056, "#6b1cfb"], [0.3575418994413408, "#981cfd"], [0.44692737430167595, "#bf1cfd"], [0.5363128491620112, "#dd2bfd"], [0.6256983240223464, "#f246fe"], [0.7150837988826816, "#fc67fd"], [0.8044692737430168, "#fe88fc"], [0.8938547486033519, "#fea5fd"], [0.9832402234636871, "#febefe"], [1, "#fec3fe], 
        "sequentialminus": [
          [0, "#0508b8"], [0.0893854748603352, "#1910d8"], [0.1787709497206704, "#3c19f0"], [0.2681564245810056, "#6b1cfb"], [0.3575418994413408, "#981cfd"], [0.44692737430167595, "#bf1cfd"], [0.5363128491620112, "#dd2bfd"], [0.6256983240223464, "#f246fe"], [0.7150837988826816, "#fc67fd"], [0.8044692737430168, "#fe88fc"], [0.8938547486033519, "#fea5fd"], [0.9832402234636871, "#febefe"], [1, "#fec3fe]
      }, 
      "plot_bgcolor": "white", 
      "paper_bgcolor": "white", 
      "shapedefaults": {
        "line": {"width": 0}, 
        "opacity": 0.4, 
        "fillcolor": "#506784"
      }, 
      "annotationdefaults": {
        "arrowhead": 0, 
        "arrowcolor": "#506784", 
        "arrowwidth": 1
      }
    }, 
    "themeRef": "PLOTLY_WHITE"
  }, 
  "showlegend": True, 
  "paper_bgcolor": "rgb(219, 242, 246)"
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)