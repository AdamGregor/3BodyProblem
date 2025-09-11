import numpy as np
from test_data import test_data
import sim_step
import misc



# def test_case(value):   
#      # Alien glyph-like characters
#     glyphs = ["Ξ", "Φ", "Ω", "Ψ", "λ", "¤", "§", "Ø", "∆", "≡", "⊗", "⋆"]

#     # Simulated transmission effect
#     print("[Initiating Intergalactic Transmission...]\n")

#     # Static noise effect
#     print("".join(random.choice(glyphs) for _ in range(25)))

#     # Sci-fi style boolean output
#     if value:
#         print("☢ TRANSMISSION STATUS: ✅ TRUE ☢")
#     else:
#         print("☢ TRANSMISSION STATUS: ❌ FALSE ☢")
#     print()


def main():
    #INITIAL SETTING
    G= 1

    t_0 = 0
    t_end = 20
    t_delta = 0.01
    t_frames = int((t_end - t_0) / t_delta)

    m_1 = 1.0
    m_2 = 1.0
    m_3 = 1.0

    # Position
    positions = np.zeros((t_frames+1, 3, 3)) #frame, object, xyz
    positions[0,0,:] = np.array([0.97000436, -0.24308753,  0.0])
    positions[0,1,:] = np.array([-0.9700436,  0.24308753,  0.0])
    positions[0,2,:] = np.array([0.0,  0.0,  0.0])

    # Velocity
    vel_1 =  np.array([0.93240737/2, 0.86473/2, 0])
    vel_2 =  np.array([0.93240737/2, 0.86473/2, 0.0])
    vel_3 =  np.array([-0.93240737, -0.86473146, 0.0])

    all_correct = True
    no_test = 1
    for i in range(t_frames):
        p = positions[i, :, :]
        p_n1, p_n2, p_n3, vel_1, vel_2 , vel_3 = sim_step.calculate_step(p[0], p[1], p[2], vel_1, vel_2, vel_3, m_1, m_2, m_3, t_delta, G) 
        positions[i+1, 0] = p_n1 
        positions[i+1, 1] = p_n2 
        positions[i+1, 2] = p_n3

        if(i in test_data):
            fits = ([p_n1, p_n2, p_n3] - test_data[i]) < test_data['eps']
            misc.test_case(no_test, fits.all())
            no_test += 1
            all_correct = all_correct and fits.all()


    misc.overall_result(all_correct)
    if not all_correct:
        return

    misc.send_message()
    misc.do_animation(positions, t_frames)
    misc.waiting_spin(5, "WAITING FOR RESPONSE")
    misc.loading_bar(10, "RECIEVING MESSAGE")
    misc.print_alien(20)
    misc.loading_bar(3, "DECODING TO ["+ misc.COLORS[4]+"C"+misc.COLORS[2]+"ZE"+misc.COLORS[3]+"CH"+misc.RESET+"]")
    misc.print_ending()

if __name__ == "__main__":
    main()