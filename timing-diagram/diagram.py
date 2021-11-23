import os
import subprocess

SPEED_FACTOR=1
LOW_BASE_FREQ=1000
HIGH_BASE_FREQ=1050
SECTION_DIFF=-200

## ADVANCED CONFIG
SAMPLE_RATE=10000
## END OF CONFIG

example_new="1 0@1.33 1@3.3 0@3.5 1@3.6 0@3.8"

def get_args(args):
  a = args.split("@")
  return (a[0], float(a[1]))

def convert(syn):
  first_state = syn[0]
  slist = syn.split(" ")[1:]
  tarr = list()
  tarr.append((first_state,))
  time_offset = 0
  for ti in range(len(slist)):
    state, time = get_args(slist[ti])
    tarr[ti] = (tarr[ti][0], time-time_offset)
    time_offset = time
    tarr.append((state,))
  tarr[len(tarr)-1] = (tarr[len(tarr)-1][0], 100)
  return tarr

def create_commands(example):
  return [f"sox -r 10000 -n _tmp_exmp.wav synth {example[i][1]} sine {1000 + (i*50)}" for i in range(len(example))]
    
print(create_commands(convert(example_new)))
exit(1)

LBF=str(LOW_BASE_FREQ)
HBF=str(HIGH_BASE_FREQ)

METRONOME_CLOCK=MC=f"sox -r {str(SAMPLE_RATE)} -n metronome.wav synth .005 sine 4000".split(" ")

SPEED_FACTOR=SF=SPEED_FACTOR**-1

SINE_LINE = ((f"{LBF} {SF} {HBF} {SF} ") * 10).strip(" ")

def add_metronome(file_name):
    if not os.path.exists("metronome.wav"):
      subprocess.call(MC)
    subprocess.run(["sox", "--combine", "merge", f"{file_name}", "metronome.wav", f"{file_name}_met.wav"])
    subprocess.run(["mv", f"{file_name}_met.wav", f"{file_name}"])

def create_tones(tone_list, final_name):
  split_line = SINE_LINE.split(" ")
  idex = range(0, len(split_line), 2)

  for i in idex:
    print(f"sox -r 10000 -n _tmp_output_{str(i)}.wav synth {split_line[i+1]} sine {split_line[i]}")
    subprocess.run(["sox", "-r", "10000", "-n", f"_tmp_output_{str(i)}.wav", "synth", split_line[i+1], "sine", split_line[i]])
    add_metronome(f"_tmp_output_{str(i)}.wav")

  files = [f"_tmp_output_{str(i)}_met.wav" for i in idex]
  subprocess.call(["sox", *files, f"{final_name}.wav"])
  #subprocess.call(["rm", "_tmp_output_*"])

create_tones(SINE_LINE, "final")
