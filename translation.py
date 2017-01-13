class Translators:
  def __init__(self):

    # translate official name to a shorter version  
    self.response_short = {    
        "Algoma University": "Algoma",
        "Brescia University College": "Brescia",
        "Brock University": "BrockU",
        "Carleton University": "CarletonU",
        "Collège de Hearst": "Hearst",
        "Huntington University": "Huntington",
        "Huron University College": "Huron",
        "King's University College": "Kings",
        "Lakehead University": "Lakehead",
        "Laurentian University of Sudbury": "LaurentianU",
        "McMaster University": "McMasterU",
        "Nipissing University": "NipissingU",
        "Northern Ontario School of Medicine": "NOSM",
        "Ontario College of Art and Design University": "OCAD",
        "Queen's University": "Queens",
        "Ryerson University": "Ryerson",
        "Trent University": "Trent",
        "Trinity College": "Trinity",
        "University of Guelph": "GuelphU",
        "University of Ontario Institute of Technology": "UOIT",
        "University of Ottawa": "OttawaU",
        "University of St. Michael's College": "St. M",
        "University of Sudbury": "SudburyU",
        "University of Toronto": "UofT",
        "University of Waterloo": "UoW",
        "University of Western Ontario": "UWO",
        "University of Windsor": "WindsorU",
        "Victoria University": "VictoriaU",
        "Wilfrid Laurier University": "WLaurier",
        "York University": "York"
    }
    self.hashtags = {    
        "Algoma University": "#AlgomaU",
        "Brescia University College": "#uWaterloo",
        "Brock University": "#BrockU",
        "Carleton University": "#CarletonU",
        "Collège de Hearst": "#HearstCollege",
        "Huntington University": "#HuntingtonU",
        "Huron University College": "#uwo",
        "King's University College": "#uwo",
        "Lakehead University": "#LakeheadU",
        "Laurentian University of Sudbury": "#LaurentianU",
        "McMaster University": "#McMasterU",
        "Nipissing University": "#NipissingU",
        "Northern Ontario School of Medicine": "#NOSM",
        "Ontario College of Art and Design University": "#OCAD",
        "Queen's University": "#QueensU",
        "Ryerson University": "#RyersonU",
        "Trent University": "#TrentU",
        "Trinity College": "#uoft",
        "University of Guelph": "#uofg",
        "University of Ontario Institute of Technology": "#UOIT",
        "University of Ottawa": "#uOttawa",
        "University of St. Michael's College": "#uoft",
        "University of Sudbury": "#uSudbury",
        "University of Toronto": "#uoft",
        "University of Waterloo": "#uwaterloo",
        "University of Western Ontario": "#uwo",
        "University of Windsor": "#uWindsor",
        "Victoria University": "#uoft",
        "Wilfrid Laurier University": "#WilfredLaurier",
        "York University": "#YorkU"
    }

    self.uni_short = {
        #a
        "au": "Algoma University",
        "algoma": "Algoma University",
        "a": "Algoma University",
        "#algomau": "Algoma University",

        #b
        "bresica": "Brescia University College",
        "buc": "Brescia University College",
        "br": "Brescia University College",
        "#brocku": "Brock University",
        "brock": "Brock University",
        "bu": "Brock University",
        "b": "Brock University",

        #c
        "#carletonu": "Carleton University",
        "carleton": "Carleton University",
        "cu": "Carleton University",
        "c": "Carleton University",
        
        "hearst": "Collège de Hearst",
        "cdh": "Collège de Hearst",

        #h
        "h": "Huntington University",
        "hunt": "Huntington University",
        "huntingtion": "Huntington University",
        "hu": "Huntington University",
        "huc": "Huron University College",
        "huron": "Huron University College",

        #k
        "kings": "King's University College",
        "kuc": "King's University College",
        "ku": "King's University College",
        "k": "King's University College",

        #l
        "lakehead": "Lakehead University",
        "lu": "Lakehead University",
        "laurentian": "Laurentian University of Sudbury",
        "lus":"Laurentian University of Sudbury",

        #m
        "m": "McMaster University",
        "mu": "McMaster University",
        "mac": "McMaster University",
        "mcmaster": "McMaster University",

        #n
        "nipissing": "Nipissing University",
        "nip": "Nipissing University",
        "nu": "Nipissing University",
        "nosm": "Northern Ontario School of Medicine",
        "nosom": "Northern Ontario School of Medicine",
        "n" : "Northern Ontario School of Medicine",

        #o
        "ocad": "Ontario College of Art and Design University",
        "o": "Ontario College of Art and Design University",
        "art": "Ontario College of Art and Design University",
        "design": "Ontario College of Art and Design University",

        #q

        "qu": "Queen's University",
        "q": "Queen's University",
        "queens": "Queen's University",
        "uqueens": "Queen's University",
        "uq": "Queen's University",
        "queensu": "Queen's University",
        "queensuni": "Queen's University",

        #r
        "r": "Ryerson University",
        "ry": "Ryerson University",
        "ru": "Ryerson University",
        "rye": "Ryerson University",
        "ryerson": "Ryerson University",
        "ryhi": "Ryerson University",
        "ryehi": "Ryerson University",
        "ryhigh": "Ryerson University",
        "ryehigh": "Ryerson University",
        
        #t
        "trent": "Trent University",
        "tu": "Trent University",
        "utrent": "Trent University",
        "trentu": "Trent University",

        "trinity": "Trinity College",
        "trin": "Trinity College",
        "tc": "Trinity College",
        "t": "Trinity College",

        # u g
        "guelph": "University of Guelph",
        "gu": "University of Guelph",
        "g": "University of Guelph",
        "uog": "University of Guelph",
        "uofg": "University of Guelph",
        "uguelph": "University of Guelph",
        "guelphu": "University of Guelph",

        #u o
        "uoit": "University of Ontario Institute of Technology",
        "oit": "University of Ontario Institute of Technology",
        "it": "University of Ontario Institute of Technology",

        "ottawa": "University of Ottawa",
        "uottawa": "University of Ottawa",
        "uo": "University of Ottawa",        
        "o": "University of Ottawa",
        "uott": "University of Ottawa",
        "udo": "University of Ottawa",
        "ottawau": "University of Ottawa",
        "ou": "University of Ottawa",
        "ottu": "University of Ottawa",

        #uoft
        "usmc": "University of St. Michael's College",
        "stmikes": "University of St. Michael's College",
        "uosmc": "University of St. Michael's College",
        "stmike": "University of St. Michael's College",
        "smc": "University of St. Michael's College",
        "ustmikes": "University of St. Michael's College",
        "stmikesu": "University of St. Michael's College",


        #u s
        "sudbury": "University of Sudbury",
        "s": "University of Sudbury",
        "uos": "University of Sudbury",
        "usud": "University of Sudbury",
        "sudu": "University of Sudbury",
        "suds": "University of Sudbury",
        "usudbury": "University of Sudbury",
        "sudburyu": "University of Sudbury",


        #u t
        "uoft": "University of Toronto",
        "t": "University of Toronto",
        "utor": "University of Toronto",
        "toru": "University of Toronto",
        "utoronto": "University of Toronto",
        "torontou": "University of Toronto",


        #u w
        "uow": "University of Waterloo",
        "waterloo": "University of Waterloo",
        "w": "University of Waterloo",
        "wat": "University of Waterloo",
        "wat": "University of Waterloo",
        "uw": "University of Waterloo",
        "uwaterloo": "University of Waterloo",
        "uwat": "University of Waterloo",
        "watu": "University of Waterloo",

        "western": "University of Western Ontario",
        "uwo": "University of Western Ontario",
        "uwestern": "University of Western Ontario",
        "westernu": "University of Western Ontario",

        "windsor": "University of Windsor",
        "uwindsor": "University of Windsor",
        "windsoru": "University of Windsor",
        "wi": "University of Windsor",
        "win": "University of Windsor",
        "wind": "University of Windsor",
        "uowi": "University of Windsor",

        #v (uoft)
        "vu": "Victoria University",
        "v": "Victoria University",

        #w
        "wlu": "Wilfrid Laurier University",
        "wil": "Wilfrid Laurier University",
        "wl": "Wilfrid Laurier University",
        "willie": "Wilfrid Laurier University",
        "willy": "Wilfrid Laurier University",
        "wili": "Wilfrid Laurier University",
        "willi": "Wilfrid Laurier University",

        #y
        "yorku": "York University",
        "york": "York University",
        "yu": "York University",
        "y": "York University"}

    #more well known translated into less well known
    self.affiliates = {
        "University of Waterloo": ["Brescia University College"],
        "University of Western Ontario": ["King's University College", "Huron University College"],
        "University of Toronto": ["University of St. Michael's College", "Trinity College", "Victoria University"]
        }

