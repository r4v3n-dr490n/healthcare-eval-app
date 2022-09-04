import sqlalchemy
from sqlalchemy import create_engine, Boolean
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class EvalForm(Base):
    __tablename__ = 'evalform_table'
    id = Column(Integer, primary_key=True,autoincrement=True)
    # basic data
    evaluator_name = Column(String)
    unit_name = Column(String)
    eval_date = Column(String)

    # pt rights
    pt_rights1 = Column(Integer)
    pt_rights2 = Column(Integer)
    pt_rights3 = Column(Integer)
    pt_rights4 = Column(Integer)
    pt_rights_neg = Column(String)
    pt_rights_sol = Column(String)
    pt_rights_notes = Column(String)

    # Emergency
    emer1 = Column(Integer)
    emer2 = Column(Integer)
    emer3 = Column(Integer)
    emer4 = Column(Integer)
    emer5 = Column(Integer)
    emer_neg = Column(String)
    emer_sol = Column(String)
    emer_notes = Column(String)

    # Lab
    lab1 = Column(Integer)
    lab2 = Column(Integer)
    lab3 = Column(Integer)
    lab4 = Column(Integer)
    lab_neg = Column(String)
    lab_sol = Column(String)
    lab_notes = Column(String)

    # Pharmacy
    pharma1 = Column(Integer)
    pharma2 = Column(Integer)
    pharma3 = Column(Integer)
    pharma4 = Column(Integer)
    pharma5 = Column(Integer)
    pharma_neg = Column(String)
    pharma_sol = Column(String)
    pharma_notes = Column(String)

    # Infection Control
    infect1 = Column(Integer)
    infect2 = Column(Integer)
    infect3 = Column(Integer)
    infect4 = Column(Integer)
    infect5 = Column(Integer)
    infect6 = Column(Integer)
    infect_neg = Column(String)
    infect_sol = Column(String)
    infect_notes = Column(String)

    # Environmental Safety
    env1 = Column(Integer)
    env2 = Column(Integer)
    env3 = Column(Integer)
    env4 = Column(Integer)
    env5 = Column(Integer)
    env_neg = Column(String)
    env_sol = Column(String)
    env_notes = Column(String)

    # Dentistry
    dent1 = Column(Integer)
    dent2 = Column(Integer)
    dent3 = Column(Integer)
    dent_neg = Column(String)
    dent_sol = Column(String)
    dent_notes = Column(String)

    # Healthcare Management
    manage1 = Column(Integer)
    manage2 = Column(Integer)
    manage3 = Column(Integer)
    manage4 = Column(Integer)
    manage_neg = Column(String)
    manage_sol = Column(String)
    manage_notes = Column(String)

    # Family Medicine
    family1 = Column(Integer)
    family2 = Column(Integer)
    family3 = Column(Integer)
    family4 = Column(Integer)
    family_neg = Column(String)
    family_sol = Column(String)
    family_notes = Column(String)

    # Mobadarat
    mobad1 = Column(Integer)
    mobad2 = Column(Integer)
    mobad3 = Column(Integer)
    mobad4 = Column(Integer)
    mobad5 = Column(Integer)
    mobad6 = Column(Integer)
    mobad7 = Column(Integer)
    mobad8 = Column(Integer)
    mobad9 = Column(Integer)
    mobad10 = Column(Integer)
    mobad11 = Column(Integer)
    mobad12 = Column(Integer)
    mobad_neg = Column(String)
    mobad_sol = Column(String)
    mobad_notes = Column(String)

    # Home Isolation
    isolate1 = Column(Integer)
    isolate2 = Column(Integer)
    isolate3 = Column(Integer)
    isolate_neg = Column(String)
    isolate_sol = Column(String)
    isolate_notes = Column(String)

    # Students Health Services
    stud1 = Column(Integer)
    stud2 = Column(Integer)
    stud3 = Column(Integer)
    stud4 = Column(Integer)
    stud5 = Column(Integer)
    stud6 = Column(Integer)
    stud_neg = Column(String)
    stud_sol = Column(String)
    stud_notes = Column(String)

    # New Pregnant Women
    new_born1 = Column(Integer)
    new_preg1 = Column(Integer)
    preg1 = Column(Integer)
    preg_notes = Column(String)

    # Average infants visits
    new_born2 = Column(Integer)
    no_child = Column(Integer)
    avg_child_visit = Column(Integer)
    infants_notes = Column(String)

    # Percentage of pregnant women
    new_preg2 = Column(Integer)
    new_preg3 = Column(Integer)
    avg_preg_visit = Column(Integer)

    # Percentage of one year infants hge
    infant1 = Column(Integer)
    infant2 = Column(Integer)
    avg_infant_hge = Column(Integer)
    hge_notes = Column(String)

    # IMCI
    is_doctor = Column(Boolean)
    infant3 = Column(Integer)
    infant4 = Column(Integer)
    imci_avg = Column(Integer)
    imci_notes = Column(String)


if __name__ == '__main__':
    engine = create_engine('sqlite:///app_database.db')
    Base.metadata.create_all(engine)
