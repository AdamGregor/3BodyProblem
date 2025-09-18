from color_text import ColorRow
import ending
import time, random 
import matplotlib.pyplot as plt
import matplotlib.animation as animation

COLORS = [
    "\033[92m",  # Green
    "\033[93m",  # Yellow
    "\033[91m",  # Red
    "\033[94m",  # Blue
    "\033[97m"   # White
]
RESET = "\033[0m"

def sharps():
    return "###################################################"

def test_case(test_no, value):
    print(sharps())
    print("TEST ", test_no, " FINISHED ", end="")
    time.sleep(0.66)
    print(COLORS[0] + "SUCCESFULLY" if value else COLORS[2]+ "INCORRECTLY", RESET)

def send_message():
    for _ in range(3):
        time.sleep(0.2)
        print()

    text = ColorRow().t("TRANSMITTING DATA TO ").yellow("TRISOL")
    text.print_typed(sleep=0.25)

def render_loading(row_len, sharps):
    last = True
    for i in range(row_len):
        if i == 0:
            print('[', end="")
        
        elif i <= sharps:
            print(COLORS[1]+"#"+RESET, end="")

        elif i == row_len - 1:
            print("]", end="\r")

        else:
            print(".", end="")
            last = False

    return last

def overall_result(value):
    for _ in range(3):
        time.sleep(0.2)
        print(sharps())

    if value:
        text = "ALL TESTS " + COLORS[0] + " PASSED SUCCESFULLY" + RESET
    else:
        text = COLORS[2] + "ERROR IN SOME TEST CASES, CHECK YOUR IMPLEMENTATION" + RESET

    for _ in range(3):
        print(text, end="\r")
        time.sleep(0.5)
        print(" "*len(text), end="\r")
        time.sleep(0.5)
    print(text)
    time.sleep(0.5)    
    print(sharps())


def do_animation(positions, t_frames):
    p1x_sol = positions[:, 0, 0]
    p1y_sol = positions[:, 0, 1]
    p1z_sol = positions[:, 0, 2]

    p2x_sol = positions[:, 1, 0]
    p2y_sol = positions[:, 1, 1]
    p2z_sol = positions[:, 1, 2]

    p3x_sol = positions[:, 2, 0]
    p3y_sol = positions[:, 2, 1]
    p3z_sol = positions[:, 2, 2]
    # ------------------------------------------------------------------- #

    fig, ax = plt.subplots(subplot_kw={"projection":"3d"})

    planet1_plt, = ax.plot(p1x_sol, p1y_sol, p1z_sol, 'green', label='V2500', linewidth=1)
    planet2_plt, = ax.plot(p2x_sol, p2y_sol, p2z_sol, 'red', label='υ3 Eridani', linewidth=1)
    planet3_plt, = ax.plot(p3x_sol, p3y_sol, p3z_sol, 'blue',label='LHS 3844', linewidth=1)

    planet1_dot, = ax.plot([p1x_sol[-1]], [p1y_sol[-1]], [p1z_sol[-1]], 'o', color='green', markersize=6)
    planet2_dot, = ax.plot([p2x_sol[-1]], [p2y_sol[-1]], [p2z_sol[-1]], 'o', color='red', markersize=6)
    planet3_dot, = ax.plot([p3x_sol[-1]], [p3y_sol[-1]], [p3z_sol[-1]], 'o', color='blue', markersize=6)


    ax.set_title("The 3 Sun Problem")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    plt.grid()
    plt.legend()
    
    def update(frame):
        percents = (frame+1) / t_frames * 100
        row_len = len(sharps())
        percent = (row_len - 2) / 100
        no_sharps = int(percents * percent + 1 )
        
        last = render_loading(row_len, no_sharps)
        
        if last:
            plt.close()
            print()

        x_current_1 = p1x_sol[0:frame+1]
        y_current_1 = p1y_sol[0:frame+1]
        z_current_1 = p1z_sol[0:frame+1]

        x_current_2 = p2x_sol[0:frame+1]
        y_current_2 = p2y_sol[0:frame+1]
        z_current_2 = p2z_sol[0:frame+1]

        x_current_3 = p3x_sol[0:frame+1]
        y_current_3 = p3y_sol[0:frame+1]
        z_current_3 = p3z_sol[0:frame+1]

        planet1_plt.set_data(x_current_1, y_current_1)  
        planet1_plt.set_3d_properties(z_current_1)

        planet1_dot.set_data([x_current_1[-1]], [y_current_1[-1]])
        planet1_dot.set_3d_properties([z_current_1[-1]])



        planet2_plt.set_data(x_current_2, y_current_2)  
        planet2_plt.set_3d_properties(z_current_2)

        planet2_dot.set_data([x_current_2[-1]], [y_current_2[-1]])
        planet2_dot.set_3d_properties([z_current_2[-1]])

        planet3_plt.set_data(x_current_3, y_current_3)  
        planet3_plt.set_3d_properties(z_current_3)

        planet3_dot.set_data([x_current_3[-1]], [y_current_3[-1]])
        planet3_dot.set_3d_properties([z_current_3[-1]])

        return planet1_plt, planet1_dot, planet2_plt, planet2_dot, planet3_plt, planet3_dot 




    ani = animation.FuncAnimation(
        fig,
        update,
        frames=range(0, t_frames, 5),
        interval=10,
        blit = False,
        repeat = False
    )

    # Close figure automatically when animation completes
    def close_event(*args):
        print("tadyyk")
        plt.close(fig)
    
    ani._stop = lambda *args, **kwargs: (
        animation.Animation._stop(ani, *args, **kwargs),
        close_event()
    )
    plt.show()

def waiting_spin(cycles, text=''):
    phases = ['|', '/', '-', '\\', '|', '/', '-', '\\']
    for _ in range(cycles):
        for sign in phases:
            print(text + '['+sign+']', end='\r')
            time.sleep(0.25)
    print()

def loading_bar(seconds, text):
    print("\n"+text)
    
    percent = seconds/100
    for i in range(101): 
        time.sleep(percent)
        n_sharps = int((len(sharps())-2) * (i/100))
        render_loading(len(sharps()), n_sharps)
    print()

def print_alien(rows):
    glyphs = ["Ξ", "Φ", "Ω", "Ψ", "λ", "¤", "§", "Ø", "∆", "≡", "⊗", "⋆", ' ', ' ']
    row_size = 60

    for _ in range(rows):
        row = []
        for _ in range(row_size):
            letter = glyphs[random.randrange(len(glyphs))] 
            if letter == ' ' and len(row) == 0:
                continue
            elif letter == '\n':
                break
            row += letter
            print(''.join(row), end='\r')
            time.sleep(0.01)
        time.sleep(0.1)
        print()

def print_ending():
    for row in ending.text:
        curr_row = []
        for letter in row:
            curr_row += letter
            print(''.join(curr_row), end="\r")
            time.sleep(0.05)
        time.sleep(0.1)
        print()
