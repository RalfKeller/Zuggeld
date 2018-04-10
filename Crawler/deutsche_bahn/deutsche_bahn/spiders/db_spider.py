import scrapy
import datetime
import time

class MiniSpider(scrapy.Spider):

    name = "db"

    strecken = [{"abfahrt": "Aachen ", "ankunft": " Hamm(Westf)"}, {"abfahrt": "Hamm(Westf) ", "ankunft": " Aachen"}, {"abfahrt": "Düsseldorf HBF ", "ankunft": " Münster"}, {"abfahrt": "Münster ", "ankunft": " Düsseldorf"}, {"abfahrt": "Düsseldorf HBF ", "ankunft": " Hamm(Westf)"}, {"abfahrt": "Hamm(Westf) ", "ankunft": " Düsseldorf"}, {"abfahrt": "Aachen ", "ankunft": " Dortmund"}, {"abfahrt": "Dortmund ", "ankunft": " Aachen"}, {"abfahrt": "Wesel ", "ankunft": " Bonn UN Campus"}, {"abfahrt": "Bonn UN Campus ", "ankunft": " Wesel"}, {"abfahrt": "Köln Bonn Flughafen ", "ankunft": " Minden"}, {"abfahrt": "Minden ", "ankunft": " Köln Bonn Flughafen"}, {"abfahrt": "Krefeld ", "ankunft": " Rheine"}, {"abfahrt": "Rheine ", "ankunft": " Krefeld"}, {"abfahrt": "Aachen ", "ankunft": " Siegen"}, {"abfahrt": "Siegen ", "ankunft": " Aachen"}, {"abfahrt": "Kleve ", "ankunft": " Düsseldorf HBF"}, {"abfahrt": "Düsseldorf HBF", "ankunft": " Kleve"}, {"abfahrt": "Düsseldorf HBF", "ankunft": " Paderborn"}, {"abfahrt": "Paderborn ", "ankunft": " Düsseldorf"}, {"abfahrt": "Köln ", "ankunft": " Trier"}, {"abfahrt": "Triet ", "ankunft": " Köln"}, {"abfahrt": "Mönchengladbach ", "ankunft": " Hamm(Westf)"}, {"abfahrt": "Hamm(Westf) ", "ankunft": " Mönchengladbach"}, {"abfahrt": "Borken(Westf)", "ankunft": " Essen "}, {"abfahrt": "Essen ", "ankunft": " Borken(Westf)"}, {"abfahrt": "Münster ", "ankunft": " Rheine"}, {"abfahrt": "Rheine ", "ankunft": " Münster"}, {"abfahrt": "Essen ", "ankunft": " Iserlohn"}, {"abfahrt": "Iserlohn ", "ankunft": " Essen"}, {"abfahrt": "Hagen ", "ankunft": " Warburg"}, {"abfahrt": "Warburg ", "ankunft": " Hagen"}, {"abfahrt": "Düren", "ankunft": " Linnich Bhf"}, {"abfahrt": "Linnich Bhf", "ankunft": " Düren"}, {"abfahrt": "Köln ", "ankunft": " Euskirchen"}, {"abfahrt": "Euskirchen ", "ankunft": " Köln"}, {"abfahrt": "Bad Münstereifel ", "ankunft": " Euskirchen"}, {"abfahrt": "Euskirchen ", "ankunft": " Bad Münstereifel"}, {"abfahrt": "Köln ", "ankunft": " Bonn"}, {"abfahrt": "Bonn ", "ankunft": " Köln"}, {"abfahrt": "Mönchengladbach ", "ankunft": " Bad Honnef"}, {"abfahrt": "Bad Honnef ", "ankunft": " Mönchengladbach"}, {"abfahrt": "Düren ", "ankunft": " Euskirchen"}, {"abfahrt": "Euskirchen ", "ankunft": " Düren "}, {"abfahrt": "Duisburg ", "ankunft": " Xanten"}, {"abfahrt": "Xanten ", "ankunft": " Duisburg"}, {"abfahrt": "Bocholt ", "ankunft": " Wesel"}, {"abfahrt": "Aachen ", "ankunft": " Duisburg"}, {"abfahrt": "Duisburg ", "ankunft": " Aachen"}, {"abfahrt": "Dalheim ", "ankunft": " Mönchengladbach"}, {"abfahrt": "Mönchengladbach ", "ankunft": " Dalheim"}, {"abfahrt": "Wesel ", "ankunft": " Mönchengladbach"}, {"abfahrt": "Mönchengladbach ", "ankunft": " Wesel "}, {"abfahrt": "Duisburg", "ankunft": "Ruhrort "}, {"abfahrt": "Oberhausen ", "ankunft": " Duisburg"}, {"abfahrt": "Duisburg ", "ankunft": " Duisburg"}, {"abfahrt": "Bedburg(Erft) ", "ankunft": " Köln Messe/Deutz"}, {"abfahrt": "Köln Messe/Deutz ", "ankunft": " Bedburg(Erft)"}, {"abfahrt": "Düsseldorf HBF", "ankunft": " Bedburg(Erft)"}, {"abfahrt": "Bedburg(Erft)", "ankunft": " Düsseldorf"}, {"abfahrt": "Essen ", "ankunft": " Hagen"}, {"abfahrt": "Hagen ", "ankunft": " Essen"}, {"abfahrt": "Münster ", "ankunft": " Mönchengladbach"}, {"abfahrt": "Mönchengladbach ", "ankunft": " Münster"}, {"abfahrt": "Brilon Stadt ", "ankunft": " Brilon Wald"}, {"abfahrt": "Brilon Wald ", "ankunft": " Brilon Stadt"}, {"abfahrt": "Dorsten ", "ankunft": " Dortmund"}, {"abfahrt": "Dortmund ", "ankunft": " Dorsten"}, {"abfahrt": "Dorsten ", "ankunft": " Oberhausen"}, {"abfahrt": "Oberhausen ", "ankunft": " Dorsten"}, {"abfahrt": "Dorsten ", "ankunft": " Coesfeld"}, {"abfahrt": "Coesfeld ", "ankunft": " Dorsten"}, {"abfahrt": "Gelsenkirchen ", "ankunft": " Bochum"}, {"abfahrt": "Bochum ", "ankunft": " Gelsenkirchen"}, {"abfahrt": "Wuppertal", "ankunft": "Oberbarmen "}, {"abfahrt": "Bonn", "ankunft": "Mehlem "}, {"abfahrt": "Dortmund ", "ankunft": " Münster"}, {"abfahrt": "Münster ", "ankunft": " Dortmund"}, {"abfahrt": "Dortmund ", "ankunft": " Gronau "}, {"abfahrt": "Gronau ", "ankunft": " Dortmund"}, {"abfahrt": "Dortmund ", "ankunft": " Iserlohn"}, {"abfahrt": "Iserlohn ", "ankunft": " Dortmund"}, {"abfahrt": "Unna ", "ankunft": " Neuenrade"}, {"abfahrt": "Neuenrade ", "ankunft": " Unna"}, {"abfahrt": "Dortmund ", "ankunft": " Brilon Stadt"}, {"abfahrt": "Brilon Stadt ", "ankunft": " Dortmund"}, {"abfahrt": "Dortmund ", "ankunft": " Soest"}, {"abfahrt": "Soest ", "ankunft": " Dortmund"}, {"abfahrt": "Rheine ", "ankunft": " Bielefeld"}, {"abfahrt": "Bielefeld ", "ankunft": " Rheine"}, {"abfahrt": "Münster(W)Zentrum Nord ", "ankunft": " Coesfeld"}, {"abfahrt": "Coesfeld ", "ankunft": " Münster(W)Zentrum Nord"}, {"abfahrt": "Münster ", "ankunft": " Gronau"}, {"abfahrt": "Gronau ", "ankunft": " Münster"}, {"abfahrt": "Münster ", "ankunft": " Rheine"}, {"abfahrt": "Rheine ", "ankunft": " Münster"}, {"abfahrt": "Münster ", "ankunft": " Lengerich"}, {"abfahrt": "Lengerich ", "ankunft": " Münster"}, {"abfahrt": "Münster ", "ankunft": " Bielefeld"}, {"abfahrt": "Bielefeld ", "ankunft": " Münster"}, {"abfahrt": "Münster ", "ankunft": " Bielefeld"}, {"abfahrt": "Bielefeld ", "ankunft": " Münster"}, {"abfahrt": "Bielefeld ", "ankunft": " Minden"}, {"abfahrt": "Minden ", "ankunft": " Bielefeld"}, {"abfahrt": "Bielefeld ", "ankunft": " Rahden"}, {"abfahrt": "Rahden ", "ankunft": " Bielefeld"}, {"abfahrt": "Herford ", "ankunft": " Paderborn"}, {"abfahrt": "Paderborn ", "ankunft": " Herford"}, {"abfahrt": "Bielefeld ", "ankunft": " Paderborn"}, {"abfahrt": "Paderborn ", "ankunft": " Bielefeld"}, {"abfahrt": "Löhne ", "ankunft": " Rinteln"}, {"abfahrt": "Rinteln ", "ankunft": " Löhne"}, {"abfahrt": "Minden ", "ankunft": " Bielefeld"}, {"abfahrt": "Bielefeld ", "ankunft": " Minden"}, {"abfahrt": "Bielefeld ", "ankunft": " Altenbeken"}, {"abfahrt": "Altenbeken ", "ankunft": " Bielefeld"}, {"abfahrt": "Ottbergen ", "ankunft": " Paderborn"}, {"abfahrt": "Paderborn ", "ankunft": " Ottbergen"}, {"abfahrt": "Ottbergen ", "ankunft": " Paderborn"}, {"abfahrt": "Paderborn ", "ankunft": " Ottbergen"}, {"abfahrt": "Münster ", "ankunft": " Warburg"}, {"abfahrt": "Warburg ", "ankunft": " Münster"}, {"abfahrt": "Siegen ", "ankunft": " Au(Sieg)"}, {"abfahrt": "Au(Sieg) ", "ankunft": " Siegen"}, {"abfahrt": "Hagen ", "ankunft": " Iserlohn"}, {"abfahrt": "Iserlohn ", "ankunft": " Hagen"}, {"abfahrt": "Siegen ", "ankunft": " Bad Berleburg"}, {"abfahrt": "Bad Berleburg ", "ankunft": " Siegen"}, {"abfahrt": "Siegen ", "ankunft": " Wilnsdorf"}, {"abfahrt": "Wilnsdorf", "ankunft": "Rudersdorf(Siegen)"}, {"abfahrt": "Neunkirchen ", "ankunft": " Burbach Mitte"}, {"abfahrt": "Burbach Mitte", "ankunft": " Neunkirchen"}, {"abfahrt": "Dortmund ", "ankunft": " Solingen"}, {"abfahrt": "Solingen ", "ankunft": " Dortmund"}, {"abfahrt": "Dortmund ", "ankunft": " Gelsenkirchen"}, {"abfahrt": "Gelsenkirchen ", "ankunft": " Dortmund"}, {"abfahrt": "Oberhausen ", "ankunft": "Hattingen(R) Mitte"}, {"abfahrt": "Hattingen(R) Mitte", "ankunft": " Oberhausen"}, {"abfahrt": "Unna ", "ankunft": " Dortmund"}, {"abfahrt": "Dortmund ", "ankunft": " Hagen"}, {"abfahrt": "Hagen ", "ankunft": " Dortmund"},  {"abfahrt": "Wupptertal ", "ankunft": " Solingen"}, {"abfahrt": "Hagen ", "ankunft": " Mönchengladbach"}, {"abfahrt": "Mönchengladbach ", "ankunft": " Hagen"}, {"abfahrt": "Marl(Westf) Mitte", "ankunft": " Bottrop"}, {"abfahrt": "Bottrop ", "ankunft": " Marl(Westf) Mitte"}, {"abfahrt": "Köln ", "ankunft": " Au(Sieg)"}, {"abfahrt": "Au(Sieg) ", "ankunft": " Köln"}, {"abfahrt": "Aachen ", "ankunft": " Troisdorf"}, {"abfahrt": "Troisdorf ", "ankunft": " Aachen"}, {"abfahrt": "Düren ", "ankunft": " Au(Sieg)"}, {"abfahrt": "Au(Sieg) ", "ankunft": " Düren"}, {"abfahrt": "Bonn ", "ankunft": " Euskirchen"}, {"abfahrt": "Euskirchen ", "ankunft": " Bonn"}, {"abfahrt": "Mettmann Stadtwald ", "ankunft": " Neuss"}, {"abfahrt": "Wuppertal", "ankunft": "Vohwinkel "}]
    
    custom_settings = {
        #'USER_AGENT' : 'usermuser1234',
        'ROBOTSTXT_OBEY' :  False,
    }
    
    start_urls = ["https://www.bahn.de/p/view/index.shtml"
        
    ]
    now = datetime.datetime.now()
    weekdays = ["Mo","Di","Mi","Do","Fr","Sa","So"]
    weekday = datetime.datetime.today().weekday()
    weekday = weekdays[weekday]

    ajax_more_details = "HWAI=CONNECTION$C0-2!id=C0-2!HwaiConId=C0-2!HwaiDetailStatus=details!&ajax=1"


    def parse(self, response):
        for strecke in self.strecken:
		    yield scrapy.Request("https://reiseauskunft.bahn.de/bin/query.exe/dn?revia=yes&existOptimizePrice=1&country=DEU&dbkanal_007=L01_S01_D001_KIN0001_qf-bahn-svb-nn-kl2_lz03&start=1&protocol=https%3A&REQ0JourneyStopsS0A=1&S="+strecke["ankunft"]+"&Z="+strecke["abfahrt"]+"&REQ0JourneyStopsZID=&date="+self.weekday+"%2C+"+str(self.now.day)+"."+str(self.now.month)+"."+str(self.now.year)+"&time="+str((self.now.hour+1)%24)+"%3A"+str(self.now.minute)+"&timesel=depart&returnDate=&returnTime=&returnTimesel=depart&optimize=0&journeyProducts=1016&auskunft_travelers_number=1&tariffTravellerType.1=E&tariffTravellerReductionClass.1=0&tariffClass=2&rtMode=DB-HYBRID&externRequest=yes&HWAI=JS%21js%3Dyes%21ajax%3Dyes%21",
                callback= self.parse_artikel)

    #def parse_kategorie(self, response):
    


            
    def parse_artikel(self, response):
        if response.css("title::text").extract_first().find("Verbindungen - Fehler") > 0:
            if not response.css("p:nth-child(4)::text").extract_first().find("H9380") > 0:
                time.sleep(5)
                yield scrapy.Request(response.url,dont_filter=True,callback=self.parse_artikel)
        else:
            train_blocks = response.css(".boxShadow.scheduledCon")
            if not train_blocks:
                yield {"train_block":"null", "url":response.url, "body":response.text} 
            for block in train_blocks:

                prognosed_time = block.css(".last .time::text").extract_first()
                actual_time = block.css(".last .time .delay::text").extract_first()
                request_date = str(self.now.day)+"."+str(self.now.month)+"."+str(self.now.year)
                tomorrow = datetime.date.today() + datetime.timedelta(days=1)
                if actual_time:
                    differenz = self.get_min_diff(prognosed_time,actual_time)
                else:
                    differenz = 0
                
                start_station = block.css(".station.first::text").extract_first()
                end_station = block.css(".stationDest::text").extract_first()

                request_time= str((self.now.hour+1)%24) + ":" + str(self.now.minute)
                
                if actual_time:
                    if self.is_arrival_tomorrow(request_time, actual_time):
                        arrival_date = tomorrow
                    else:
                        arrival_date = request_date
                else:
                    if self.is_arrival_tomorrow(request_time, prognosed_time):
                        arrival_date = tomorrow
                    else:
                        arrival_date = request_date

                departure_time = block.css(".firstrow .time::text").extract()
                
                more_details_link = block.css(".open::attr(href)").extract_first() + self.ajax_more_details

                if differenz > 60:
                    meta_dict = { "prognose":prognosed_time, 
                            "realtime": actual_time, 
                            "url":response.url, 
                            "difference": differenz,
                            "start_station": start_station,
                            "end_station": end_station,
                            "datum": request_date,
                            "request_time": str((self.now.hour+1)%24)+":"+str(self.now.minute),
                            "arrival_date" : arrival_date,
                            "departure_time": departure_time,
                            "more_details_link" : more_details_link
                            }

                    yield scrapy.http.Request(more_details_link, meta= meta_dict, callback=self.parse_more_details)

                    # yield { "prognose":prognosed_time, 
                    #         "realtime": actual_time, 
                    #         "url":response.url, 
                    #         "difference": differenz,
                    #         "start_station": start_station,
                    #         "end_station": end_station,
                    #         "datum": request_date,
                    #         "request_time": str((self.now.hour+1)%24)+":"+str(self.now.minute),
                    #         "arrival_date" : arrival_date,
                    #         "departure_time": departure_time,
                    #         "more_details_link" : more_details_link
                    #         }
        
    def parse_more_details(self, response):

        train_number = response.css(".products a::text").extract_first()
        train_type = train_number.split(' ',1)[0]

        yield {     "prognose":response.meta['prognose'], 
                    "realtime": response.meta['realtime'], 
                    "url":response.meta['url'], 
                    "difference": response.meta['difference'],
                    "start_station": response.meta['start_station'],
                    "end_station": response.meta['end_station'],
                    "datum": response.meta['datum'],
                    "request_time": response.meta['request_time'],
                    "arrival_date" : response.meta['arrival_date'],
                    "departure_time": response.meta['departure_time'],
                    "more_details_link" : response.meta['more_details_link'],
                    "train_type": train_type,
                    "train_number": train_number,
                    }


    def get_min(self,time_str):
        h = time_str.split(':')
        return int(h[0]) * 60 + int(h[1])

    def get_min_diff(self, prognose, tatsache):
        prognose_min = self.get_min(prognose)
        tatsache_min = self.get_min(tatsache)
        if prognose_min > tatsache_min:
            tatsache_min = tatsache_min + 24*60 
        return tatsache_min - prognose_min

    def is_arrival_tomorrow(self,prognose,tatsache):
        prognose_min = self.get_min(prognose)
        tatsache_min = self.get_min(tatsache)
        if prognose_min > tatsache_min:
            return True
        else:
            return False

