import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

COLORS = [
    "\033[92m",  # Green
    "\033[93m",  # Yellow
    "\033[91m",  # Red
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
    for _ in range(10):
        time.sleep(0.2)
        print()

    text = "TRANSMITTING DATA TO " + COLORS[1] +"TRISOL"+RESET

    for i in range(len(text)):
        time.sleep(0.25)
        print(text[0:i], end="\r")
        if(i > len("TRANSMITTING DATA TO ")):
            print(RESET, end="\r")
    print(text)

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
        # print(percents, no_sharps)
        last = True
        for i in range(row_len):
            if i == 0:
                print('[', end="")
            
            elif i <= no_sharps:
                print(COLORS[1]+"#"+RESET, end="")

            elif i == row_len - 1:
                print("]", end="\r")

            else:
                print(".", end="")
                last = False
        
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
    #TODO opravit
    def close_event(*args):
        print("tadyyk")
        plt.close(fig)
    
    ani._stop = lambda *args, **kwargs: (
        animation.Animation._stop(ani, *args, **kwargs),
        close_event()
    )
    plt.show()