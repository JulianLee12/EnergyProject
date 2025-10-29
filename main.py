import html
import streamlit.components.v1 as components
imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")
import altair as alt


import streamlit as st
import pandas as pd

st.set_page_config(page_title="PowerInfo", layout="wide")

# =========================================
# Global CSS (eco + modern; animation + remove all top whitespace)
# =========================================
CUSTOM_CSS = """
<style>
:root{
  --bg: #F0FCF5;
  --card: #ffffff;
  --accent: #2e7d32;
  --accent-soft: #A5D6A7;
  --text: #1f2937;
  --muted: #6b7280;
  --shadow: 0 8px 24px rgba(0,0,0,.08);
  --shadow-hover: 0 16px 40px rgba(0,0,0,.14);
  --radius: 18px;
}

/* REMOVE TOP STREAMLIT HEADER & PADDING */
/* MINIMAL HEADER (keeps sidebar + deploy buttons working) */
/* MINIMAL HEADER (keeps sidebar + deploy buttons working) */
/* Keep header tiny but visible so sidebar/deploy stay on-screen */
header[data-testid="stHeader"] {
  height: 36px !important;
  min-height: 36px !important;
  padding: 0 !important;
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
}


/* nice breathing room from top */
.block-container {
  padding-top: 30px !important;
  margin-top: 0 !important;
}


html, body, [data-testid="stAppViewContainer"] { background: var(--bg); }
h1, h2, h3, h4, h5, h6 { color: var(--text); }

/* Hero */
.hero {
  background: linear-gradient(120deg, rgba(165,214,167,.35), rgba(255,255,255,0));
  border: 1px solid rgba(46,125,50,.12);
  border-radius: var(--radius);
  padding: 28px 28px;
  margin-bottom: 12px;
}
.hero h1 { margin: 0 0 6px 0; font-size: 34px; line-height: 1.15; }
.hero p  { margin: 6px 0 0 0; font-size: 16px; color: var(--muted); }

/* Card row */
.fan-wrap {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  gap: 28px;
  padding: 10px 0 4px 0;
  margin: 8px auto 0 auto;
  max-width: 1100px;
  position: relative;
}

.fan-card {
  width: 340px;
  height: 230px;
  background: var(--card);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  border: 1px solid rgba(46,125,50,.12);
  padding: 18px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  cursor: pointer;
  transition: transform .22s ease, box-shadow .22s ease, filter .22s ease;
  will-change: transform;
  opacity: 0;
  transform: translateY(14px);
  animation: slidefade .60s ease forwards;
}

/* Slide fade */
@keyframes slidefade {
  from { opacity: 0; transform: translateY(14px); }
  to   { opacity: 1; transform: translateY(0); }
}

/* Fan angles */
.fan-card.water  { animation-delay: .05s;  transform: rotate(-3.2deg) translateY(8px); }
.fan-card.hvac   { animation-delay: .15s;  transform: rotate(0deg) translateY(-6px) scale(1.05); }
.fan-card.energy { animation-delay: .25s;  transform: rotate(3.2deg) translateY(8px); }

/* Hover nicer */
.fan-card:hover {
  transform: translateY(-6px) scale(1.02) rotate(0deg) !important;
  box-shadow: var(--shadow-hover);
  filter: saturate(1.03);
}

.fan-card h3 { margin: 0; font-size: 22px; color: var(--text); }
.fan-card p  { margin: 0; font-size: 14px; color: var(--muted); }

.fan-card .illus {
  margin-top: auto; height: 60px; border-radius: 12px;
  background: linear-gradient(90deg,#e8f5e9,#f1f8f4);
  border: 1px dashed #cde9d4;
  display:flex;align-items:center;justify-content:center;
  font-size:12px;color:#4b5563;
}

/* Responsive fix */
@media (max-width: 1000px) {
  .fan-wrap { flex-direction: column; align-items: stretch; gap: 14px; }
  .fan-card { width:100%; height:auto; transform:none !important; }
}

/* Footer */
.footer {
  position: fixed;
  bottom: 0; left: 0; right: 0;
  background: rgba(255,255,255,.94);
  border-top: 1px solid rgba(0,0,0,.06);
  backdrop-filter: blur(6px);
  padding: 8px 16px;
  display:flex;justify-content:center;align-items:center;
  font-size:13px;color:var(--muted);
  z-index:9999;
}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# =========================================
# TEXT CONTENT (same as before, omitted for brevity here)
# =========================================
# =========================================
# Content (TEXT ONLY, headings styled)
# =========================================

WATER_SAVING_MD = """
### What is the main use of water in households?
Toilets, Showering, tap water, laundry machines and leaks seem to be the main cause of water usage in households with bathtubs and dishwashers also playing a role. Each litre of water costs around $0.0014 to $0.0021 depending on the season.

### Why is water important?
Water is a key resource in everyone's lives, as they need it to drink, wash, and much more. Water is one of the most important thing in people's households, but there is limited amount of it. In Vancouver, water is super pure and drinkable, so we must not take it for granted and make sure to conserve as much water as we can, or else we might not have enough to sustain future generations.
"""


TOILETS_MD = """
### How Can Toilets Help Save Water?

#### Background
Background: Toilets use 6 litres of water every flush, and an average person urinates 6 to 8 times a day. Toilets are the biggest contributor to the amount of water used in households.

### Dual-flush toilets
Dual flush toilets for flushing less water when you pee, and using more water to flush when you poo. This cuts your water usage by up to 67% of water use from originally with a single-flush toilet, because you pee more than you poo everyday (unless you are in some condition) so halving the water flushed when you urinate will more than likely help save you lots of water used and save lots of money in your utility bill depending on how long you have it for. these dual flush toilets cost around 300 dollars for an average dual flush toilet, though buying just the buttons only cost on average around $10 for the button, but be sure to check the product for special conversion kits for standard toilets, because some of them don't have it and it could be hard to install. Overall, buying a whole toilet would gradually be able to save money over time, but with a button, it would be sure to save money and do a small without spending that much money.

### Flushing Once After a Few Urinations
This tip is controversial, but only flushing the toilet once after a few people urinate could save many litres of water, so you don't have to flush all the time. "If it's yellow, let it mellow. If it's brown, flush it down." If you think this is gross, think that pee doesn't really have an odor to it and that it saves, for example, a household with a family of 4, who all pee 6 times a day, you could flush every 4 times someone pees in a washroom which turns 4 people peeing into 1 person. This would save 108 litres of water a day with a normal toilet (6 litres per flush) and 54 litres with a dual-flush toilet (3 litres per flush). With a dual-flush toilet, you could be saving almost 1 cent everyday, and a normal toilet would save around 2 cents everyday. For a year, that's $3.56 for a dual flush, or $7.12 for a regular toilet. This might not seem like a lot, but it is doing a lot for the environment and saving lots of water. It's a completely free way of saving a few quick bucks.

### Old toilets vs new
In BC, a law came into effect in september 30, 2005 to change the capacity of water allowed to flush in one use from bein required to use over 13.2 litres of water to 6 litres per flush or lower. That means if you have an old toilet before laws were enacted, getting a new toilet may be easier to get clogged while pooping, but you will at least cut the amount of water used by toilets in half. It's like comparing 3 2-litre coke bottles to 6 2-litre coke bottles. In canada, even toilet water is drinking grade, so would you want to waste 6.2 more litres of bottled drinking quality water?

### Sand In Bottles
If these tips are used in your daily life and appliances, it could cut more that half your utility bill in the future.
"""


SHOWER_MD = """
### How can Showers help save water?

#### Background
Background: Showering is tied for 2nd most water used in , people usually take 1-2 showers a day, and a 5 minute shower uses up around 75 litres of water.

- Use low flow head instead to reduce the amount of water pumping out at a time
- Turn off water when u use soap and dont need water (Images referenced on the original page.)

### Showering vs Bathing
A 5 minute shower uses up around 75 litres of water, while bathing uses around 90 litres of water for a full bath. Therefore, if you take longer showers that 5 minutes on average, bathing could save a bit of water each time you do it - gradually building up while also not feeling claustrophobic in the shower stall. (Images referenced on the original page.)

### Using low-flow shower heads
Low-flow shower heads are anything under 6.8 lpm (litres per minute), and have a huge range of numbers that would be considered low-flow. These showerheads could be using 1 litre less water every minute, but could still feel the same and take the same amount of time when showering.
"""
HVAC_MD = """
### What is HVAC
HVAC stands for Heating, Ventilation, and AC/Air Conditioning.

### Why is HVAC important?
HVAC is important because it can save you lots of money and energy if you get the right appliances and things similar to that.
"""


HEATING_MD = """
### Heat Pumps
Most of the time if you have a traditional of an really old electric or oil furnace, that could be really bad for the environment and consume a lot of energy meaning it will be really expensive. Heat pumps on the other hand is still expensive in the initial cost but could save you up to 50%. Not only that, they are generally good for the environment. (Images referenced on the original page.)

### Gas vs Electric Stoves
- Gas stove requires less energy than an electric stove so if you switch from an electric to an gas stove then you could save up to 2000$ annually.
- If you want to do better for environment use an electric stove because although gas stoves use less energy, they releases double the amount of greenhouse emissions. (Images referenced on the original page.)

### Alternative Heating
- Another good option for house heating is boilers. They heat water to create steam, and send them to be circulated through pipes all around the house to heat the home.
- Finally there is a hybrid heating. This is a combination of two heating systems in order to maximize efficiency.
"""


VENTILATION_MD = """
### Types of Ventilation Systems and How They Work
- All of the ventilation systems need to have air pressure in order to move the air around the pipes carrying the air from place to place
- This air pressure is created by a form of fans forcing the air through a series of ducts and vents.
- A type of ventilation is called natural ventilation. This relies on natural things such as wind and temperature difference between indoor and outdoor air to create pressure difference.
- Another form of ventilation is called supply ventilation. This uses a fan in order to push fresh air from outside into the building creating a positive pressure that forces the stale air out through leaks and exhaust fans
"""


ENERGY_SAVING_MD = """
Without switching to renewable energy, our world would be polluted with excessive carbon emission and trigger immense climate change as well and affecting our health. Switching to renewable energy is important because we need to protect the environment. By reducing our greenhouse gas emissions and pollution we can lower our costs and reducing utility bills.
"""



RENEWABLES_MD = """
### Why we should switch to renewable energy sources.
Switching to renewable energy sources could provide cheaper energy bills as well as a constant supply and clean energy. Switching to renewable energy sources allows us to combat climate change as well as improving the air quality and the cleanliness of the water. Using renewable energy is important becuase non-renewable energies like fossil fuels (coal, oil, and natural gas) and uranium for nuclear energy will eventually run out. (Images referenced on the original page.)

### Wind Energy
Wind turbines generate energy by harnessing the wind kinetic energy spinning the large blades on the machine which in turn spins the shaft connected to the power generator. Wind turbines are often found in large groups in windy areas or hill tops. (Images referenced on the original page.)

### Solar Panels
Solar panles are the main source of solar energy. Solar panels convert sunlight into usable energy using a process called photovoltaic effect. Adding solar may be costly but will pay off in the long run especially in places with lots of sunlight. Even without direct sunlight solar panels can still generate energy. (Images referenced on the original page.)

### Geothermal
Unlike other renewable energy sources, geothermal energy harness the heat of the Earth. Thi s mode of energy can provide almost unlimited energy generation unlike solar and wind energy. (Images referenced on the original page.)

### Biomass
Biomass is a renewable energy source that is produced from organic matter like plants or Biomass is a renewable energy source derived from organic materials like plants or animals. It is converted into heat, electricity, or fuels such as bioethanol and biodiesel through processes like combustion, gasification, and fermentation. (Images referenced on the original page.)

### Hydro-electric
Hydroelectric energy is generated from the force of moving water, such as rivers, lakes and the ocean. The grid stability of hydroelectric dams is very consistent, as the push and ebb of water can provide unlimited energy. (Images referenced on the original page.)

### Piezoelectricity
This form of energy is created when substances are forced under pressure of mechanical stress. This happens because the stress shifts the positive and negative charges in the structure.
"""


ENERGY_CONSERVATION_MD = """
### Shop Responsibly
When shopping, look for more energy-efficient models rather than outdated ones. Also, be mindful of online shipping returns as all of thse actions contribute to emiting CO2.

### Turn Off Lighting When Not Needed

### Adjust Thermostats
"""


# =========================================
# HOMEPAGE
# =========================================
def page_home():
    st.markdown(
        '<div class="hero"><h1>PowerInfo</h1><p>Small changes, big impact — Learn how to conserve energy and water in your home.</p></div>',
        unsafe_allow_html=True,
    )
    st.caption("Explore a category:")

    st.markdown(
        """
        <style>
        /* ensure no underline for clickable cards */
        .fan-card {
          text-decoration: none !important;
          color: inherit !important;
        }
        </style>

        <div class="fan-wrap">
          <a href="/page_water" target="_self" class="fan-card water">
            <h3>Water Saving</h3>
            <p>Toilets, showers, taps, laundry and leak prevention.</p>
            <div class="illus">Illustration placeholder</div>
          </a>

          <a href="/page_hvac" target="_self" class="fan-card hvac">
            <h3>HVAC</h3>
            <p>Heating, ventilation and air conditioning basics & tips.</p>
            <div class="illus">Illustration placeholder</div>
          </a>

          <a href="/page_energy" target="_self" class="fan-card energy">
            <h3>Energy Saving</h3>
            <p>Renewables, efficiency and everyday conservation.</p>
            <div class="illus">Illustration placeholder</div>
          </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

def page_rebate():
    st.markdown("# Rebates in British Columbia")

    st.markdown("""
    You may be eligible for rebates that help offset the cost of energy-efficient upgrades to your home.
    These rebate programs are offered by BC Hydro and related provincial initiatives to encourage
    clean energy adoption and home efficiency improvements.
    """)

    # Rebate data
    data = {
        "Rebate": [
            "Attic Insulation",
            "Battery Storage",
            "Heat Pump Water Heater",
            "Level 2 EV Charger",
            "New Toilets",
            "Refrigerators",
            "Solar Panels",
            "Whole Home Heating"
        ],
        "Amount ($)": [
            900,
            5000,
            1000,
            350,
            100,
            150,
            5000,
            4000
        ]
    }

    df = pd.DataFrame(data).sort_values("Rebate")

    st.markdown("### Available Rebates (BC Hydro)")

    # Determine chart upper limit (add headroom)
    max_val = df["Amount ($)"].max()

    # Main chart with labels
    bars = alt.Chart(df).mark_bar().encode(
        x=alt.X("Rebate:N", sort=None, title="Program"),
        y=alt.Y(
            "Amount ($):Q",
            title="Rebate Amount ($)",
            scale=alt.Scale(domain=[0, max_val * 1.15])  # breathing space
        ),
        tooltip=["Rebate", "Amount ($)"]
    )

    labels = alt.Chart(df).mark_text(
        align='center',
        baseline='bottom',
        dy=-4,
        fontSize=12
    ).encode(
        x="Rebate:N",
        y="Amount ($):Q",
        text=alt.Text("Amount ($):Q", format="$.0f")
    )

    chart = (bars + labels).properties(height=500)

    st.altair_chart(chart, use_container_width=True)

    # CTA button
    st.markdown(
        """
        <br>
        <a href="https://www.bchydro.com/powersmart/residential/rebates-programs.html" target="_blank"
           style="display:inline-block;padding:10px 16px;background-color:#2e7d32;color:white;border-radius:8px;
                  text-decoration:none;font-weight:500;">
            Learn More at BC Hydro
        </a>
        """,
        unsafe_allow_html=True
    )




# =========================================
# PAGE RENDERERS
# =========================================
def page_water():
    st.markdown("# Water Saving\n"+WATER_SAVING_MD)
    # ---------- constants ----------
    MIN_COST_PER_L = 0.0014
    MAX_COST_PER_L = 0.0021

    def _money_range_from_litres(L: float):
        low_cost = L * MIN_COST_PER_L
        high_cost = L * MAX_COST_PER_L
        return low_cost, high_cost

    # ---------- static content ----------


    st.markdown("### 💧 Interactive Bathroom Configurator")
    st.caption("Pick your setup and see how it compares to an older, less efficient bathroom.")

    # ---------- UI ----------
    c1, c2, c3 = st.columns(3)
    people = c1.number_input("Household size", 1, 12, 3)
    toilet_type = c2.selectbox(
        "Toilet type",
        ["Old (≈13 L/flush)", "Modern (≈6 L/flush)", "Dual-flush (≈3 L avg)"]
    )
    shower_head = c3.selectbox(
        "Shower head",
        ["Standard (≈9.5 L/min)", "Low-flow (≈6.8 L/min)"]
    )

    c4, c5 = st.columns(2)
    flushes = c4.slider("Flushes per person / day", 2, 12, 6)
    minutes = c5.slider("Shower minutes per person", 0, 30, 8)

    # ---------- logic ----------
    toilet_map = {"Old (≈13 L/flush)": 13.0, "Modern (≈6 L/flush)": 6.0, "Dual-flush (≈3 L avg)": 3.0}
    shower_map = {"Standard (≈9.5 L/min)": 9.5, "Low-flow (≈6.8 L/min)": 6.8}

    # your setup
    flush_L = toilet_map[toilet_type]
    lpm = shower_map[shower_head]

    your_flush_total = people * flushes * flush_L
    your_shower_total = people * minutes * lpm
    your_total = your_flush_total + your_shower_total

    # baseline (always "old" gear)
    baseline_flush_total = people * flushes * 13.0
    baseline_shower_total = people * minutes * 9.5
    baseline_total = baseline_flush_total + baseline_shower_total

    savings = baseline_total - your_total
    low_cost_year, high_cost_year = _money_range_from_litres(savings * 365)

    # ---------- output ----------
    c6, c7, c8 = st.columns(3)
    c6.metric("Your usage (L/day)", f"{your_total:,.0f}")
    c7.metric("Old baseline (L/day)", f"{baseline_total:,.0f}")
    c8.metric("Daily savings", f"{savings:,.0f} L")

    st.success(
        f"**Estimated yearly savings:** ${low_cost_year:,.0f} – ${high_cost_year:,.0f} per year "
        f"just from bathroom upgrades & habits."
    )

    # optional small breakdown chart
    st.bar_chart(
        pd.DataFrame(
            {
                "Baseline": [baseline_flush_total, baseline_shower_total],
                "Your Setup": [your_flush_total, your_shower_total],
            },
            index=["Toilet", "Shower"],
        )
    )


    # ---------- Water Usage Pie Chart ----------
    st.markdown("### Household Water Usage Breakdown")

    import plotly.graph_objects as go

    labels = ["Toilet", "Shower", "Faucet", "Washing Machine", "Leak", "Other"]
    values = [24, 20, 19, 17, 12, 8]

    fig = go.Figure(
        data=[go.Pie(
            labels=labels,
            values=values,
            hoverinfo="label+percent",
            textinfo="label+percent",
            hole=.35  # donut style (clean + modern)
        )]
    )

    fig.update_layout(
        height=380,
        showlegend=False,
        margin=dict(t=10, b=10, l=10, r=10)
    )

    st.plotly_chart(fig, use_container_width=True)


def page_toilets():
    st.markdown("# Toilets")
    st.subheader("How Can Toilets Help Save Water?")

    st.markdown("""
    Background: Toilets use 6 litres of water every flush, and an average person urinates 6 to 8 times a day. 
    Toilets are the biggest contributor to the amount of water used in households.
    """)

    tabs = st.tabs([
        "Dual-Flush Toilets",
        "Flushing Once After a Few Urinations",
        "Old Toilets vs New",
        "Sand in Bottles in Toilet Tanks"
    ])

    with tabs[0]:
        st.markdown("""
        ### Dual-Flush Toilets

        Dual flush toilets use less water when you pee, and more when you poo. This can reduce your toilet-related water usage
        by up to **67%** compared to a single-flush toilet, because urination happens much more frequently.

        A full dual-flush toilet typically costs around **300 dollars**, but buying just the **dual-flush button conversion kit**
        is usually about **10 dollars**, if your toilet is compatible.

        It might be hard to install depending on the toilet model, so be sure to check for compatibility first. Buying a whole
        dual-flush toilet might not save you enough money to justify the cost right away, but using just the conversion button
        is a cheap and effective way to save water and help the environment with a much smaller investment.
        """)

    with tabs[1]:
        st.markdown("""
        ### Flushing Once After a Few Urinations

        This tip is sometimes considered controversial, but flushing only **after several urinations** can save a large 
        amount of water each day. The saying goes:

        > “If it's yellow, let it mellow. If it's brown, flush it down.”

        For a household of 4 people urinating 6 times a day each, flushing every 4 urinations turns **24 flushes into 6** 
        flushes per day. This saves **108 litres per day** using a standard toilet (6L/flush) and **54 litres per day** 
        using a dual-flush model (3L/flush).

        With a dual flush toilet, you could be saving almost **8 cents every day**, and a normal toilet would save around 
        **15 cents per day**. Over a year, this equals **$3.56** for dual flush and **$7.12** for regular toilets. This 
        might not seem like a lot, but it is a **completely free** way to save water and help the environment.
        """)

    with tabs[2]:
        st.markdown("""
        ### Old Toilets vs New

        In BC, a law came into effect on **September 30, 2005**, requiring all new toilets to use **6 litres per flush or 
        less**, replacing older toilets that used over **13.2 litres** per flush.

        Upgrading from an old toilet cuts water usage **in half** or more, even if the flushing strength feels different. 
        It’s like comparing **3 x 2-litre Coke bottles** versus **6 x 2-litre Coke bottles** of clean, drinkable water.

        Yes — in Canada, even toilet water is **drinking-grade**. So if your toilet is older, switching to a newer model 
        is one of the biggest improvements you can make to reduce household water waste and lower your monthly bill.
        """)

    with tabs[3]:
        st.markdown("""
        ### Sand in Bottles in Toilet Tanks

        Placing sealed bottles filled with sand in your toilet tank **displaces water**, reducing how much is used per flush.
        A **2-litre bottle displaces 2 litres** of water, so each litre you add displaces one litre per flush.

        However, a few things to avoid:

        - Using a bottle that is **too big** — the toilet may not flush properly.
        - In **modern toilets**, this can reduce flushing performance and do more harm than good because newer systems are 
          already designed for low-volume efficiency.

        This method is best for **older toilets**, not newer water-efficient models.
        """)

        # -------- QUIZ SECTION --------
    st.markdown("---")
    st.markdown("## Toilets Quiz")

    st.markdown("Test your understanding of how toilets can help save water:")

    q1 = st.radio(
        "1) What is the main advantage of a dual-flush toilet?",
        ["It costs less upfront", "It uses less water for urination", "It flushes stronger than old toilets"],
        index=None
    )

    q2 = st.radio(
        "2) Why does flushing less often save so much water?",
        ["Urination happens more often than bowel movements", "New toilets leak more",
         "Toilets store extra water when unused"],
        index=None
    )

    q3 = st.radio(
        "3) True or False: A law in BC requires all toilets after 2005 to use 6 litres per flush or less.",
        ["True", "False"],
        index=None
    )

    q4 = st.radio(
        "4) True or False: Adding bottles of sand to the toilet tank works best in modern toilets.",
        ["True", "False"],
        index=None
    )

    correct_answers = [
        "It uses less water for urination",
        "Urination happens more often than bowel movements",
        "True",
        "False"
    ]

    user_answers = [q1, q2, q3, q4]

    if st.button("Submit Quiz"):
        score = sum([user_answers[i] == correct_answers[i] for i in range(4)])
        st.success(f"You scored {score} / 4")

        explanations = [
            "Dual-flush toilets reduce water usage for urination, which happens more frequently.",
            "Most flushing is from urination, so reducing those flushes saves more water.",
            "BC introduced a law in 2005 limiting toilets to 6L or less per flush.",
            "The sand bottle trick is mainly for **older** toilets, not modern efficient ones."
        ]

        for i in range(4):
            if user_answers[i] == correct_answers[i]:
                st.write(f"✅ Q{i + 1}: {explanations[i]}")
            else:
                st.write(f"❌ Q{i + 1}: {explanations[i]}")

def page_washing_machine():
    st.markdown("# Washing Machine")
    st.subheader("How Can We Save Water with a Laundry Machine?")

    st.markdown("""
    Background: Washing machines use the third most amount of water in an average household, and 1 person washes their clothes 
    from 1-3 times a week. A load for a normal washing machine uses around **85 litres** of water.
    """)

    tabs = st.tabs([
        "Different Piles & Modes",
        "Loads"
    ])

    with tabs[0]:
        st.markdown("""
        ### Different Piles & Modes

        Making a separate pile for dirty/sweaty items and casual/not beat up clothes for different washing modes can help save 
        more water than you think. When you get dirty and musty clothes, you would most likely use a full wash to fully wash 
        away the bacteria and the smell. Instead of making a load with dirty and not very dirty clothes together, you should 
        split them apart.

        With not so beat up clothes, you can use different modes such as eco mode or speed wash. While a standard machine uses 
        around **87.1 litres** of water per load, eco mode can use from only **35 to 50 litres**. You could save more than 
        **30 litres of water per wash**, which is equivalent to a jerry can full of water or more.
        """)

    with tabs[1]:
        st.markdown("""
        ### Loads

        You should only use full loads when washing clothes because when you put in half a load, you're using the same amount 
        of water and energy just for half the amount of clothes you could've washed for the same result overall. It is pretty 
        straightforward — don't use your washing machine until there is a **full load** of clothes to wash and save lots of 
        water and energy being put into it.
        """)

    # ---------------- Interactive Calculator ----------------
    st.markdown("---")
    st.markdown("## Laundry Water Savings Calculator")

    st.markdown("Adjust the values below to estimate how much water you can save by switching to eco mode.")

    # Inputs
    loads_per_week = st.slider("Loads per week", 1, 10, 3)
    eco_litres = st.slider("Eco mode water usage per load (L)", 35, 50, 40)

    # Constants
    STANDARD_LITRES = 87  # standard washing machine usage

    # Calculations
    weekly_standard = loads_per_week * STANDARD_LITRES
    weekly_eco = loads_per_week * eco_litres
    weekly_savings = weekly_standard - weekly_eco
    yearly_savings = weekly_savings * 52

    col1, col2, col3 = st.columns(3)
    col1.metric("Standard use (L/week)", f"{weekly_standard:,.0f}")
    col2.metric("Eco use (L/week)", f"{weekly_eco:,.0f}")
    col3.metric("Weekly savings (L)", f"{weekly_savings:,.0f}")

    st.success(
        f"⭐ By using eco mode, you could save approximately **{yearly_savings:,.0f} litres per year**!"
    )




def page_shower():
    st.markdown("# Shower")
    st.subheader("How can Showers help save water?")

    st.markdown("""
    Showering is tied for the **second highest** water usage in most homes. People usually take
    **1–2 showers a day**, and a **5-minute shower uses around 75 litres of water**.
    Using more efficient shower heads or reducing how long water is running can significantly reduce waste.
    """)

    st.markdown("## Showering vs Bathing")
    st.markdown("""
         Baths use a fixed amount of water each time, while showers use more water the longer they run.
         Depending on your shower length and shower head type, a shower can use **less** or **more** water
         than a bath. Use the calculator below to compare and see which is more efficient for your household.
         """)

    col1, col2 = st.columns(2)

    with col1:
        minutes = st.slider("Average shower length (minutes)", 1, 30, 5)
        head_type = st.selectbox(
            "Shower head type",
            ["Standard (≈9.5 L/min)", "Low-flow (≈6.8 L/min)"]
        )
        people = st.number_input("Number of people showering", 1, 10, 1)

    with col2:
        bath_size = st.selectbox(
            "Bath size",
            ["Small (70 L)", "Standard (90 L)", "Large (110 L)"]
        )

    # mapping to actual numbers
    head_map = {"Standard (≈9.5 L/min)": 9.5, "Low-flow (≈6.8 L/min)": 6.8}
    bath_map = {"Small (70 L)": 70, "Standard (90 L)": 90, "Large (110 L)": 110}

    lpm = head_map[head_type]
    bath_litres = bath_map[bath_size]

    shower_total = minutes * lpm * people
    difference = bath_litres - shower_total

    st.markdown("### Comparison")

    col3, col4 = st.columns(2)
    col3.metric("Your shower(s)", f"{shower_total:.1f} L")
    col4.metric("Bath", f"{bath_litres:.1f} L")

    if shower_total < bath_litres:
        st.success("✅ Your showers use **less** water than taking a bath.")
    elif shower_total > bath_litres:
        st.warning("⚠️ Your showers use **more** water than taking a bath — a bath may be more efficient at this length.")
    else:
        st.info("ℹ️ Your shower water usage is **equal** to a bath.")

    st.subheader("Using low-flow shower heads")
    st.markdown("""Low-flow shower heads are anything under 6.8 lpm,(litres per minute) and have a huge range of numbers that would be considered low-flow. These showerheads could use around 3 litres less water every minute, but could still feel the same and take the same amount of time when showering. The shower heads usually cost around $25, or up so buying it won't help much with saving money unless used over many years, but it can save 10+ litres of water everyday to help save water for future generations.
""")

    st.subheader("Turning Water Off While Putting Soap On")
    st.markdown("""Each time you shower, you put on soap (unless it's a quick rinse) and the average time to put it on is 20 seconds. Just 20 seconds could use up more than 3 litres of water in the shower. Do you rinse your body the same time you put on soap? No, all the soap would wash away before anything even happens, so it's a totally free way to save 3 litres of water everyday when you shower. 
""")



def page_hvac():
    st.markdown("# HVAC\n"+HVAC_MD)
    st.image("https://img.freepik.com/premium-vector/hvac-logo-design-template-cooling-heating-logo-illustration_373791-3698.jpg")
def page_heating():
    st.markdown("# Heating")
    st.subheader("What is home heating?")
    st.markdown("""
    Heating is used to warm the home during cold seasons, and it is one of the biggest contributors
    to household energy consumption. The type of heating system you use and how efficient it is 
    can have a major impact on cost, comfort, and environmental footprint.
    """)


    st.image("https://lh3.googleusercontent.com/sitesv/AAzXCkfMYGOFjoV-DdB8g51_UEvFQsQDUl45Y7mT5FMCgSH6PKAJBYjpKMgc-JwKdj5aqxopQG3Wu0dlY7-0cMX9lS299HpMlbtLyLe56I0lj4Fh5qSCXke4oJp6QVVErEkdvfbrOFBCOk-YLb_FCcFpi8rjV6tzTCaUnAKpglbpnYqyngC2G_Qppn-fgrfclhAWUA3Vzu0pmfLBDRws7Qr7v8OoqeQbQm_AhXvouwM=w1280")
    # Tabs for different heating system explanations
    tabs = st.tabs([
        "Heat Pumps",
        "Gas vs Electric Stoves",
        "Alternative Heating",
        "Furnace"
    ])

    # ---------------- TAB 1: Heat Pumps ----------------
    with tabs[0]:
        st.markdown("""
        ### Heat Pumps
        Most of the time if  you have a traditional of an really old electric or oil furnace, that could be really bad for the environment and consume a lot of energy meaning it will be really expensive. Heat pumps on the other hand is still expensive in the initial cost but could save you up to 50%. Not only that, they are generally good for the environment.
        """)
        st.image("https://lh6.googleusercontent.com/c9gjxk4XoO8IObswmHf-uc4yKd8mxVLPbtyIUuzZ_rhHgepqsOoGNWWSRDoPlq-9mZ14pPsyIb5I3Lv2oy66UJk")

    # ---------------- TAB 2: Gas vs Electric Stoves ----------------
    with tabs[1]:
        st.markdown("""
        ### Gas vs Electric Stoves
        - Gas stoves require less energy than electric stoves and heat up faster, so switching from electric to gas can save **10–20% annually**.
        - If you want to do better for the environment, choose an **electric stove**, because although gas stoves are more energy-efficient, they release **double the greenhouse emissions**.

        """)
        st.image("https://lh6.googleusercontent.com/AW_8EiRBJ4hvU64T2_XTdRjtLjb_aLTzk5XJgYWz__yRX6conWdxGiPOaEbBFlLpXXSmw4Q5apjypbGFI9g0kg")
        st.image("https://static.scientificamerican.com/sciam/cache/file/4FEB5C93-F6DA-475B-9FB7C0A2A73227E9_source.jpg?crop=1%3A1%2Csmart&w=1000")
    # ---------------- TAB 3: Alternative Heating ----------------
    with tabs[2]:
        st.markdown("""
        ### Alternative Heating
        Some homes use boilers. This system heats water to create steam. Then they send them to be circulated through pipes all around the house to heat the home. Another option is hybrid heating. This is a combination of two heating systems in order to maximize efficiency.
        """)
        st.image("https://lh5.googleusercontent.com/FpPxqjwYfywjgwP-SKrqBEpjHNWUt9UmK02BAXG6w24qwM7NUD1-ieDKi6_EerhH6BUoRTYgPqTrA-dwUC8LwrY")
        st.markdown("---")
        st.markdown("## Heat Pump vs Furnace (Interactive Comparison)")
        st.markdown("""
        Use the calculator below to estimate how much you could save by switching from an old furnace
        to a modern heat pump. This comparison assumes a **65% efficient furnace vs a 250% efficient
        heat pump**, which is typical for many older homes.
        """)

        cost = st.slider("Your current annual heating cost ($)", 500, 5000, 1500, 100)

        FURNACE_EFF = 0.65
        HEATPUMP_EFF = 2.5

        new_cost = cost * (FURNACE_EFF / HEATPUMP_EFF)
        savings = cost - new_cost
        percent_savings = (savings / cost) * 100

        col1, col2 = st.columns(2)
        col1.metric("Current heating cost", f"${cost:,.0f}/yr")
        col2.metric("With a heat pump", f"${new_cost:,.0f}/yr")

        st.success(f"✅ Estimated savings: **${savings:,.0f} per year** (~{percent_savings:.0f}% less)")
        co2_reduction = percent_savings
        st.info(f"🌱 Estimated CO₂ reduction: **~{co2_reduction:.0f}%** per year")

    # ---------------- TAB 4: Furnace ----------------
    with tabs[3]:
        st.markdown("""
        ### Furnace
        Tending to your furnace is vital, especially if it is an older model. The first step is annual servicing by a professional, which involves cleaning or replacing old parts and making sure the furnace isn't working harder than it needs to. When a furnace is clogged the system will need to work harder to push making the energy consumption higher. Finally, older furnaces loses its energy efficient over time so by tending to the worn out parts it will restore its efficiency.        """)

        st.markdown("---")
        st.markdown("### Furnace Quiz")

        q1 = st.radio("1) Why should an older furnace be serviced annually?",
                      ["For decoration",
                       "Because it keeps it efficient & prevents wasted energy",
                       "To make the furnace quieter"],
                      index=None)

        q2 = st.radio("2) What happens when a furnace filter is clogged?",
                      ["It releases more heat",
                       "It has to work harder and uses more energy",
                       "It turns off permanently"],
                      index=None)

        q3 = st.radio("3) Why does maintenance matter more for older furnaces?",
                      ["They are already efficient",
                       "Replacing worn parts reduces wasted energy",
                       "They don't use electricity"],
                      index=None)

        if st.button("Submit Furnace Answers"):
            answers = [
                "Because it keeps it efficient & prevents wasted energy",
                "It has to work harder and uses more energy",
                "Replacing worn parts reduces wasted energy"
            ]
            user = [q1, q2, q3]
            score = sum([user[i] == answers[i] for i in range(3)])
            st.success(f"Your score: {score}/3")
            explanations = [
                "Servicing prevents the furnace from wasting fuel or power.",
                "A clogged filter forces the furnace to push harder, raising energy use.",
                "Older furnaces lose efficiency over time, so maintenance restores performance."
            ]
            for i in range(3):
                if user[i] == answers[i]:
                    st.write(f"✅ Q{i+1}: {explanations[i]}")
                else:
                    st.write(f"❌ Q{i+1}: {explanations[i]}")


def page_vent():
    st.markdown("# Ventilation")
    st.subheader("What is ventilation?")
    st.markdown("""
    Ventilation is how fresh air enters a home and stale or humid air leaves it. Good ventilation improves
    air quality, reduces moisture, prevents mold growth, and makes indoor spaces more comfortable and healthy.
    Some systems rely on natural airflow, while others use fans to push or pull air through the building.
    """)

    # Tabs for organized information
    tabs = st.tabs([
        "Natural Ventilation",
        "Supply Ventilation",
        "Exhaust Ventilation"

    ])

    with tabs[0]:
        st.markdown("""
        ### Natural Ventilation
        One type of ventilation is called natural ventilation. This relies on natural things such as wind and temperature difference between indoor and outdoor air to create pressure difference.
        """)

    with tabs[1]:
        st.markdown("""
        ### Supply Ventilation
        This uses a fan in order to push fresh air from outside into the building creating a positive pressure that forces the stale air out through leaks and exhaust fans.
        """)

    with tabs[2]:
        st.markdown("""
        ### Exhaust Ventilation
        One form of ventilation is exhaust ventilation. These systems are mainly are inside the bathroom, and things similar to that and they work by depressurizing the inside of the house when the air goes out of the building. These systems use exhaust fans to push the stale air out.
        """)

    # --------------------- Mini-Game ---------------------
    st.markdown("## Mini-Game: Classify the Ventilation Methods")
    st.markdown("Select which category each ventilation method belongs to:")

    methods = [
        ("Opening windows", "Natural"),
        ("Fan pushing fresh air inside", "Supply"),
        ("Exhaust fan pulling stale air out", "Exhaust"),
        ("Bathroom fan", "Exhaust"),
    ]

    if "vent_answers" not in st.session_state:
        st.session_state.vent_answers = {}

    options = ["Natural", "Supply", "Exhaust"]

    for name, correct in methods:
        st.session_state.vent_answers[name] = st.radio(
            f"{name}",
            options,
            horizontal=True,
            key=f"radio_{name}"
        )

    if st.button("Check Answers"):
        correct_count = 0
        for name, correct in methods:
            user_choice = st.session_state.vent_answers.get(name)
            if user_choice == correct:
                correct_count += 1

        st.markdown(f"### You got **{correct_count} / {len(methods)}** correct")

        # Show detailed feedback
        for name, correct in methods:
            user_choice = st.session_state.vent_answers.get(name)
            if user_choice == correct:
                st.success(f"✅ {name} — Correct")
            else:
                # Explanation based on category
                if correct == "Natural":
                    reason = "Natural ventilation relies on wind or temperature differences and does not use mechanical fans."
                elif correct == "Supply":
                    reason = "Supply systems push **fresh air into** the home using fans, creating positive pressure."
                else:  # Exhaust
                    reason = "Exhaust systems pull **stale air out** of the home using fans, creating negative pressure."

                st.error(
                    f"❌ {name} — You chose **{user_choice}**\n\n"
                    f"**Correct:** {correct}\n\n"
                    f"**Why:** {reason}"
                )


def page_ac():
    st.markdown("# Air Conditioning")
    st.subheader("How does air conditioning impact energy use?")

    st.markdown("""
    In energy usage, an air conditioner uses **500 to 3500 watts per hour** depending on the size:
    - A **large central AC unit** uses around **3500 watts per hour**
    - A **small room AC** uses around **500–1000 watts per hour**

    Older air conditioners are also worse for the environment because they release **hydrofluorocarbons** into the atmosphere.
    This is a pretty harmful greenhouse gas.

    A more sustainable option is a **heat pump**, which can both heat *and* cool while using far less energy and is environmentally friendly.

    According to the Residential Energy Consumption Survey (RECS), about **10% of the average household's total
    electricity consumption** comes from air conditioning. Therefore by turning off your AC or heater and just wear a warm sweater in the winter or wear shorts in the summer could save you lots of money and energy.
    """)

    st.markdown("## AC Energy Usage Estimator")

    ac_type = st.selectbox(
        "Select AC type",
        ["Small (500 W)", "Medium (1000 W)", "Central (3500 W)"]
    )

    power_map = {"Small (500 W)": 500, "Medium (1000 W)": 1000, "Central (3500 W)": 3500}
    power = power_map[ac_type]

    hours = st.slider("Hours of use per day", 1, 24, 6)
    cost_kwh = st.number_input("Electricity cost ($ per kWh)", 0.05, 0.50, 0.12, step=0.01)

    # convert W → kW
    kwh_per_day = (power * hours) / 1000
    daily_cost = kwh_per_day * cost_kwh
    monthly_cost = daily_cost * 30

    st.markdown("### Estimated Energy Use")
    col1, col2 = st.columns(2)
    col1.metric("kWh per day", f"{kwh_per_day:.1f}")
    col2.metric("Cost per day", f"${daily_cost:.2f}")

    col3, col4 = st.columns(2)
    col3.metric("Estimated monthly cost", f"${monthly_cost:.2f}")
    col4.metric("Power rating", f"{power} W")

    # Optional "what if I reduce hours?"
    reduced_hours = max(hours - 2, 0)
    reduced_cost = (power * reduced_hours / 1000) * cost_kwh * 30
    savings = monthly_cost - reduced_cost

    st.info(
        f"🌿 If you used the AC **2 hours less per day**, you could save about **${savings:.2f} per month**."
    )


def show_carousel(img_list):
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])  # Balanced centered layout
    with col2:
        st.markdown(
            "<div style='max-width:600px;margin:0 auto;'>",
            unsafe_allow_html=True,
        )
        imageCarouselComponent(imageUrls=img_list, height=300)  # << updated height here
        st.markdown("</div>", unsafe_allow_html=True)

def page_energy():
    st.markdown("# Energy Saving\n"+ENERGY_SAVING_MD)

    show_carousel([
                "https://offgridsolarsystem.ca/images/canada-electricity-rates-july-2025.png",
                "https://renewablesassociation.ca/wp-content/smush-webp/2025/01/UPDATED-January-30-2025-fewer-decimal-1024x744.png.webp"])





# ----- Helper function to calculate energy savings based on behavior -----
def calculate_savings(lighting, appliances, electronics, heating, cooling):
    """
    lighting, appliances, electronics, heating, cooling: % reduction
    Returns a dict with adjusted energy consumption for each category
    """
    # Base annual energy usage in kWh for each category (example values)
    base_energy = {
        "Lighting": 1000,
        "Appliances": 1500,
        "Electronics": 1200,
        "Heating": 2000,
        "Cooling": 1800
    }

    saved_energy = {
        "Lighting": base_energy["Lighting"] * (1 - lighting / 100),
        "Appliances": base_energy["Appliances"] * (1 - appliances / 100),
        "Electronics": base_energy["Electronics"] * (1 - electronics / 100),
        "Heating": base_energy["Heating"] * (1 - heating / 100),
        "Cooling": base_energy["Cooling"] * (1 - cooling / 100)
    }
    return saved_energy, base_energy


# ----- Tabs -----


# Overview tab

def page_renew():
    st.markdown("# Renewable Energy Sources")

    st.subheader("Why renewables?")
    st.markdown("""
    Switching to renewable energy sources could provide cheaper energy bills as well as a constant supply and clean energy.
    Renewables help combat climate change, improve air quality, and protect water resources. They are also sustainable — unlike
    fossil fuels such as coal, oil, natural gas, and even uranium (for nuclear power), which will eventually run out.
    """)

    tabs = st.tabs([
        "Wind",
        "Solar",
        "Geothermal",
        "Biomass",
        "Hydro-electric",
        "Piezoelectricity"
    ])

    # Small wrapper function for clean centered carousel
    def show_carousel(img_list):
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])  # Balanced centered layout
        with col2:
            st.markdown(
                "<div style='max-width:600px;margin:0 auto;'>",
                unsafe_allow_html=True,
            )
            imageCarouselComponent(imageUrls=img_list, height=300)  # << updated height here
            st.markdown("</div>", unsafe_allow_html=True)

    # Shared simulator function (unchanged)
    def renewable_simulator(source_name, eff, co2_factor):
        st.markdown("---")
        st.subheader(f"⚡ Compare: With {source_name} vs Without It")

        st.info(f"""
        Adjust the sliders below to see how switching to **{source_name} energy** affects your energy costs
        and carbon emissions. The bar charts show your comparison **before and after adoption**.
        """)

        col1, col2 = st.columns(2)
        with col1:
            adoption = st.slider(f"{source_name} adoption level (%)", 0, 100, 50,
                                 key=f"{source_name}_adopt")
            annual_cost = st.number_input("💰 Current annual energy cost ($)", 500, 10000, 2500,
                                          step=50, key=f"{source_name}_cost")

        with_adoption_savings = annual_cost * (adoption / 100) * eff
        cost_with = annual_cost - with_adoption_savings
        cost_without = annual_cost
        co2_reduction = (adoption / 100) * co2_factor * 100
        co2_with = 100 - co2_reduction

        df_cost = pd.DataFrame({"Scenario": ["Without Renewable", f"With {source_name}"],
                                "Annual Cost ($)": [cost_without, cost_with]})
        df_co2 = pd.DataFrame({"Scenario": ["Without Renewable", f"With {source_name}"],
                               "CO₂ Emissions (%)": [100, co2_with]})

        cost_chart = alt.Chart(df_cost).mark_bar(cornerRadiusTopLeft=5, cornerRadiusTopRight=5) \
            .encode(x="Scenario:N", y="Annual Cost ($):Q",
                    color=alt.Color("Scenario:N",
                                    scale=alt.Scale(domain=["Without Renewable", f"With {source_name}"],
                                                    range=["#E74C3C", "#27AE60"]),
                                    legend=None)) \
            .properties(title="💸 Annual Energy Cost Comparison", height=300)

        co2_chart = alt.Chart(df_co2).mark_bar(cornerRadiusTopLeft=5, cornerRadiusTopRight=5) \
            .encode(x="Scenario:N", y="CO₂ Emissions (%):Q",
                    color=alt.Color("Scenario:N",
                                    scale=alt.Scale(domain=["Without Renewable", f"With {source_name}"],
                                                    range=["#E67E22", "#2ECC71"]),
                                    legend=None)) \
            .properties(title="🌿 CO₂ Emission Impact", height=300)

        st.markdown("### 📊 Visual Comparison")
        c1, c2 = st.columns(2)
        c1.altair_chart(cost_chart, use_container_width=True)
        c2.altair_chart(co2_chart, use_container_width=True)

        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        col1.metric("💰 Estimated Annual Savings", f"${with_adoption_savings:,.0f}")
        col2.metric("🌿 Estimated CO₂ Reduction", f"{co2_reduction:.1f}%")

        st.success(
            f"By adopting **{adoption}% {source_name} energy**, you could save about **${with_adoption_savings:,.0f} per year** "
            f"and reduce emissions by **{co2_reduction:.1f}%** compared to fossil fuel energy."
        )

    # 🌬 WIND TAB
    with tabs[0]:
        st.markdown("""
        ### Wind Energy
        Wind turbines generate electricity by converting kinetic energy from the wind into mechanical energy using large blades.
        The spinning shaft powers a generator to produce electricity. Wind farms are typically located in windy open areas or
        on hilltops where airflow is strong and consistent.
        """)
        show_carousel([
            "https://www.energy.gov/sites/default/files/styles/full_article_width/public/Turbine_Comparison.jpg?itok=2tmJtLXQ",
            "https://caltechsites-prod-assets.s3.amazonaws.com/scienceexchange/images/wind-turbine-future-energy.2e16d0ba.fill-933x525-c100.jpg",
            "https://files.lexology.com/images/lexology/static/f0abac77-75d7-4e00-85c5-ce78f31e7d01.png",
            "https://assets.nationbuilder.com/canadaaction/pages/3664/meta_images/original/wind_power_in_canada_facts_statistics.JPG?1717994021",
            "https://www.repsol.com/content/dam/repsol-corporate/es/energia-e-innovacion/parques%20eolicos%20on%20shore%20y%20near%20shore.jpg",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzfpB4vPsHSa6PO7FMVkVF0We5MzbTIaILRA&s",
        ])
        renewable_simulator("Wind", 0.35, 0.4)

    # ☀️ SOLAR TAB
    with tabs[1]:
        st.markdown("""
        ### Solar Panels
        Solar panels convert sunlight into electricity using the photovoltaic effect. Although solar systems can be expensive
        to install, they often pay for themselves over time — especially in regions with high sunlight exposure — and can still
        generate energy even in cloudy conditions.
        """)
        show_carousel([
            "https://www.gridserve.com/wp-content/uploads/2022/08/1.-Listicle-Solar-is-awesome-1024x683.jpg",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRjJzcS6_xYfMYPOCTz_u3pT-J8whciq6r7pw&s",
            "hhttps://amplussolar.com/blog/wp-content/uploads/2025/01/Types-of-Solar-Panels.jpg",
            "https://artisanelectricinc.com/wp-content/uploads/2019/09/Backsheet.jpg",
        ])
        renewable_simulator("Solar", 0.3, 0.35)

    # 🌋 GEOTHERMAL TAB
    with tabs[2]:
        st.markdown("""
        ### Geothermal
        Geothermal energy harnesses heat from beneath the Earth's surface. Unlike wind or solar, it is not weather-dependent,
        making it one of the most stable and reliable renewable energy sources.
        """)
        show_carousel([
            "https://emission-index.b-cdn.net/wp-content/uploads/2023/11/64d3e36f7274f04d628bdd0a_Geothermal-Energy-1-01.png",
            "https://dandelionenergy.com/wp-content/uploads/2019/10/IjkKdqvok6ktMM6kQU7fPOzDrfVwZZM4qOH-Y_QdsLi7F3f5DMDSZONn0wowWwFd17Vp8WM3mrp6yueNHt-1wK-0oHCfmy2-nCAPKOihUYUnJZIYSkjp-gadFCzrj7miIU2FgTw8",
            "https://www.24hplans.com/wp-content/uploads/2018/01/Geothermal-Heating-Digging-the-Ground.jpeg",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXoVjxS_EUAdCvwQx6FEkb32wp6wPKDSM_NA&s",
        ])
        renewable_simulator("Geothermal", 0.25, 0.3)

    # 🌾 BIOMASS TAB
    with tabs[3]:
        st.markdown("""
        ### Biomass
        Biomass energy is produced from organic matter such as plants or animal waste. It can be converted into usable energy
        like heat, electricity, or biofuels through combustion, gasification, or fermentation.
        """)
        show_carousel([
            "https://www.mdpi.com/energies/energies-16-01783/article_deploy/html/images/energies-16-01783-g001.png",
            "https://powerzone.clarkpublicutilities.com/wp-content/uploads/2022/03/CPUD22_Biomass-Cycle-1-scaled.jpg",
            "https://images.theecoexperts.co.uk/wp-content/uploads/2022/02/Biomass-power-plant-in-the-UK.jpg",
            "https://www.eia.gov/energyexplained/biomass/images/wastetoenergy.png",
        ])
        renewable_simulator("Biomass", 0.2, 0.2)

    # 💦 HYDRO TAB
    with tabs[4]:
        st.markdown("""
        ### Hydro-electric
        Hydroelectric power is generated using the movement of water in rivers, lakes, or ocean tides. Because flowing water is
        highly consistent in many regions, hydroelectric energy is known for being one of the most reliable sources for grid
        stability.
        """)
        show_carousel([
            "https://letstalkscience.ca/sites/default/files/2019-11/Carillon_Hydroelectric_Power_Station.jpg",
            "https://www.nbpower.com/media/1664/d-html-en-safety_learning-learning-electricity_generated-hydro-hydro-anim-en.gif",
            "https://powerzone.clarkpublicutilities.com/wp-content/uploads/2022/03/CPUD22_Hydroelectric-Dam_2000x2000.jpg",
            "https://cleanpower.org/wp-content/uploads/2022/03/hoover-dam-aerial-photo-2048x1365.jpg",
        ])
        renewable_simulator("Hydro-electric", 0.28, 0.25)

    # ⚙️ PIEZOELECTRICITY TAB
    with tabs[5]:
        st.markdown("""
        ### Piezoelectricity
        Piezoelectricity occurs when certain materials generate an electric charge in response to applied mechanical stress.
        Vibrations, pressure, or movement can be converted into small amounts of electricity — a concept often used in sensors,
        lighter igniters, and emerging micro-scale power technologies.
        """)
        show_carousel([
            "https://blog.piezo.com/hs-fs/hubfs/image.png?width=450&name=image.png",
            "http://pavegen.com/hs-fs/hubfs/Pavegen_April2025/images/Kia%20Hero%20-%20A%206.png?width=513&height=290&name=Kia%20Hero%20-%20A%206.png",
            "",
        ])
        renewable_simulator("Piezoelectricity", 0.1, 0.1)




def page_conserve():
    import streamlit as st

    st.markdown("# Energy Conservation")

    st.markdown("""
    Energy conservation means using less energy through smarter choices in how we shop, heat our homes,
    and use electricity. Small daily habits make a difference, but choosing efficient appliances and better
    home systems can reduce energy waste for years.
    """)

    tabs = st.tabs([
        "Test Windows & Doors",
        "Combat Phantom Power Consumption"
    ])

    # ========== TAB 1: FURNACE ==========



    # ========== TAB 2: WINDOWS ==========
    with tabs[0]:
        st.markdown("""
        ### Test Windows & Doors
        If your home isn't airtight, hot or cold air will leak out and waste energy. To check for drafts,
        hold a candle around window and door frames — if the flame flickers, there is a leak. Caulking the
        frames helps create an airtight seal and reduces heat loss.
        """)

        st.markdown("---")
        st.markdown("### Windows & Doors Quiz")

        w1 = st.radio("1) How do you check for air leaks?",
                      ["Use a candle to detect flickering", "Turn on a fan", "Tap the window glass"],
                      index=None)

        w2 = st.radio("2) Why do drafts waste energy?",
                      ["They let in sunlight",
                       "Heated/cooled air escapes and HVAC must work harder",
                       "They increase humidity"],
                      index=None)

        w3 = st.radio("3) What is the solution if a draft is found?",
                      ["Install a new furnace",
                       "Use caulking around the frames",
                       "Replace light bulbs"],
                      index=None)

        if st.button("Submit Windows Answers"):
            answers = [
                "Use a candle to detect flickering",
                "Heated/cooled air escapes and HVAC must work harder",
                "Use caulking around the frames"
            ]
            user = [w1, w2, w3]
            score = sum([user[i] == answers[i] for i in range(3)])
            st.success(f"Your score: {score}/3")
            explanations = [
                "A flickering flame shows moving air — a sign of leakage.",
                "Air leaks cause constant heating/cooling loss.",
                "Caulking seals gaps to stop heat from escaping."
            ]
            for i in range(3):
                if user[i] == answers[i]:
                    st.write(f"✅ Q{i+1}: {explanations[i]}")
                else:
                    st.write(f"❌ Q{i+1}: {explanations[i]}")


    # ========== TAB 3: PHANTOM POWER ==========
    with tabs[1]:
        st.markdown("""
        ### Combat Phantom Power Consumption
        Plugged-in devices like televisions, cable boxes, and game consoles consume energy even when not in use. 
        Chargers that remain plugged in also draw power even when nothing is connected. Unplugging devices or using 
        smart plugs can help block this wasted energy.
        """)

        st.markdown("---")
        st.markdown("### Phantom Power Quiz")

        p1 = st.radio("1) What is phantom power?",
                      ["Energy used by plugged-in devices even when off",
                       "Power used by lightbulbs",
                       "Energy from heating water"],
                      index=None)

        p2 = st.radio("2) Which of the following still draws power when idle?",
                      ["A disconnected lamp",
                       "A phone charger still plugged in",
                       "A bookcase"],
                      index=None)

        p3 = st.radio("3) What reduces phantom power best?",
                      ["Leaving everything plugged in",
                       "Using smart plugs or unplugging devices",
                       "Installing a new heater"],
                      index=None)

        if st.button("Submit Phantom Answers"):
            answers = [
                "Energy used by plugged-in devices even when off",
                "A phone charger still plugged in",
                "Using smart plugs or unplugging devices"
            ]
            user = [p1, p2, p3]
            score = sum([user[i] == answers[i] for i in range(3)])
            st.success(f"Your score: {score}/3")
            explanations = [
                "Phantom power is wasted electricity from devices in standby.",
                "Chargers and consoles keep drawing small amounts of power.",
                "Smart plugs cut standby power automatically."
            ]
            for i in range(3):
                if user[i] == answers[i]:
                    st.write(f"✅ Q{i+1}: {explanations[i]}")
                else:
                    st.write(f"❌ Q{i+1}: {explanations[i]}")
    st.markdown("---")
    tabss = st.tabs([
        "Refrigerators",
        "Smartphones",
        "Freezers",
        "Dryers",
    ])
    with tabss[0]:
        st.subheader("Energy Efficient Models")
        st.markdown("When looking for refrigerators, typically designs with top freezer, or just smaller sizes tend to be more energy efficient. The most important thing to be looking for is that the model has a Energy Star on it and has a lower Global Warming Potential(GWP).")
        st.subheader("High Energy Consumption Models")
        st.markdown("Models that are old and have outdated technology often are the least energy efficient. Refrigerators with energy intensive function such as, built in ice makers or water dispensers has a higher energy usage.")
        st.subheader("Key Factors")
        st.markdown(
            """
            - Size
            - Energy Star Models
            - Age
            - Functions
            """
        )

    with tabss[1]:
        st.subheader("Energy Efficient Models")
        st.markdown("Smartphones that are newer or have smaller chips are more energy efficient than others. Larger batteries, and memory storage also can contribute. Settings that can be easily changed that can help reduce you energy usage includes lowering your screen brightness, disabling unnecessary wireless functions (Bluetooth, Wi-Fi, GPS) and power saving models can all minimize energy utilization.")
        st.subheader("High Energy Consumption Models")
        st.markdown("Smartphones that are high is size, resolution, and ones that use power-draining hardware can lead to high energy consumption.")
        st.subheader("Key Factors")
        st.markdown(
            """
            - Size
            - Brightness
            - Resolution
            - Hardware
            """
        )
    with tabss[2]:
        st.subheader("Energy Efficient Models")
        st.markdown("Chest Freezers are the most efficient because their design minimizes cold air loss when it is opened. Another reason is because of its smaller size. ")
        st.subheader("High Energy Consumption Models")
        st.markdown("Upright freezers with an automatic defrost functions, because when it's opened a lot more cold air is released.")
        st.subheader("Key Factors")
        st.markdown(
            """
            - Defrost Functions,
            - Manual vs. Automatic
            - Age
            - Size
            - Energy Star certified models
            """
        )
    with tabss[3]:
        st.subheader("Energy Efficient Models")
        st.markdown("The most energy-efficient dryer is a heat pump dryer. This is because it uses a closed-loop system to recycle the heat. and can use 50% less energy than a standard one can.")
        st.subheader("High Energy Consumption Models")
        st.markdown("Models that are vented and standard tend to use more energy. Vented models vent hot, moist air outside which might clogg the ventilation system which causes extened drying time. ")
        st.subheader("Key Factors")
        st.markdown(
            """
            - Gas vs. electric
            - Energy Star Rating
            - Heat Settings
            """
        )
def page_contact():
    st.markdown("# Contact Us")
    st.markdown("""
    Have a question or suggestion? Get in touch with our team using the form below.
    """)

    with st.form("contact_form"):
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        email = st.text_input("Your Email")
        phone = st.text_input("Your Phone Number")
        message = st.text_area("Message", height=160)

        submitted = st.form_submit_button("Send Message")

        if submitted:
            if not first_name or not last_name or not email or not phone or not message :
                st.error("Please fill in all fields before submitting.")
            else:
                # Construct a mailto link
                recipients = (
                    "julian.lee31@stgeorges.bc.ca,"
                    "joshua.tse31@stgeorges.bc.ca,"
                    "harvey.tjoa31@stgeorges.bc.ca"
                )
                subject = f"Contact Form Submission from {first_name} {last_name}"
                body = f"From: {first_name} {last_name} {phone} {email})%0D%0A%0D%0A{message}"

                mailto_link = f"mailto:{recipients}?subject={subject}&body={body}"

                st.markdown(
                    f"""
                    <a href="{mailto_link}" target="_blank"
                       style="display:inline-block;margin-top:15px;padding:10px 16px;
                       background-color:#2e7d32;color:white;border-radius:8px;
                       text-decoration:none;font-weight:500;">
                       Click here to send email
                    </a>
                    """,
                    unsafe_allow_html=True
                )

                st.success("Preview ready — click the button above to send your message.")

def page_sink_faucet():
    st.markdown("# Sink / Faucet")
    st.subheader("How Can We Save Water with a Sink Tap?")

    st.markdown("""
    Background: The average amount of water a tap uses is **10–15 litres per minute (lpm)**, 
    and the average person uses the tap for about **8 minutes every day**.
    """)

    tabs = st.tabs([
        "Brushing Your Teeth",
        "Low-flow Aerators"
    ])

    with tabs[0]:
        st.markdown("""
        ### Brushing Your Teeth

        When you brush your teeth, it is common for people to leave the tap on. A tap on average uses **10–15 litres per minute**, 
        and a person takes around **2 minutes** to brush their teeth **two times a day**. That means you could use **40 litres or more** 
        every day for no reason — just flowing straight down the drain.

        All you have to do is **turn the tap off while brushing**, and you can save more than **20 litres of water per day**, which also 
        saves **6–9 cents every day** just by changing this small habit.
        """)

    with tabs[1]:
        st.markdown("""
        ### Low-flow Aerators

        Low-flow aerators are very effective because they reduce the amount of water used per minute while **keeping or even increasing 
        water pressure**. Most modern faucets already have them built in, but if yours does not, they are **highly recommended**.

        Low-flow aerators can cut water use by **up to 50%** while making the stream smoother, gentler, and no-splash. They also help 
        control direction, so water doesn’t spray everywhere or bounce out of the sink.
        """)

    # ----------- Tap Water Waste Visualizer -----------
    st.markdown("---")
    st.markdown("## Tap Water Waste Visualizer")
    st.markdown("Use the sliders to see how much water is wasted — the drip speeds up as waste increases.")

    # Sliders
    minutes = st.slider("Minutes per day left running unnecessarily", 0, 15, 2)
    flow_rate = st.slider("Flow rate (litres per minute)", 10, 15, 12)

    # Calculations
    wasted_daily = minutes * flow_rate
    wasted_yearly = wasted_daily * 365

    # Dynamic drip speed mapping
    duration = 2.0 - (wasted_daily / 150.0) * 1.5
    duration = max(0.5, min(duration, 2.0))

    # Multi-drip threshold (>40L)
    multi_drip = wasted_daily > 40

    mcol, acol = st.columns([1, 1], vertical_alignment="top")

    with mcol:
        st.markdown("### Your Impact")
        c1, c2 = st.columns(2)
        c1.metric("Water wasted per day", f"{wasted_daily:,.0f} L")
        c2.metric("Water wasted per year", f"{wasted_yearly:,.0f} L")
        st.caption("Turn off the tap while brushing or add a low-flow aerator to reduce this dramatically.")

    with acol:
        faucet_container = st.empty()

        if minutes > 0:
            drops_html = (
                """
                <div class="drop d1"></div>
                <div class="drop d2"></div>
                <div class="drop d3"></div>
                """ if multi_drip else
                """<div class="drop d1"></div>"""
            )

            faucet_container.markdown(
                f"""
                <style>
                .faucet-wrap {{
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 180px;
                }}
                .faucet-container {{
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                }}
                .faucet-head {{
                    width: 90px;
                    height: 24px;
                    background-color: #8a8f96;
                    border-radius: 12px 12px 0 0;
                }}
                .faucet-pipe {{
                    width: 14px;
                    height: 50px;
                    background-color: #8a8f96;
                    margin-top: -2px;
                    border-radius: 0 0 10px 10px;
                }}
                .drop {{
                    width: 14px;
                    height: 14px;
                    background-color: #3f9ae0;
                    border-radius: 50%;
                    position: relative;
                    animation-name: drip;
                    animation-duration: {duration:.2f}s;
                    animation-iteration-count: infinite;
                    margin-top: 6px;
                    filter: drop-shadow(0 2px 2px rgba(0,0,0,0.15));
                }}
                .drop.d1 {{ animation-delay: 0s; }}
                .drop.d2 {{ animation-delay: {duration/3:.2f}s; }}
                .drop.d3 {{ animation-delay: {2*duration/3:.2f}s; }}

                @keyframes drip {{
                    0%   {{ opacity: 0; transform: translateY(0);   }}
                    20%  {{ opacity: 1; }}
                    80%  {{ opacity: 1; transform: translateY(56px); }}
                    100% {{ opacity: 0; transform: translateY(72px); }}
                }}
                </style>

                <div class="faucet-wrap">
                    <div class="faucet-container">
                        <div class="faucet-head"></div>
                        <div class="faucet-pipe"></div>
                        {drops_html}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            faucet_container.markdown(
                """
                <div style="display:flex;justify-content:center;align-items:center;height:180px;">
                    <div style="display:flex;flex-direction:column;align-items:center;">
                        <div style="width:90px;height:24px;background-color:#8a8f96;border-radius:12px 12px 0 0;"></div>
                        <div style="width:14px;height:50px;background-color:#8a8f96;margin-top:-2px;border-radius:0 0 10px 10px;"></div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    # ✅ success message AFTER animation (prevents </div> glitch)
    st.success(
        f"By simply turning off the tap while brushing, you could save roughly **{wasted_yearly:,.0f} litres per year**."
    )


def page_leaks():
    st.markdown("# Leaks")
    st.subheader("How Do Leaks Waste Water and How Can We Prevent Them?")

    st.markdown("""
    Leaks are one of the most overlooked sources of water waste in a household.  
    Even slow or hidden leaks can waste **dozens of litres per day**, adding up to thousands of litres per month.  
    Leaks often come from **water pressure issues, frozen pipes, or faulty HVAC condensation systems**.  
    Understanding what causes them — and how to detect them early — can prevent expensive repairs and major water loss.
    """)

    tabs = st.tabs([
        "Water Pressure",
        "Frozen Pipes",
        "HVAC Systems",
        "Detecting High Pressure"
    ])

    with tabs[0]:
        st.markdown("""
        ### Water Pressure

        High water pressure in pipes increases the risk of leaks because it puts stress on joints,
        fittings, and older plumbing systems. Over time, excess pressure can loosen connections and
        create small cracks that eventually become leaks. Maintaining a proper pressure range protects
        both your plumbing and your water usage.
        """)

    with tabs[1]:
        st.markdown("""
        ### Frozen Pipes

        Leaks often happen because of **frozen pipes**, which expand as the trapped water inside freezes.
        This can cause pipes to burst or crack. Wrapping exposed pipes with foam insulation (even pool noodles)
        can significantly reduce the chance of bursting. Even a **small drip leak** from thawing water can waste
        **over 90 litres per day**.
        """)

    with tabs[2]:
        st.markdown("""
        ### HVAC Systems

        Without proper HVAC maintenance, condensation can pool or clog drainage pipes, eventually causing leaks.
        Faulty HVAC systems can create moisture buildup that damages more than pipes — it can affect walls,
        ceilings, and floors. If you notice unexpected water in your home, an HVAC technician might be needed
        to inspect the system for hidden condensation leaks.
        """)

    with tabs[3]:
        st.markdown("""
        ### Detecting High Pressure

        To check if you have high pressure, use a **water pressure gauge** and attach it to an outdoor hose.
        Make sure no other taps or appliances are running, then turn the hose fully on.  
        If the gauge reads **above 80 psi**, your water pressure is too high and should be lowered using a
        pressure regulator (turning it counter-clockwise).
        """)

    st.markdown("---")
    st.markdown("## Quick Leak Prevention Quiz")

    q1 = st.radio("1) What happens when water pressure is too high?",
                  ["It improves water efficiency", "It increases pipe strain and leak risk", "It lowers HVAC usage"], index=None)

    q2 = st.radio("2) Why do frozen pipes often cause leaks?",
                  ["They shrink and seal tighter", "They expand and burst/crack", "They release cold steam"], index=None)

    q3 = st.radio("3) How can HVAC systems cause leaks?",
                  ["By cooling the home too quickly", "By building condensation or clogging drains", "By using too much electricity"], index=None)

    q4 = st.radio("4) What reading on a pressure gauge indicates high pressure?",
                  ["Over 80 psi", "Below 30 psi", "Exactly 60 psi"], index=None)

    if st.button("Submit Answers"):
        score = 0
        answers = [
            "It increases pipe strain and leak risk",
            "They expand and burst/crack",
            "By building condensation or clogging drains",
            "Over 80 psi"
        ]
        user = [q1, q2, q3, q4]

        for i in range(4):
            if user[i] == answers[i]:
                score += 1

        st.success(f"Your Score: {score}/4")

        explanations = [
            "High pressure stresses plumbing joints and increases leak risk.",
            "Frozen pipes expand and crack, which leads to leaking as they thaw.",
            "HVAC condensation or clogged drain lines can cause hidden leaks.",
            "Anything over 80 psi is considered too high and should be regulated."
        ]

        for i in range(4):
            if user[i] == answers[i]:
                st.write(f"✅ Q{i+1}: {explanations[i]}")
            else:
                st.write(f"❌ Q{i+1}: {explanations[i]}")




# =========================================
# NAVIGATION (Home is TOP-LEVEL)
# =========================================
PAGES = {
    "": [
        st.Page(page_home, title="Home")
    ],
    "Water Saving": [
        st.Page(page_water, title="Overview"),
        st.Page(page_toilets, title="Toilets"),
        st.Page(page_shower, title="Shower"),
        st.Page(page_washing_machine, title="Washing Machine"),
        st.Page(page_sink_faucet, title="Sink / Faucet"),
        st.Page(page_leaks, title="Leaks")

    ],

    "HVAC": [
        st.Page(page_hvac, title="Overview"),
        st.Page(page_heating, title="Heating"),
        st.Page(page_vent, title="Ventilation"),
        st.Page(page_ac, title="Air Conditioning"),   # ✅ add this line
    ],

    "Energy Saving": [
        st.Page(page_energy, title="Overview"),
        st.Page(page_renew, title="Renewable Energy Sources"),
        st.Page(page_conserve, title="Energy Conservation"),
    ],
    "Other": [
        st.Page(page_rebate, title="Rebate"),
        st.Page(page_contact, title="Contact Us")
    ]

}


pg = st.navigation(PAGES, position="sidebar")
pg.run()

# =========================================
# FOOTER
# =========================================
st.markdown(
    '<div class="footer">Credits: Joshua Tse, Harvey Tjoa, and Julian Lee (2025)</div>',
    unsafe_allow_html=True
)