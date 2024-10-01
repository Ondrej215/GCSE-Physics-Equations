from tkinter import *
import random
import sys

class formula:
    def __init__(self, name, numbers, sub_fraction_numbers, power, description, letter_equation, variable_one,
                 variable_two, variable_three, variable_four, variable_five, order_doesnt_matter,
                 answer_unit, variable_one_unit, variable_two_unit, variable_three_unit, variable_four_unit, variable_five_unit):
        self.name = name
        self.numbers = numbers # amount of numbers over fraction line, 1 2 3, 4
        self.subfraction_numbers = sub_fraction_numbers # amount of numbers under fraction line, 0 or 1
        self.power = power # 0 if no power, 1 if power at the end
        self.description = description # includes units and use of the formula
        self.letter_equation = letter_equation
        self.variable_one = variable_one # first variable of the equation above fraction line
        self.variable_two = variable_two # second variable above fraction line
        self.variable_three = variable_three # third variable above fraction line
        self.variable_four = variable_four # fourth variable above fraction line
        self.variable_five = variable_five # fifth variable above fraction line
        self.order_doesnt_matter = order_doesnt_matter
        self.answer_unit = answer_unit
        self.variable_one_unit = variable_one_unit
        self.variable_two_unit = variable_two_unit
        self.variable_three_unit = variable_three_unit
        self.variable_four_unit = variable_four_unit
        self.variable_five_unit = variable_five_unit

def place_main_menu():

    def higher_checkbox_toggle():
        if higher_checkbox.cget("text") == "✓":
            higher_checkbox.configure(text="")
        else:
            higher_checkbox.configure(text="✓")

    def place_test_all_equations():

        # clears window
        for child in window.winfo_children():
            child.destroy()

        equation_name = Label(window, bg="#1A2434", fg="white", text="Equation Name Goes Here", font=("Calibri", 28))
        equation_name.place(relx=0.3, rely=0.0, relwidth=0.4, relheight=0.1)

        equation_unit = StringVar()
        equation_unit.set("Pick Unit...")

        equation_unit_pick = OptionMenu(window, equation_unit, *units)
        equation_unit_pick.config(bg="#273142", fg="white")
        equation_unit_pick["menu"].config(bg="#273142", fg="white")
        equation_unit_pick.place(relx=0.4, rely=0.12, relwidth=0.2, relheight=0.06)

        element_one = Entry(window, bg="white", fg="black", font=("Calibri", 17))
        element_one.place(relx=0.055, rely=0.4, relwidth=0.2, relheight=0.06)

        operator_one = Label(window, text="x", fg="white", bg="#1A2434", font=("Calibri", 20))
        operator_one.place(relx=0.255, rely=0.4, relwidth=0.03, relheight=0.06)

        element_two = Entry(window, bg="white", fg="black", font=("Calibri", 17))
        element_two.place(relx=0.285, rely=0.4, relwidth=0.2, relheight=0.06)

        operator_two = Label(window, text="x", fg="white", bg="#1A2434", font=("Calibri", 20))
        operator_two.place(relx=0.485, rely=0.4, relwidth=0.03, relheight=0.06)

        element_three = Entry(window, bg="white", fg="black", font=("Calibri", 17))
        element_three.place(relx=0.515, rely=0.4, relwidth=0.2, relheight=0.06)

        operator_three = Label(window, text="+", fg="white", bg="#1A2434", font=("Calibri", 20))
        operator_three.place(relx=0.715, rely=0.4, relwidth=0.03, relheight=0.06)

        element_four = Entry(window, bg="white", fg="black", font=("Calibri", 17))
        element_four.place(relx=0.745, rely=0.4, relwidth=0.2, relheight=0.06)

        operator_four = Label(window, bg="white")
        operator_four.place(relx=0.055, rely=0.5, relwidth=0.2, relheight=0.001)

        element_five = Entry(window, bg="white", fg="black", font=("Calibri", 17))
        element_five.place(relx=0.055, rely=0.54, relwidth=0.2, relheight=0.06)

        squared_one = Label(window, bg="#1A2434", fg="white", text="2", font=("Calibri", 17))
        squared_one.place(relx=0.715, rely=0.34, relwidth=0.03, relheight=0.06)

        squared_two = Label(window, bg="#1A2434", fg="white", text="2", font=("Calibri", 17))
        squared_two.place(relx=0.945, rely=0.34, relwidth=0.03, relheight=0.06)

        unit_one = StringVar()

        unit_one_pick = OptionMenu(window, unit_one, *units)
        unit_one_pick.config(bg="#273142", fg="white")
        unit_one_pick["menu"].config(bg="#273142", fg="white")
        unit_one_pick.place(relx=0.055, rely=0.32, relwidth=0.2, relheight=0.06)

        unit_two = StringVar()

        unit_two_pick = OptionMenu(window, unit_two, *units)
        unit_two_pick.config(bg="#273142", fg="white")
        unit_two_pick["menu"].config(bg="#273142", fg="white")
        unit_two_pick.place(relx=0.285, rely=0.32, relwidth=0.2, relheight=0.06)

        unit_three = StringVar()

        unit_three_pick = OptionMenu(window, unit_three, *units)
        unit_three_pick.config(bg="#273142", fg="white")
        unit_three_pick["menu"].config(bg="#273142", fg="white")
        unit_three_pick.place(relx=0.515, rely=0.32, relwidth=0.2, relheight=0.06)

        unit_four = StringVar()

        unit_four_pick = OptionMenu(window, unit_four, *units)
        unit_four_pick.config(bg="#273142", fg="white")
        unit_four_pick["menu"].config(bg="#273142", fg="white")
        unit_four_pick.place(relx=0.745, rely=0.32, relwidth=0.2, relheight=0.06)

        unit_five = StringVar()

        unit_five_pick = OptionMenu(window, unit_five, *units)
        unit_five_pick.config(bg="#273142", fg="white")
        unit_five_pick["menu"].config(bg="#273142", fg="white")
        unit_five_pick.place(relx=0.055, rely=0.62, relwidth=0.2, relheight=0.06)

        equation_description = Label(window, text="Equation Description Goes Here", font=("Calibri", 14), bg="#1a2434", fg="white")
        equation_description.place(relx=0.2, rely=0.7, relwidth=0.6, relheight=0.15)

        letter_equation = Label(window, text="Word equation here", font=("Calibri", 15), bg="#1a2434", fg="white")
        letter_equation.place(relx=0.25, rely=0.81, relwidth=0.5, relheight=0.15)

        equation_widgets = [[element_two, unit_two_pick, operator_one], [element_three, unit_three_pick, operator_two],
                            [element_four, unit_four_pick, operator_three, squared_two], [element_five, unit_five_pick, operator_four]]

        def check():
            global score
            equation = equations[-1]
            next_button.config(text="Next", command=next_equation)
            letter_equation.config(text=equation.letter_equation)

            unit_one_picked = unit_one.get()
            element_one_picked = element_one.get().strip().lower()
            if equation.numbers > 1:
                unit_two_picked = unit_two.get()
                element_two_picked = element_two.get().strip().lower()
                if equation.numbers > 2:
                    unit_three_picked = unit_three.get()
                    element_three_picked = element_three.get().strip().lower()
                    if equation.numbers > 3:
                        unit_four_picked = unit_four.get()
                        element_four_picked = element_four.get().strip().lower()

            if equation.subfraction_numbers == 1:
                unit_five_picked = unit_five.get()
                element_five_picked = element_five.get().strip().lower()

            answer_unit_picked = equation_unit.get()



            if equation.answer_unit is not None:
                equation_unit_pick.config(bg="green" if answer_unit_picked == equation.answer_unit else "red")
            if equation.variable_one_unit is not None:
                unit_one_pick.config(bg="green" if unit_one_picked == equation.variable_one_unit else "red")
            element_one.config(bg="green" if element_one_picked in equation.variable_one else "red")
            if equation.numbers > 1:
                unit_two_pick.config(bg="green" if unit_two_picked == equation.variable_two_unit else "red")
                element_two.config(bg="green" if element_two_picked in equation.variable_two else "red")
                if equation.numbers > 2:
                    unit_three_pick.config(bg="green" if unit_three_picked == equation.variable_three_unit else "red")
                    element_three.config(bg="green" if element_three_picked in equation.variable_three else "red")
                    if equation.numbers > 3:
                        unit_four_pick.config(bg="green" if unit_four_picked == equation.variable_four_unit else "red")
                        element_four.config(bg="green" if element_four_picked in equation.variable_four else "red")

            if equation.subfraction_numbers == 1:
                unit_five_pick.config(bg="green" if unit_five_picked == equation.variable_five_unit else "red")
                element_five.config(bg="green" if element_five_picked in equation.variable_five else "red")

            # does calculations for score
            if equation_unit_pick.cget("bg") == "green":
                print("Equation unit right")
                score += 1

            if unit_one_pick.cget("bg") == "green" and element_one.cget("bg") == "green":
                print("one right")
                score += 1

            if unit_two_pick.cget("bg") == "green" and element_two.cget("bg") == "green":
                print("two right")
                score += 1

            if unit_three_pick.cget("bg") == "green" and element_three.cget("bg") == "green":
                print("three right")
                score += 1

            if unit_four_pick.cget("bg") == "green" and element_four.cget("bg") == "green":
                print("four right")
                score += 1

            if unit_five_pick.cget("bg") == "green" and element_five.cget("bg") == "green":
                print("five right")
                score += 1

            print(f"score is: {score}")

            equations.pop()
            # if program is done
            if len(equations) == 0:
                for child in window.winfo_children():
                    child.destroy()

                print(f"final score is: {score}")#3

                Label(window, text=f"accuracy: {int((score/87)*100)}%", bg="#323B4C", fg="white", font=("Calibri", 18)).place(relx=0.35, rely=0.8,
                                                                                                                        relwidth=0.3, relheight=0.1)

                Label(bg="#1a2434", fg="white", font=("Calibri", 40), text="End").place(relx=0.3, rely=0.4, relwidth=0.4, relheight=0.2)
                Button(window, text="End Program", font=("Calibri", 23), bg="#23a2e8", fg="white", command=sys.exit).place(relx=0.4, rely=0.6,
                                                                                                                                       relwidth=0.2, relheight=0.1)


        def next_equation():
            equation = equations[-1]

            unit_one.set("Pick Unit...")
            unit_two.set("Pick Unit...")
            unit_three.set("Pick Unit...")
            unit_four.set("Pick Unit...")
            unit_five.set("Pick Unit...")
            equation_unit.set("Pick Unit...")

            equation_unit_pick.config(bg="#273142")
            unit_one_pick.config(bg="#273142")
            unit_two_pick.config(bg="#273142")
            unit_three_pick.config(bg="#273142")
            unit_four_pick.config(bg="#273142")
            unit_five_pick.config(bg="#273142")
            element_one.config(bg="white")
            element_two.config(bg="white")
            element_three.config(bg="white")
            element_four.config(bg="white")
            element_five.config(bg="white")
            element_one.delete(0, "end")
            element_two.delete(0, "end")
            element_three.delete(0, "end")
            element_four.delete(0, "end")
            element_five.delete(0, "end")

            for i in equation_widgets:
                for j in i:
                    j.place_forget()

            if equation.power == 1:
                squared_one.place(relx=0.715, rely=0.34, relwidth=0.03, relheight=0.06)
            else:
                squared_one.place_forget()

            if equation.numbers > 1:
                element_two.place(relx=0.285, rely=0.4, relwidth=0.2, relheight=0.06)
                operator_one.place(relx=0.255, rely=0.4, relwidth=0.03, relheight=0.06)
                unit_two_pick.place(relx=0.285, rely=0.32, relwidth=0.2, relheight=0.06)
                if equation.numbers > 2:
                    element_three.place(relx=0.515, rely=0.4, relwidth=0.2, relheight=0.06)
                    operator_two.place(relx=0.485, rely=0.4, relwidth=0.03, relheight=0.06)
                    unit_three_pick.place(relx=0.515, rely=0.32, relwidth=0.2, relheight=0.06)
                    if equation.numbers > 3:
                        element_four.place(relx=0.745, rely=0.4, relwidth=0.2, relheight=0.06)
                        operator_three.place(relx=0.715, rely=0.4, relwidth=0.03, relheight=0.06)
                        unit_four_pick.place(relx=0.745, rely=0.32, relwidth=0.2, relheight=0.06)
                        squared_two.place(relx=0.945, rely=0.34, relwidth=0.03, relheight=0.06)

            if equation.subfraction_numbers == 1:
                element_five.place(relx=0.055, rely=0.54, relwidth=0.2, relheight=0.06)
                operator_four.place(relx=0.055, rely=0.5, relwidth=0.2, relheight=0.001)
                unit_five_pick.place(relx=0.055, rely=0.62, relwidth=0.2, relheight=0.06)


            equation_name.config(text=equation.name)
            equation_description.config(text=equation.description)
            letter_equation.config(text="")

            next_button.config(text="Check", command=check)

        next_button = Button(window, text="Check", font=("Calibri", 25), bg="#23a2e8", fg="white", command=check)
        next_button.place(relx=0.75, rely=0.85, relwidth=0.2, relheight=0.1)

        random.shuffle(equations)
        next_equation()



    # main menu main header
    Label(window, bg="#1a2434", fg="white", font=("Comic Sans", 50, "bold"), text="AQA GSCE Physics\nEquations Practice").place(relx=0.25, rely=0,
                                                                                                                 relwidth=0.5, relheight=0.3)
    # main menu background
    Label(window, bg="#273142").place(relx=0.25, rely=0.26, relwidth=0.5, relheight=0.59)

    Button(window, bg="#323B4C", font=("Comic Sans", 16), text="Test All Equations", fg="white", bd=0, command=place_test_all_equations).place(relx=0.35, rely=0.45,
                                                                                                               relwidth=0.3, relheight=0.1)
    # include higher only equations checkbox
    higher_checkbox = Button(window, font=("Comic Sans", 20), text="✓", command=higher_checkbox_toggle)
    higher_checkbox.place(relx=0.55, rely=0.75, relwidth=0.03, relheight=0.06)
    Label(window, bg="#273142", font=("Comic Sans", 16), fg="white", text="Include Higher\nOnly Equations").place(relx=0.42, rely=0.75,
                                                                                                      relwidth=0.13, relheight=0.06)


window = Tk()
window.title("Physics Equations Practice")
window.config(background="#1A2434")
window.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}")

score = 0 # total = 92

units = ["°C", "Amps", "Coulombs", "Hertz", "J/kg°C", "J/kg", "Joules", "Kg m/s", "Kg/m³", "Kg", "m/s²", "m/s", "m²", "m³", "Metres", "N/kg",
         "N/m", "Newton Metres", "Newtons", "Ohms", "Pascals", "Seconds", "Tesla", "Volts", "Watts"]

kinetic_energy = formula("Kinetic Energy", 3, 0, 1,
                         "This is used to work out the energy a moving object has",
                         " Ek = 0.5mv²\nkinetic energy(J) = 0.5 x mass(Kg) x velocity(m/s)²", ["1/2", "0.5"], ["mass"], ["velocity", "speed"], None, None, False,
                         "Joules", None, "Kg", "m/s", None, None)

elastic_potential_energy = formula("Elastic Potential\nEnergy", 3, 0, 1,
                                   "This is the work done when a spring is extended or compressed",
                                   "Ee = 0.5ke²\nelastic energy(J) = 0.5 x spring constant(N/m) x extension(M)²", ["1/2", "0.5"], ["spring constant"], ["extension", "spring extension"], None, None, False,
                                   "Joules", None, "N/m", "Metres", None, None)

gravitational_potential_energy = formula("Gravitational\nPotential Energy", 3, 0, 0,
                                         "This is the potential energy of any object above the ground",
                                         "Ep = mgh\nGPE(J) = mass(Kg) x gravity strength(N/kg) x height(M)", ["mass"], ["gravity", "gravity strength", "field strength", "gravitational strength", "gravitational field strength"], ["height"], None, None, True,
                                         "Joules", "Kg", "N/kg", "Metres", None, None)

change_in_thermal_energy = formula("Change in\nThermal Energy", 3, 0, 0,
                                   "This is the change in the amount of thermal energy stored as temperature changes",
                                   "∆E = mc∆0\nenergy change(J) = mass(Kg) x specific heat capacity(J/kg°C) x temperature change(°C)", ["mass"], ["specific heat capacity"], ["temperature change", "change in temperature"], None, None, True,
                                   "Joules", "Kg", "J/kg°C", "°C", None, None)

power = formula("Power", 1, 1, 0,
                 "This is the rate of energy transfer when energy is transferred to an object",
                 "P = E/t\npower(W) = energy transferred(J) / time(s)", ["energy transferred"], None, None, None, ["time"], False,
                "Watts", "Joules", None, None, None, "Seconds")

power_in_circuits = formula("Power in\nCircuits", 2, 0, 0,
                 "This is the rate of energy change between stores in an electrical circuit",
                 "P = VI\npower in circuits(W) = voltage(V) x current(A)", ["potential difference", "voltage"], ["current"], None, None, None, True,
                            "Watts", "Volts", "Amps", None, None, None)

charge_flow = formula("Charge Flow", 2, 0, 0,
                      "This is the rate of flow of charge in electric circuits",
                      "Q = It\ncharge flow(C) = current(A) x time(s)", ["current"], ["time"], None, None, None, True,
                      "Coulombs", "Amps", "Seconds", None, None, None)

potential_difference = formula("Potential Difference", 2, 0, 0,
                               "This is a measure of the amount of energy transferred between two points in a circuit",
                               "V = IR\nPD(V) = current(A) x resistance(O)", ["current"], ["resistance"], None, None, None, True,
                               "Volts", "Amps", "Ohms", None, None, None)

energy_transferred = formula("Energy Transferred", 2, 0, 0,
                             "This is the amount of energy used by an appliance",
                             "E = Pt\nEnergy transferred(J) = power(W) x time(s)", ["power"], ["time"], None, None, None, True,
                             "Joules", "Watts", "Seconds", None, None, None)

energy_transferred_in_circuits = formula("Energy Transferred\nin Circuits", 2, 0, 0,
                                         "This is the energy change caused by a charge moving between different voltages",
                                         "E = QV\nEnergy transferred = charge flow(C) x voltage(V)", ["charge flow"], ["potential difference", "voltage"], None, None, None, True,
                                         "Joules", "Coulombs", "Volts", None, None, None)

density = formula("Density", 1, 1, 0,
                  "This is the ratio of mass to volume of an object",
                  "p = m/V\ndensity(Kg/m³) = mass(Kg) / volume(m³)", ["mass"], None, None, None, ["volume"], False,
                  "Kg/m³", "Kg", None, None, None, "m³")

energy_needed_for_change_of_state = formula("Energy needed for\nchange of state", 2, 0, 0,
                                            "This is the amount of energy needed for a substance change of state to occur",
                                            "E = mL\nenergy(J) = mass(Kg) x specific latent heat(J/kg)", ["mass"], ["latent heat", "specific latent heat"], None, None, None, True,
                                            "Joules", "Kg", "J/kg", None, None, None)

gas_constant = formula("Gas Constant", 2, 0, 0,
                       "Volume is inversely proportional to pressure when at a constant temperature",
                       "Constant = pV\nconstant = pressure(P) x volume(m³)", ["pressure"], ["volume"], None, None, None, True,
                       None, "Pascals", "m³", None, None, None)

weight = formula("Weight", 2, 0, 0,
                 "This is the force created by an object when affected by gravity",
                 "W = mg\nWeight(N) = mass(Kg) x gravity strength(N/kg)", ["mass"], ["gravity", "gravity strength", "gravitational field strength", "field strength", "gravitational strength"], None, None, None, True,
                 "Newtons", "Kg", "N/kg", None, None, None)

work_done = formula("Work Done", 2, 0, 0,
                    "This is the measure of energy transfer when a force moves an object",
                    "W = Fs\nwork done(J) = force(N) x distance(M)", ["force"], ["distance"], None, None, None, True,
                    "Joules", "Newtons", "Metres", None, None, None)

force_on_a_spring = formula("Force on\na Spring", 2, 0, 0,
                            "This is the amount of force being put on a spring",
                            "F = ke\nforce on spring(N) = spring constant(N/m) x extension(M)", ["spring constant"], ["extension"], None, None, None, True,
                            "Newtons", "N/m", "Metres", None, None, None)

moment_of_a_force = formula("Moment of\na force", 2, 0, 0,
                            "This is the strength of the turning effect caused by a force, they act around a pivot",
                            "M = Fd\nMoment(NM) = force(N) x distance(M)", ["force"], ["distance"], None, None, None, True,
                            "Newton Metres", "Newtons", "Metres", None, None, None)

pressure = formula("Pressure", 1, 1, 0,
                   "This is the force per unit area at the surface of a fluid (liquid or gas)",
                   "p = F/A\npressure(P) = force(N) / surface area(m²)", ["force", "force normal to a surface"], None, None, None, ["area of that surface", "surface area"], False,
                   "Pascals", "Newtons", None, None, None, "m²")

pressure_from_column_liquid = formula("Pressure due to a column of liquid", 3, 0, 0,
                                      "This is the pressure at a depth in a liquid, e.g. high pressure at the ocean floor",
                                      "p = hpg\npressure(P) = height(M) x density(Kg/m³) x gravity strength(N/kg)", ["height", "column height", "height of column", "height of the column"], ["density", "liquid density", "density of liquid", "density of the liquid"], ["gravity", "gravity strength", "gravitational field strength", "field strength", "gravitational strength"], None, None, True,
                                      "Pascals", "Metres", "Kg/m³", "N/kg", None, None)

distance_travelled = formula("Distance travelled", 2, 0, 0,
                             "This is the amount of distance covered by an object after a certain time",
                             "s = vt\ndistance(M) = speed(m/s) x time(s)", ["speed", "velocity"], ["time"], None, None, None, True,
                             "Metres", "m/s", "Seconds", None, None, None)

acceleration = formula("Acceleration", 1, 1, 0,
                       "This is the rate of change in speed",
                       "a = ∆v/t\nacceleration(m/s²) = speed change(m/s) / time(s)", ["change in velocity", "velocity change", "change in speed", "speed change"], None, None, None,  ["time taken", "time"], False,
                       "m/s²", "m/s", None, None, None, "Seconds")

final_velocity = formula("Final velocity²", 4, 0, 0,
                         "This is used to find the final velocity of an object after it has accelerated",
                         "v² = 2as + u²\n final velocity(m/s) = 2 x acceleration(m/s²) x distance(M) x initial velocity(m/s)", ["2"], ["acceleration"], ["distance", "displacement"], ["initial velocity"], None, False,
                         "m/s", None, "m/s²", "Metres", "m/s", None)

resultant_force = formula("Resultant force", 2, 0, 0,
                          "This is the amount of force needed to accelerate something",
                          "F = ma\nforce(N) = mass(Kg) x acceleration(m/s²)", ["mass"], ["acceleration"], None, None, None, True,
                          "Newtons", "Kg", "m/s²", None, None, None)

momentum = formula("Momentum", 2, 0, 0,
                   "This is the quantity of motion of a moving object, a direction must be included",
                   "p = mv\nmomentum(Kg m/s) = mass(Kg) x speed(m/s)", ["mass"], ["velocity", "speed"], None, None, None, True,
                   "Kg m/s", "Kg", "m/s", None, None, None)

force = formula("Force", 1, 1, 0,
                "This is the rate of change of momentum",
                "a = m∆v/∆t\nforce(N) = change in momentum(Kg m/s) / time(s)", ["momentum change", "mass x change in velocity", "change in momentum"], None, None, None, ["time taken", "time"], False,
                "Newtons", "Kg m/s", None, None, None, "Seconds")

wave_period = formula("Wave period", 1, 1, 0,
                      "This is the time period of a wave",
                      "T = 1/f\nwave period(s) = 1 / wave frequency(Hz)", ["1", "one"], None, None, None, ["frequency", "wave frequency"], False,
                      "Seconds", None, None, None, None, "Hertz")

wave_speed = formula("Wave speed", 2, 0, 0,
                     "This is the speed of a wave",
                     "v = fλ\nwave speed(m/s) = wave frequency(Hz) x wavelength(M)", ["frequency", "wave frequency"], ["wavelength", "wave length"], None, None, None, True,
                     "m/s", "Hertz", "Metres", None, None, None)

force_on_a_conductor = formula("Force on a conductor", 3, 0, 0,
                               "This is the force on a wire carrying a current at a right angle to a magnetic field",
                               "F = BIl\nforce(N) = magnetic flux density(T) x current(A) x length(M)", ["magnetic flux density"], ["current"], ["length"], None, None, True,
                               "Newtons", "Tesla", "Amps", "Metres", None, None)

equations = [kinetic_energy, elastic_potential_energy, gravitational_potential_energy, change_in_thermal_energy, power, power_in_circuits,
             charge_flow, potential_difference, energy_transferred, energy_transferred_in_circuits, density, energy_needed_for_change_of_state, gas_constant,
             weight, work_done, force_on_a_spring, moment_of_a_force, pressure,pressure_from_column_liquid, distance_travelled, acceleration, final_velocity,
             resultant_force, momentum, force, wave_period, wave_speed, force_on_a_conductor]

place_main_menu()

window.mainloop()
