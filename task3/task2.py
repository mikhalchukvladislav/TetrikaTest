def time_range(data):
    for i in range(1, len(data), 1):
        if data[i] < data[i - 1]:
            data[i] = data[i - 1]
    return list(set(data))


def appearance(intervals):
    lesson_start = intervals['lesson'][0]
    lesson_stop = intervals['lesson'][1]
    pupils_time = intervals['pupil']
    tutor_time = intervals['tutor']

    time_range(pupils_time)
    time_range(tutor_time)

    pupil_in = False
    tutor_in = False

    together_time = 0
    start_time_together = 0

    while pupils_time and tutor_time:
        if tutor_time[0] < pupils_time[0]:
            time_in_out = tutor_time.pop(0)
            tutor_in = not tutor_in
        else:
            time_in_out = pupils_time.pop(0)
            pupil_in = not pupil_in

        if pupil_in and tutor_in:
            start_time_together = time_in_out
        else:
            if start_time_together:
                if (start_time_together < lesson_start) and (time_in_out > lesson_stop):
                    start_time_together = lesson_start
                    time_in_out = lesson_stop
                elif time_in_out > lesson_stop:
                    time_in_out = lesson_stop
                elif start_time_together < lesson_start:
                    start_time_together = lesson_start
                together_time += time_in_out - start_time_together
                start_time_together = 0
    return together_time
