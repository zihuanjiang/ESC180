def initialize():

    global cur_hedons, cur_health

    global cur_time
    global last_activity, last_activity_duration

    global last_finished
    global bored_with_stars
    global tired
    global cur_star, cur_star_activity
    global estimate_hedons_running, estimate_hedons_textbooks
    global star_time

    star_time = []
    cur_hedons = 0
    cur_health = 0

    estimate_hedons_running = 0
    estimate_hedons_textbooks = 0


    cur_star = None       
    cur_star_activity = None

    bored_with_stars = False 
    tired = False

    last_activity = None
    last_activity_duration = 0

    cur_time = 0

    last_finished = -1000

def get_bored_with_star():
    global cur_star_activity
    if len(star_time) <= 2:
        return False
    else:
        for i in range(0,len(star_time)-2):
            if star_time[i+2] - star_time[i] < 120:
                cur_star_activity = None
                return True

def offer_star(activity):
    global cur_star_activity, cur_time, star_time
    star_time.append(cur_time)
    cur_star_activity = activity

def star_can_be_taken(activity):
    global cur_star_activity
    if get_bored_with_star() == True:
        return False
    else:
        if activity == cur_star_activity:
            return True
        else:
            return False


def perform_activity(activity, duration):
    global cur_health, cur_hedons, cur_time, cur_star_activity
    global last_activity, last_activity_duration, tired

    get_bored_with_star()
    if (last_activity == "resting" and last_activity_duration >= 120) or \
    last_activity == None or \
    (last_activity == "resting" and last_activity_duration == cur_time):
        tired = False
    else:
        tired = True

    cur_time += duration
    if last_activity != "running" and activity == "running" and \
    cur_star_activity != "running":
        if duration <= 10:
            cur_health += 3 * duration
            if tired == False:
                cur_hedons += 2 * duration
            if tired == True:
                cur_hedons -= 2 * duration

        if duration > 10 and duration <= 180:
            cur_health += 3 * duration
            if tired == False:
                cur_hedons = cur_hedons + 40 - 2 * duration
            if tired == True:
                cur_hedons = cur_hedons - 2 * duration

        if duration > 180:
            cur_health += 360 + duration
            if tired == False:
                cur_hedons = cur_hedons + 40 - 2 * duration
            if tired == True:
                cur_hedons = cur_hedons - 2 * duration
        last_activity = "running"
        last_activity_duration = duration
        cur_star_activity = None

    elif last_activity != "running" and activity == "running" and \
    cur_star_activity == "running":
        if duration <= 10:
            cur_health += 3 * duration
            if tired == False:
                cur_hedons += 5 * duration
            if tired == True:
                cur_hedons += duration

        if duration > 10 and duration <= 180:
            cur_health = cur_health + 3 * duration
            if tired == False:
                cur_hedons = cur_hedons + 40 - 2 * duration + 30
            if tired == True:
                cur_hedons = cur_hedons - 2 * duration + 30

        if duration > 180:
            cur_health += 360 + duration
            if tired == False:
                cur_hedons = cur_hedons + 40 - 2 * duration + 30
            if tired == True:
                cur_hedons = cur_hedons - 2 * duration + 30
        last_activity = "running"
        last_activity_duration = duration
        cur_star_activity = None

    elif last_activity == "running" and activity == "running" and \
    cur_star_activity != "running":
        total_duration = last_activity_duration + duration
        if total_duration <= 10:
            cur_health += 3 * duration
            cur_hedons -= 2 * duration

        if total_duration > 10 and total_duration <= 180:
            cur_health += 3 * duration
            cur_hedons = cur_hedons - 2 * duration

        if total_duration > 180:
            cur_health += 3 * (180 - last_activity_duration) + \
            total_duration - 180

            cur_hedons = cur_hedons - 2 * duration
        last_activity = "running"
        last_activity_duration = total_duration
        cur_star_activity = None

    elif last_activity == "running" and activity == "running" and \
    cur_star_activity == "running":
        total_duration = last_activity_duration + duration
        if duration <= 10:
            if total_duration <= 10:
                cur_health += 3 * duration
                cur_hedons -= 2 * duration + 3 * duration

            if total_duration > 10 and total_duration <= 180:
                cur_health += 3 * duration
                cur_hedons = cur_hedons - 2 * duration + 3 * duration

            if total_duration > 180:
                cur_health += 3 * (180 - last_activity_duration) + \
                total_duration - 180

                cur_hedons = cur_hedons - 2 * duration + 3 * duration
        if duration > 10:
            if total_duration <= 10:
                cur_health += 3 * duration
                cur_hedons -= 2 * duration + 30

            if total_duration > 10 and total_duration <= 180:
                cur_health += 3 * duration
                cur_hedons = cur_hedons - 2 * duration + 30

            if total_duration > 180:
                cur_health += 3 * (180 - last_activity_duration) + \
                total_duration - 180

                cur_hedons = cur_hedons - 2 * duration + 30

            last_activity = "running"
            last_activity_duration = total_duration
            cur_star_activity = None

    elif last_activity != "textbooks" and activity == "textbooks" and \
    cur_star_activity != "textbooks":
        cur_health += 2 * duration

        if duration <= 20:
            if tired == False:
                cur_hedons = cur_hedons + duration
            if tired == True:
                cur_hedons = cur_hedons - 2 * duration

        if duration > 20:
            if tired == False:
                cur_hedons = cur_hedons + 40 - duration
            if tired == True:
                cur_hedons = cur_hedons - 2 * duration
        last_activity = "textbooks"
        last_activity_duration = duration
        cur_star_activity = None

    elif last_activity != "textbooks" and activity == "textbooks" and \
    cur_star_activity == "textbooks":
        cur_health += 2 * duration

        if duration <= 10:
            if tired == False:
                cur_hedons = cur_hedons + 4 * duration
            if tired == True:
                cur_hedons = cur_hedons + duration

        if duration > 10 and duration <= 20:
            if tired == False:
                cur_hedons = cur_hedons + duration + 30
            if tired == True:
                cur_hedons = cur_hedons - 2 * duration + 30

        if duration > 20:
            if tired == False:
                cur_hedons = cur_hedons + 70 - duration
            if tired == True:
                cur_hedons = cur_hedons - 2 * duration + 30
        last_activity = "textbooks"
        last_activity_duration = duration
        cur_star_activity = None


    elif last_activity == "textbooks" and activity == "textbooks" and \
    cur_star_activity != "textbooks":
        cur_health += 2 * duration
        cur_hedons -= 2 * duration
        last_activity = "textbooks"
        last_activity_duration += duration
        cur_star_activity = None


    elif last_activity == "textbooks" and activity == "textbooks" and \
    cur_star_activity == "textbooks":
        total_duration = last_activity_duration + duration
        cur_health += 2 * duration

        if duration <= 10:
            cur_hedons += duration

        if duration > 10:
            cur_hedons = cur_hedons - 2 * duration + 30
        last_activity = "textbooks"
        last_activity_duration += duration
        cur_star_activity = None

    elif last_activity != "resting" and activity == "resting":
        last_activity = "resting"
        last_activity_duration = duration
        cur_star_activity = None

    elif last_activity == "resting" and activity == "resting":
        last_activity = "resting"
        last_activity_duration += duration
        cur_star_activity = None


def get_cur_hedons():
    return cur_hedons

def get_cur_health():
    return cur_health


def estimate_hedons_delta_running():
    global estimate_hedons_running, tired, last_activity
    global last_activity_duration
    if last_activity == None:
        if cur_star_activity != "running":
            estimate_hedons_running = 2
        if cur_star_activity == "running":
            estimate_hedons_running = 5
    elif last_activity == "running" or last_activity == "textbooks":
        if cur_star_activity != "running":
            estimate_hedons_running = -2
        if cur_star_activity == "running":
            estimate_hedons_running = 1
    elif last_activity == "resting":
        if cur_time == last_activity_duration:
            if cur_star_activity != "running":
                estimate_hedons_running = 2
            if cur_star_activity == "running":
                estimate_hedons_running = 5
        elif cur_time != last_activity_duration:
            if cur_star_activity != "running":
                if last_activity_duration < 120:
                    estimate_hedons_running = -2
                elif last_activity_duration >= 120:
                    estimate_hedons_running = 2
            if cur_star_activity == "running":
                if last_activity_duration < 120:
                    estimate_hedons_running = 1
                elif last_activity_duration >= 120:
                    estimate_hedons_running = 5
    return estimate_hedons_running


def estimate_hedons_delta_textbooks():
    global estimate_hedons_textbooks, tired, last_activity
    global last_activity_duration
    if last_activity == None:
        if cur_star_activity != "textbooks":
            estimate_hedons_textbooks = 1
        if cur_star_activity == "textbooks":
            estimate_hedons_textbooks = 4
    elif last_activity == "running" or last_activity == "textbooks":
        if cur_star_activity != "textbooks":
            estimate_hedons_textbooks = -2
        if cur_star_activity == "textbooks":
            estimate_hedons_textbooks = 1
    elif last_activity == "resting":
        if cur_time == last_activity_duration:
            if cur_star_activity != "textbooks":
                estimate_hedons_textbooks = 1
            if cur_star_activity == "textbooks":
                estimate_hedons_textbooks = 4
        elif cur_time != last_activity_duration:
            if cur_star_activity != "textbooks":
                if last_activity_duration < 120:
                    estimate_hedons_textbooks = -2
                elif last_activity_duration >= 120:
                    estimate_hedons_textbooks = 1
            if cur_star_activity == "textbooks":
                if last_activity_duration < 120:
                    estimate_hedons_textbooks = 1
                elif last_activity_duration >= 120:
                    estimate_hedons_textbooks = 4
    return estimate_hedons_textbooks

def most_fun_activity_minute():
    global estimate_hedons_running, estimate_hedons_textbooks

    estimate_hedons_delta_running()
    estimate_hedons_delta_textbooks()
    if estimate_hedons_running < 0 and estimate_hedons_textbooks < 0:
        return "resting"
    elif estimate_hedons_running > estimate_hedons_textbooks:
        return "running"
    elif estimate_hedons_running < estimate_hedons_textbooks:
        return "textbooks"





###############################################################################
if __name__ == '__main__':
    initialize()
    perform_activity("running", 30)
    print(get_cur_hedons())            # -20 = 10 * 2 + 20 * (-2)             # Test 1
    print(get_cur_health())            # 90 = 30 * 3                          # Test 2
    print(most_fun_activity_minute())  # resting                              # Test 3
    perform_activity("resting", 30)
    offer_star("running")

    print(star_can_be_taken("running"))
    print(most_fun_activity_minute())  # running                              # Test 4
    perform_activity("textbooks", 30)
    print(get_cur_health())            # 150 = 90 + 30*2                      # Test 5
    print(get_cur_hedons())            # -80 = -20 + 30 * (-2)                # Test 6
    offer_star("running")
    perform_activity("running", 20)
    print(get_cur_health())            # 210 = 150 + 20 * 3                   # Test 7
    print(get_cur_hedons())            # -90 = -80 + 10 * (3-2) + 10 * (-2)   # Test 8
    perform_activity("running", 170)
    print(get_cur_health())            # 700 = 210 + 160 * 3 + 10 * 1         # Test 9
    print(get_cur_hedons())            # -430 = -90 + 170 * (-2)              # Test 10

