import time
import bme280
import phant

def main():

    post = phant.Phant("zD9obXl4K3UM1E0MY5q2", "privateKey")
    (chip_id, chip_version) = bme280.readBME280ID()
    total_temp =0
    total_pressure = 0
    total_humidity = 0
    cycle_counter =0
    print "Chip ID     :", chip_id
    print "Version     :", chip_version
    while 1:
        temperature, pressure, humidity = bme280.readBME280All()
        total_temp += temperature
        total_pressure += pressure
        total_humidity += humidity
        cycle_counter+=1
        time.sleep(1)
        if(cycle_counter == 60):
            post.post_data("{0:.2f}".format(total_humidity/cycle_counter), "{0:.2f}".format(total_pressure/cycle_counter), "{0:.2f}".format(total_temp/cycle_counter))
            print "Temperature : ", total_temp/cycle_counter, "C"
            print "Pressure : ", total_pressure/cycle_counter, "hPa"
            print "Humidity : ", total_humidity/cycle_counter, "%"
            total_pressure = total_temp = total_humidity = cycle_counter = 0


if __name__ == "__main__":
        main()