# streamlit_app.py
import streamlit as st

st.title("🏠 Immobilien-Investitionsrechner")

kaufpreis = st.number_input("Kaufpreis (€)", value=300000)
nebenkosten = st.number_input("Nebenkosten (%)", value=10.0) / 100
renovierung = st.number_input("Renovierungskosten (€)", value=20000)
eigenkapital = st.number_input("Eigenkapital (€)", value=100000)
miete = st.number_input("Mieteinnahmen (€ / Monat)", value=1200)
zins = st.number_input("Zinssatz (%)", value=3.0) / 100
tilgung = st.number_input("Tilgung (%)", value=2.0) / 100
kosten = st.number_input("Nicht umlagefähige Kosten (€)", value=150)
ruecklagen = st.number_input("Verwaltung & Rücklagen (€)", value=100)
wertsteigerung = st.number_input("Wertsteigerung (%)", value=2.0) / 100

if st.button("Berechnen"):
    gesamtkosten = kaufpreis + kaufpreis * nebenkosten + renovierung
    fremdkapital = gesamtkosten - eigenkapital
    zins_m = fremdkapital * zins / 12
    tilgung_m = fremdkapital * tilgung / 12
    kredit_m = zins_m + tilgung_m
    ausgaben = kredit_m + kosten + ruecklagen
    cashflow = miete - ausgaben
    cashflow_jahr = cashflow * 12
    rendite_ohne = cashflow_jahr / eigenkapital * 100
    wertzuwachs = kaufpreis * wertsteigerung
    rendite_mit = (wertzuwachs + cashflow_jahr) / eigenkapital * 100

    st.subheader("📊 Ergebnis")
    st.write(f"Monatlicher Cashflow: {cashflow:.2f} €")
    st.write(f"Eigenkapitalrendite ohne Wertsteigerung: {rendite_ohne:.2f} %")
    st.write(f"Eigenkapitalrendite mit Wertsteigerung: {rendite_mit:.2f} %")
