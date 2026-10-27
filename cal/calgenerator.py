

import urllib.parse as up
import datetime as dt
import zoneinfo as zi

BASEYEAR = 2026
BASETIME = 16 
HOSTTIMEZONE = "Europe/Berlin"
ZOOMLINK = 'https://uni-passau.zoom-x.de/j/64779445248?pwd=ffFmeSI6Mb0YbSjbpxTam3N6Q5hIwK.1'

def create_link(ics_file,speaker,title,day,month,year=BASEYEAR,hour=BASETIME,zoom=ZOOMLINK):
    timestamp = dt.datetime(year,month,day,hour,tzinfo=zi.ZoneInfo(HOSTTIMEZONE))
    details = f'Speaker: {speaker}\nTalk: {title}\n\n'+zoom
    timestr = timestamp.strftime("%Y%m%dT%H%M%SZ/")+(timestamp+dt.timedelta(hours=1)).strftime("%Y%m%dT%H%M%SZ")
    url = 'https://calendar.google.com/calendar/render?'
    query = up.urlencode({'action':'TEMPLATE',
                          'dates':timestr,
                          'details':details,
                          'location':'',
                          'text':'ThRaSH Seminar'},quote_via=up.quote)

    link = f"""
    <!-- Calendar link for {year}-{month}-{day} generated on: {dt.datetime.now(dt.timezone(dt.timedelta(0)))} -->
    <a href="{url+query}" class="btn btn-season mx-3" target="_blank" rel="noopener">
        <i class="bi bi-google me-2"></i>
        Add to Google Calendar
    </a>    
    <a href="cal/{ics_file}" class="btn btn-season mx-3" target="_blank" rel="noopener">
        <i class="bi calendar2-heart-fill me-2"></i>
        Add to Calendar
    </a>
    """
    return link

def write_ics_file(speaker,title,day,month,year=BASEYEAR,hour=BASETIME,zoom=ZOOMLINK):
    uid = f'ThRaSH-{year}-{month}-{day}'
    fname = uid + '.ics'
    event = f"""
    BEGIN:VCALENDAR
    VERSION:2.0
    PRODID:-//ThRaSH Seminar//Generated ICS//
    CALSCALE:GREGORIAN
    METHOD:PUBLISH
    BEGIN:VTIMEZONE
    TZID:Europe/Berlin
    BEGIN:DAYLIGHT
    TZOFFSETFROM:+0100
    TZOFFSETTO:+0200
    TZNAME:CEST
    DTSTART:19700329T020000
    RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
    END:DAYLIGHT
    BEGIN:STANDARD
    TZOFFSETFROM:+0200
    TZOFFSETTO:+0100
    TZNAME:CET
    DTSTART:19701025T030000
    RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
    END:STANDARD
    END:VTIMEZONE
    BEGIN:VEVENT
    UID:{uid}
    DTSTART;TZID=Europe/Berlin:{year}{month}{day}T{hour}0000Z
    DTEND;TZID=Europe/Berlin:{year}{month}{day}T{hour+1}0000Z
    SUMMARY:ThRaSH Seminar
    DESCRIPTION:Speaker: {speaker.replace(",",r"\,")}\\nTitle: {title.replace(",",r"\,")}
    LOCATION:{zoom}
    END:VEVENT
    END:VCALENDAR
    """
    with open(fname,'w') as f:
        f.write(event)
    return fname

          

def schedule_talk(speaker,title,day,month,year=BASEYEAR,hour=BASETIME,zoom=ZOOMLINK):
    ics_file = write_ics_file(speaker,title,day,month,year,hour,zoom)
    link_str = create_link(ics_file,speaker,title,day,month,year,hour,zoom)
    print(link_str)

    

schedule_talk("Per Kristian Lehre (University of Birmingham, UK)"," Can LLMs Design and Analyse Evolutionary Algorithms? Machine-checked Runtime Bounds in Lean",20,10)
schedule_talk("Johanna Gasse (Hasso Plattner Institute, Germany)","Vertex Coloring: Combinatorial Landscape Analysis and Run Time Bounds",27,10)
schedule_talk("Andre Opris (University of Passau, Germany)","",3,11)
schedule_talk("Yuetong Sun (Nanjing University, China) ","Theoretical Analysis of Multi-Objective Evolutionary Algorithms on Integer Spaces with Local Optima",10,11,hour=15)
#schedule_talk("","",17,11)
#schedule_talk("","",24,11)
schedule_talk("Roman Kalkreuth (RWTH Aachen University, Germany)","Runtime Analysis of Cartesian Genetic Programming on MAX: A Proven Exponential Speedup",1,12)
#schedule_talk("","",8,12)
#schedule_talk("","",15,12)



