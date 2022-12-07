import os
import random
from tkinter import *
import tkinter.messagebox as tmsg


# y to change position of frame vertically
# x to change position of frame horizontally
# height to change height
# relwidth is used LabelFrame,Frame to fit according to window size


class Bill_App:
    def __init__(self, r):
        self.root = r
        self.root.geometry("10000x8000")
        self.root.title("I - MART")
        bg_colour = "lightgreen"
        title = Label(self.root, text="Billing Software", bd=12, font="ComicSansMS 20 bold", fg="red", bg=bg_colour
                      , relief=GROOVE, pady=1)
        title.place(x=0, y=5, height=70, relwidth=1)

        # scroll_y = Scrollbar(root, orient=VERTICAL)
        # self.Bill_App = Text(root, yscrollcommand=scroll_y.set)
        # scroll_y.pack(side=RIGHT, fill=Y)
        # scroll_y.configure(command=self.Bill_App.yview)
        # self.Bill_App.pack(fill=BOTH)

        # VARIABLES

        # COSMETICS
        self.soap = IntVar()
        self.beard_cream = IntVar()
        self.face_wash = IntVar()
        self.hair_spray = IntVar()
        self.body_lotion = IntVar()
        self.deo = IntVar()

        # GROCERY
        self.rice = IntVar()
        self.wheat = IntVar()
        self.cooking_oil = IntVar()
        self.tea = IntVar()
        self.sugar = IntVar()
        self.coffee = IntVar()

        # COLD DRINK
        self.red_bull = IntVar()
        self.coca_cola = IntVar()
        self.maaza = IntVar()
        self.fanta = IntVar()
        self.sprite = IntVar()
        self.rio = IntVar()

        # TOTAL PRICE AND TAX
        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price = StringVar()

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()

        # CUSTOMER
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()
        self.print_bill = StringVar()

        # CUSTOMER DETAILS FRAME
        F1 = LabelFrame(self.root, text="Customer Details", font="ComicSansMS 15 bold", fg="purple", bg=bg_colour,
                        bd=12,
                        relief=GROOVE)
        F1.place(x=0, y=67, relwidth=1)

        c_name_lbl = Label(F1, text="Customer Name", fg="dark green", font="ComicSansMS 16 bold")
        c_name_lbl.grid(row=0, column=0, padx=20, pady=20)
        c_name_text = Entry(F1, width=15, font="Calibri 15", textvariable=self.c_name, bd=7, relief=SUNKEN)
        c_name_text.grid(row=0, column=1, padx=10)

        c_phn_lbl = Label(F1, text="Phone No.", fg="dark green", font="ComicSansMS 16 bold")
        c_phn_lbl.grid(row=0, column=2, padx=20, pady=20)
        c_phn_text = Entry(F1, width=15, font="Calibri 15", textvariable=self.c_phone, bd=7, relief=SUNKEN)
        c_phn_text.grid(row=0, column=3, padx=10)

        c_bill_lbl = Label(F1, text="Bill No.", fg="dark green", font="ComicSansMS 16 bold")
        c_bill_lbl.grid(row=0, column=4, padx=20, pady=20)
        c_bill_text = Entry(F1, width=15, font="Calibri 15", textvariable=self.search_bill, bd=7, relief=SUNKEN)
        c_bill_text.grid(row=0, column=5, padx=10)

        c_bill_btn = Button(F1, text="Search", width=10, bd=7, font="Arial 12 bold", relief=GROOVE,
                            command=self.find_bill
                            , fg="red", bg="white")
        c_bill_btn.grid(row=0, column=6, padx=10, pady=10)

        # COSMETICS FRAME
        F2 = LabelFrame(self.root, text=" COSMETICS", font="ComicSansMS 15 bold", fg="purple", bg=bg_colour, bd=12,
                        relief=GROOVE)
        F2.place(x=6, y=175, width=324, height=365)

        bath_lbl = Label(F2, text="Soap", font="LucidaFax 16 bold", bg=bg_colour, fg="red")
        bath_lbl.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        bath_txt = Entry(F2, width=10, font="LucidFax 16 bold", textvariable=self.soap, bd=4, relief=SUNKEN)
        bath_txt.grid(row=0, column=1, padx=10, pady=10)

        beard_c_lbl = Label(F2, text="Beard Cream", font="LucidaFax 16 bold", bg=bg_colour, fg="red")
        beard_c_lbl.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        beard_c_txt = Entry(F2, width=10, font="LucidFax 16 bold", textvariable=self.beard_cream, bd=4, relief=SUNKEN)
        beard_c_txt.grid(row=1, column=1, padx=10, pady=10)

        face_w_lbl = Label(F2, text="Face Wash", font="LucidaFax 16 bold", bg=bg_colour, fg="red")
        face_w_lbl.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        face_w_txt = Entry(F2, width=10, font="LucidFax 16 bold", textvariable=self.face_wash, bd=4, relief=SUNKEN)
        face_w_txt.grid(row=2, column=1, padx=10, pady=10)

        hair_s_lbl = Label(F2, text="Hair Spray", font="LucidaFax 16 bold", bg=bg_colour, fg="red")
        hair_s_lbl.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        hair_s_txt = Entry(F2, width=10, font="LucidFax 16 bold", textvariable=self.hair_spray, bd=4, relief=SUNKEN)
        hair_s_txt.grid(row=3, column=1, padx=10, pady=10)

        body_lbl = Label(F2, text="Body Lotion", font="LucidaFax 16 bold", bg=bg_colour, fg="red")
        body_lbl.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        body_txt = Entry(F2, width=10, font="LucidFax 16 bold", textvariable=self.body_lotion
                         , bd=4, relief=SUNKEN)
        body_txt.grid(row=4, column=1, padx=10, pady=10)

        deo_lbl = Label(F2, text="Deo", font="LucidaFax 16 bold", bg=bg_colour, fg="red")
        deo_lbl.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        deo_txt = Entry(F2, width=10, font="LucidFax 16 bold", textvariable=self.deo, bd=4, relief=SUNKEN)
        deo_txt.grid(row=5, column=1, padx=10, pady=10)

        # GROCERY ITEMS FRAME
        F3 = LabelFrame(self.root, text="GROCERY(1KG)", font="ComicSansMS 15 bold", fg="purple", bg=bg_colour, bd=12,
                        relief=GROOVE)
        F3.place(x=340, y=175, width=324, height=365)
        g1_lbl = Label(F3, text="Rice", font="LucidaFax 16 bold", bg=bg_colour, fg="red")
        g1_lbl.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        g1_txt = Entry(F3, width=10, font="LucidFax 16 bold", textvariable=self.rice, bd=4, relief=SUNKEN)
        g1_txt.grid(row=0, column=1, padx=10, pady=10)

        g2_lbl = Label(F3, text="Wheat", font="LucidaFax 16 bold", bg=bg_colour, fg="red")
        g2_lbl.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        g2_txt = Entry(F3, width=10, font="LucidFax 16 bold", textvariable=self.wheat, bd=4, relief=SUNKEN)
        g2_txt.grid(row=1, column=1, padx=10, pady=10)

        g3_lbl = Label(F3, text="Cooking Oil", font="LucidaFax 16 bold", bg=bg_colour, fg="red")
        g3_lbl.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        g3_txt = Entry(F3, width=10, font="LucidFax 16 bold", textvariable=self.cooking_oil, bd=4, relief=SUNKEN)
        g3_txt.grid(row=2, column=1, padx=10, pady=10)

        g4_lbl = Label(F3, text="Tea", font="LucidaFax 16 bold", bg=bg_colour, fg="red")
        g4_lbl.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        g4_txt = Entry(F3, width=10, font="LucidFax 16 bold", textvariable=self.tea, bd=4, relief=SUNKEN)
        g4_txt.grid(row=3, column=1, padx=10, pady=10)

        g5_lbl = Label(F3, text="Sugar", font="LucidaFax 16 bold", bg=bg_colour, fg="red")
        g5_lbl.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        g5_txt = Entry(F3, width=10, font="LucidFax 16 bold", textvariable=self.sugar, bd=4, relief=SUNKEN)
        g5_txt.grid(row=4, column=1, padx=10, pady=10)

        g6_lbl = Label(F3, text="Coffee", font="LucidaFax 16 bold", bg=bg_colour, fg="red")
        g6_lbl.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        g6_txt = Entry(F3, width=10, font="LucidFax 16 bold", textvariable=self.coffee, bd=4, relief=SUNKEN)
        g6_txt.grid(row=5, column=1, padx=10, pady=10)

        # COLD DRINK FRAME
        F4 = LabelFrame(self.root, text="COLD DRINK(250mL)", font="ComicSansMS 15 bold", fg="purple", bg=bg_colour,
                        bd=12,
                        relief=GROOVE)
        F4.place(x=670, y=175, width=324, height=365)

        c1_lbl = Label(F4, text="Red Bull", font="LucidaFax 16 bold", bg=bg_colour, fg="red")
        c1_lbl.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        c1_txt = Entry(F4, width=10, font="LucidFax 16 bold", textvariable=self.red_bull, bd=4, relief=SUNKEN)
        c1_txt.grid(row=0, column=1, padx=10, pady=10)

        c2_lbl = Label(F4, text="Coca Cola", font="LucidaFax 16 bold", bg=bg_colour, fg="red")
        c2_lbl.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        c2_txt = Entry(F4, width=10, font="LucidFax 16 bold", textvariable=self.coca_cola, bd=4, relief=SUNKEN)
        c2_txt.grid(row=1, column=1, padx=10, pady=10)

        c3_lbl = Label(F4, text="Maaza", font="LucidaFax 16 bold", bg=bg_colour, fg="red")
        c3_lbl.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        c3_txt = Entry(F4, width=10, font="LucidFax 16 bold", textvariable=self.maaza, bd=4, relief=SUNKEN)
        c3_txt.grid(row=2, column=1, padx=10, pady=10)

        c4_lbl = Label(F4, text="Fanta", font="LucidaFax 16 bold", bg=bg_colour, fg="red")
        c4_lbl.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        c4_txt = Entry(F4, width=10, font="LucidFax 16 bold", textvariable=self.fanta, bd=4, relief=SUNKEN)
        c4_txt.grid(row=3, column=1, padx=10, pady=10)

        c5_lbl = Label(F4, text="Sprite", font="LucidaFax 16 bold", bg=bg_colour, fg="red")
        c5_lbl.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        c5_txt = Entry(F4, width=10, font="LucidFax 16 bold", textvariable=self.sprite, bd=4, relief=SUNKEN)
        c5_txt.grid(row=4, column=1, padx=10, pady=10)

        c6_lbl = Label(F4, text="Rio", font="LucidaFax 16 bold", bg=bg_colour, fg="red")
        c6_lbl.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        c6_txt = Entry(F4, width=10, font="LucidFax 16 bold", textvariable=self.rio, bd=4, relief=SUNKEN)
        c6_txt.grid(row=5, column=1, padx=10, pady=10)

        # BILL PRODUCTIONS
        F5 = Frame(self.root, bd=12, relief=GROOVE)
        F5.place(x=1010, y=175, width=350, height=365)

        # SCROLLBAR IN BILL AREA
        bill_title = Label(F5, text="Total I Bill", font="Arial 15 bold", bd=7, relief=GROOVE)
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.configure(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH)

        # BILL FRAME
        F6 = LabelFrame(self.root, text="BILL MENU", font="ComicSansMS 15 bold", fg="purple", bg=bg_colour, bd=12,
                        relief=GROOVE)
        F6.place(x=0, y=540, height=180, relwidth=1)

        # PRICES
        m1_lbl = Label(F6, text="Cosmetic Price", font="ComicSansMS 12 bold", fg="darkblue")
        m1_lbl.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        m1_text = Entry(F6, width=18, font="ComicSansMS 12 bold", textvariable=self.cosmetic_price, bd=7, relief=SUNKEN)
        m1_text.grid(row=0, column=1, padx=10, pady=1)

        m2_lbl = Label(F6, text="Grocery Price", font="ComicSansMS 12 bold", fg="darkblue")
        m2_lbl.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        m2_text = Entry(F6, width=18, font="ComicSansMS 12 bold", textvariable=self.grocery_price, bd=7, relief=SUNKEN)
        m2_text.grid(row=1, column=1, padx=10, pady=1)

        m3_lbl = Label(F6, text="COLD DRINK Price", font="ComicSansMS 12 bold", fg="darkblue")
        m3_lbl.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        m3_text = Entry(F6, width=18, font="ComicSansMS 12 bold", textvariable=self.cold_drink_price, bd=7,
                        relief=SUNKEN)
        m3_text.grid(row=2, column=1, padx=10, pady=1)

        # TAX

        c1_lbl = Label(F6, text="Cosmetic Tax", font="ComicSansMS 12 bold", fg="darkblue")
        c1_lbl.grid(row=0, column=2, padx=10, pady=10, sticky="w")
        c1_text = Entry(F6, width=18, font="ComicSansMS 12 bold", textvariable=self.cosmetic_tax, bd=7, relief=SUNKEN)
        c1_text.grid(row=0, column=3, padx=10, pady=1)

        c2_lbl = Label(F6, text="Grocery Tax", font="ComicSansMS 12 bold", fg="darkblue")
        c2_lbl.grid(row=1, column=2, padx=10, pady=10, sticky="w")
        c2_text = Entry(F6, width=18, font="ComicSansMS 12 bold", textvariable=self.grocery_tax, bd=7, relief=SUNKEN)
        c2_text.grid(row=1, column=3, padx=10, pady=1)

        c3_lbl = Label(F6, text="COLD DRINK Tax", font="ComicSansMS 12 bold", fg="darkblue")
        c3_lbl.grid(row=2, column=2, padx=10, pady=10, sticky="w")
        c3_text = Entry(F6, width=18, font="ComicSansMS 12 bold", textvariable=self.cold_drink_tax, bd=7, relief=SUNKEN)
        c3_text.grid(row=2, column=3, padx=10, pady=1)

        # BUTTONS(TOTAL, C BILL, CLEAR, EXIT)

        btn_F = Frame(F6, bd=7, relief=GROOVE)
        btn_F.place(x=750, width=580, height=105)

        # TOTAL BUTTON
        total_btn = Button(btn_F, text="Total", font="ComicSansMS 14", bg="yellow", fg="darkblue", bd=5, pady=15,
                           width=10
                           , command=self.total)
        total_btn.grid(row=0, column=0, padx=8, pady=5)

        # CREATE BILL BUTTON
        cbill_btn = Button(btn_F, text="Create I Bill", font="ComicSansMS 14", bg="yellow", fg="darkblue", bd=5,
                           pady=15,
                           width=10, command=self.area_bill)
        cbill_btn.grid(row=0, column=1, padx=8, pady=5)

        # CLEAR BUTTON
        clear_btn = Button(btn_F, text="Clear", font="ComicSansMS 14", bg="yellow", fg="darkblue", bd=5, pady=15,
                           width=10
                           , command=self.clear_data)
        clear_btn.grid(row=0, column=2, padx=8, pady=5)

        # EXIT BUTTON
        Exit_btn = Button(btn_F, text="Exit", font="ComicSansMS 14", bg="yellow", fg="darkblue", bd=5, pady=15, width=10
                          , command=self.Exit_app)
        Exit_btn.grid(row=0, column=3, padx=8, pady=5)
        self.wlcm_bill()


        print_btn = Button(btn_F, text="Print", )




        # COSMETIC PRICES

    # def soap(self):
    # soap=40
    # beard_cream = 100
    # face_wash = 50
    # hair_spray = 120
    # body_lotion = 250
    # deo = 350

    # GROCERY PRICES

    # rice = IntVar()
    # rice.set(30)
    # wheat = 40
    # cooking_oil = 150
    # tea = 480
    # sugar = 420
    # coffee = 700

    # COLD DRINK PRICES

    # red_bull = 140
    # coca_cola = 42
    # maaza = 40
    # fanta = 45
    # sprite = 32
    # rio = 220

    # CREATING TOTAL BILL BUTTON
    def total(self):
        # COSMETICS PRICE
        self.c_s_p = (self.soap.get() * 40)
        self.c_fc_p = (self.beard_cream.get() * 100)
        self.c_fw_p = (self.face_wash.get() * 50)
        self.c_hs_p = (self.hair_spray.get() * 120)
        self.c_l_p = (self.body_lotion.get() * 250)
        self.c_d_p = (self.deo.get() * 330)
        self.total_cosmetic_price = float(
            self.c_s_p + self.c_l_p + self.c_fc_p + self.c_fw_p + self.c_hs_p + self.c_d_p)
        self.cosmetic_price.set("Rs. " + str((self.total_cosmetic_price)))
        self.c_tax = (round((self.total_cosmetic_price * 0.12), 2))
        self.cosmetic_tax.set("Rs. " + str(self.c_tax))

        # GROCERY PRICE
        self.g_r_p = (self.rice.get() * 30)
        self.g_w_p = (self.wheat.get() * 40)
        self.g_co_p = (self.cooking_oil.get() * 150)
        self.g_t_p = (self.tea.get() * 480)
        self.g_s_p = (self.sugar.get() * 420)
        self.g_c_p = (self.coffee.get() * 700)
        self.total_grocery_price = float(self.g_r_p + self.g_w_p + self.g_co_p + self.g_t_p + self.g_s_p + self.g_c_p)
        self.grocery_price.set("Rs. " + str((self.total_grocery_price)))
        self.g_tax = (round((self.total_grocery_price * 0.15), 2))
        self.grocery_tax.set("Rs. " + str(self.g_tax))

        # COLD DRINK PRICE
        self.cd_rb_p = (self.red_bull.get() * 140)
        self.cd_cc_p = (self.coca_cola.get() * 42)
        self.cd_m_p = (self.maaza.get() * 40)
        self.cd_f_p = (self.fanta.get() * 45)
        self.cd_s_p = (self.sprite.get() * 32)
        self.cd_ri_p = (self.rio.get() * 220)
        self.total_cold_drink_price = float(self.cd_rb_p + self.cd_cc_p + self.cd_m_p + self.cd_f_p + self.cd_s_p +
                                            self.cd_ri_p)
        self.cold_drink_price.set("Rs. " + str(self.total_cold_drink_price))
        self.cd_tax = (round((self.total_cold_drink_price * 0.12), 2))
        self.cold_drink_tax.set("Rs. " + str(self.cd_tax))

        self.total_bill = (float(round((self.total_cosmetic_price + self.c_tax + self.total_grocery_price + self.g_tax
                                        + self.total_cold_drink_price + self.cd_tax), 2)))

    # BILL PRODUCTION AREA

    # DECORATING BILL AREA
    def wlcm_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "           Welcome to I-Mart")
        self.txtarea.insert(END, "\n      Lots to love. Less to spend")
        self.txtarea.insert(END, f"\n I Bill Number: {self.bill_no.get()}")
        self.txtarea.insert(END, f"\n Customer Name: {self.c_name.get()}")
        self.txtarea.insert(END, f"\n Phone Number: {self.c_phone.get()}")
        self.txtarea.insert(END, f"\n======================================")
        self.txtarea.insert(END, f"\n Products\t\tQTY\tRate\tPrice")
        self.txtarea.insert(END, f"\n======================================")

    def area_bill(self):
        self.wlcm_bill()
        if self.c_name.get() == "":
            tmsg.showerror("Error", "Enter Customer Name")
        elif self.c_phone.get() == "":
            tmsg.showerror("Error", "Enter Customer Phone Number")
        elif self.cosmetic_price.get() == "Rs. 0.0" and self.grocery_price.get() == "Rs. 0.0" and self.cold_drink_price.get() == "Rs. 0.0":
            tmsg.showerror("Empty", "No Products are selected from I - MART")
        else:
            # COSMETICS
            if self.soap.get() != 0:
                self.txtarea.insert(END, f"\n Soap\t\t{self.soap.get()}\t40\t{self.c_s_p}")
            if self.beard_cream.get() != 0:
                self.txtarea.insert(END, f"\n Beard Cream\t\t{self.beard_cream.get()}\t100\t{self.c_fc_p}")
            if self.face_wash.get() != 0:
                self.txtarea.insert(END, f"\n Face Wash\t\t{self.face_wash.get()}\t50\t{self.c_fw_p}")
            if self.hair_spray.get() != 0:
                self.txtarea.insert(END, f"\n Hair Spray\t\t{self.hair_spray.get()}\t120\t{self.c_hs_p}")
            if self.body_lotion.get() != 0:
                self.txtarea.insert(END, f"\n Body Lotion\t\t{self.body_lotion.get()}\t250\t{self.c_l_p}")
            if self.deo.get() != 0:
                self.txtarea.insert(END, f"\n Deo\t\t{self.deo.get()}\t330\t{self.c_d_p}")

            # GROCERY
            if self.rice.get() != 0:
                self.txtarea.insert(END, f"\n Rice\t\t{self.rice.get()}\t30\t{self.g_r_p}")
            if self.wheat.get() != 0:
                self.txtarea.insert(END, f"\n Wheat\t\t{self.wheat.get()}\t40\t{self.g_w_p}")
            if self.cooking_oil.get() != 0:
                self.txtarea.insert(END, f"\n Cooking Oil\t\t{self.cooking_oil.get()}\t150\t{self.g_co_p}")
            if self.tea.get() != 0:
                self.txtarea.insert(END, f"\n Tea\t\t{self.tea.get()}\t480\t{self.g_t_p}")
            if self.sugar.get() != 0:
                self.txtarea.insert(END, f"\n Sugar\t\t{self.sugar.get()}\t420\t{self.g_s_p}")
            if self.coffee.get() != 0:
                self.txtarea.insert(END, f"\n Coffee\t\t{self.coffee.get()}\t700\t{self.g_c_p}")

            # COLD DRINK
            if self.red_bull.get() != 0:
                self.txtarea.insert(END, f"\n Red Bull\t\t{self.red_bull.get()}\t140\t{self.cd_rb_p}")
            if self.coca_cola.get() != 0:
                self.txtarea.insert(END, f"\n Coca Cola\t\t{self.coca_cola.get()}\t42\t{self.cd_cc_p}")
            if self.maaza.get() != 0:
                self.txtarea.insert(END, f"\n Maaza\t\t{self.maaza.get()}\t40\t{self.cd_m_p}")
            if self.fanta.get() != 0:
                self.txtarea.insert(END, f"\n Fanta\t\t{self.fanta.get()}\t45\t{self.cd_f_p}")
            if self.sprite.get() != 0:
                self.txtarea.insert(END, f"\n Sprite\t\t{self.sprite.get()}\t32\t{self.cd_s_p}")
            if self.rio.get() != 0:
                self.txtarea.insert(END, f"\n Rio\t\t{self.rio.get()}\t220\t{self.cd_ri_p}")

            self.txtarea.insert(END, f"\n======================================")
            if self.cosmetic_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\n Cosmetic Tax\t\t\t{self.cosmetic_tax.get()}")
            if self.grocery_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
            if self.cold_drink_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\n Cold Drink Tax\t\t\t{self.cold_drink_tax.get()}")
            self.txtarea.insert(END, f"\n Total I Bill: \t\t\tRs. {self.total_bill}")
            self.txtarea.insert(END, f"\n======================================")
            self.txtarea.insert(END, f"\n======================================")
            self.txtarea.insert(END, f"\nAbove prices are inclusive of I-Taxes.")
            self.txtarea.insert(END, f"\nThis is RUSHI'S mart generated I-Bill")

            self.save_bill()

    def save_bill(self):
        op = tmsg.askyesno("Save I Bill", "Do you want to save it")
        self.bill_data = self.txtarea.get("1.0", END)
        f1 = open("virtualenv" + str(self.bill_no.get()) + ".txt", "w")
        f1.write(self.bill_data)
        f1.close()
        # tmsg.showinfo("Saved", f"Bill No.: {self.bill_no.get()} has been saved")
        if op > 0:
            tmsg.showinfo("Saved", f"Your I Bill No.: {self.bill_no.get()} has been saved")
            return
        else:
            tmsg.showinfo("Don't Save Bill", "Thank You For Shopping With Us.")

    # SEARCH BILL
    def find_bill(self):
        present = "no"
        for i in os.listdir(""):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"{i}", "r")
                self.txtarea.delete('1.0', END)
                for d in f1:
                    self.txtarea.insert(END, d)
                f1.close()
                present = "yes"
        if present == "no":
            tmsg.showerror("Not Found", "Oops!! Invalid I Bill Number.")

    def clear_data(self):
        op = tmsg.askyesno("Clear", "Do you want to clear everything")
        if op > 0:
            # COSMETICS
            self.soap.set(0)
            self.beard_cream.set(0)
            self.face_wash.set(0)
            self.hair_spray.set(0)
            self.body_lotion.set(0)
            self.deo.set(0)

            # GROCERY
            self.rice.set(0)
            self.wheat.set(0)
            self.cooking_oil.set(0)
            self.tea.set(0)
            self.sugar.set(0)
            self.coffee.set(0)

            # COLD DRINK
            self.red_bull.set(0)
            self.coca_cola.set(0)
            self.maaza.set(0)
            self.fanta.set(0)
            self.sprite.set(0)
            self.rio.set(0)

            # TOTAL PRICE AND TAX
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")

            # CUSTOMER
            self.c_name.set("")
            self.c_phone.set("")
            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.wlcm_bill()

    def Exit_app(self):
        op = tmsg.askyesno("Exit", "Do you really want to Exit RUSHI's - MART")
        if op > 0:
            self.root.destroy()


root = Tk()

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(fill=BOTH)
scrollbar.config(command=txt.yview)

obj = Bill_App(root)
# root.wm_iconbitmap("apple.ico")
root.mainloop()