def analyze_traffic_flow(filename):
    total_district = {}
    congest_streets = []

    with open(filename,"r") as file :
        for line in file :
            line = line.strip()
            parts = line.split(',')
            if len(parts) != 4 :
             continue
            street , district , car_count , truck_count = parts
            try:
               car_count = int(car_count)
               truck_count = int(truck_count)
            except ValueError:
               continue
            total_vol = car_count + truck_count
            if district not in total_district:
               total_district[district] = 0
            total_district[district] += total_vol
            if total_vol > 500:
               congest_streets.append((street , total_vol))
    return total_district, congest_streets

def write_traffic_report(district_totals, congested_streets):
   with open("traffic_report.txt" ,"w") as f :
      f.write("DISTRICT TRAFFIC VOLUME\n")
      f.write("--------------------------")
      
      for district , total in district_totals.items():
         f.write(f"{district} : {total}\n")

      f.write("CONGESTED STREETS (> 500 vehicles)\n")
      f.write("---------------------------")
      for street, volume in congested_streets:
        f.write(f"{street} ({volume} vehicles)\n")
      
district_totals, congested_streets = analyze_traffic_flow("traffic_survey.txt")
write_traffic_report(district_totals, congested_streets)



               

                



