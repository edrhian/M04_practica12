import xml.etree.ElementTree as ET
# Funcio que crea un xml
def createXMLStudents():
    p_students = ET.Element('students')
    #Student 1
    c_student1 = ET.SubElement(p_students, 'student')
    sc_name1 = ET.SubElement(c_student1, 'name')
    sc_name1.text = "Gustavo"
    sc_surname1 = ET.SubElement(c_student1, 'surname')
    sc_surname1.text = "Alfonso"
    sc_email1 = ET.SubElement(c_student1, 'email')
    sc_email1.text = "gAlfonso@gmail.com"
    sc_dni1 = ET.SubElement(c_student1, 'dni')
    sc_dni1.text = "73458602Y"
    #Student 2
    c_student2 = ET.SubElement(p_students, 'student')
    sc_name2 = ET.SubElement(c_student2, 'name')
    sc_name2.text = "Jose"
    sc_surname2 = ET.SubElement(c_student2, 'surname')
    sc_surname2.text = "Alejandro"
    sc_email2 = ET.SubElement(c_student2, 'email')
    sc_email2.text = "jAlejandro@gmail.com"
    sc_dni2 = ET.SubElement(c_student2, 'dni')
    sc_dni2.text = "95417470S"
    #Student 3
    c_student3 = ET.SubElement(p_students, 'student')
    sc_name3 = ET.SubElement(c_student3, 'name')
    sc_name3.text = "Simon"
    sc_surname3 = ET.SubElement(c_student3, 'surname')
    sc_surname3.text = "Andres"
    sc_email3 = ET.SubElement(c_student3, 'email')
    sc_email3.text = "sAndres@gmail.com"
    sc_dni3 = ET.SubElement(c_student3, 'dni')
    sc_dni3.text = "35080361W"
    # Student 4
    c_student4 = ET.SubElement(p_students, 'student')
    sc_name4 = ET.SubElement(c_student4, 'name')
    sc_name4.text = "Giselle"
    sc_surname4 = ET.SubElement(c_student4, 'surname')
    sc_surname4.text = "Ter"
    sc_email4 = ET.SubElement(c_student4, 'email')
    sc_email4.text = "gTer@gmail.com"
    sc_dni4 = ET.SubElement(c_student4, 'dni')
    sc_dni4.text = "64682124Y"
    # Student 5
    c_student5 = ET.SubElement(p_students, 'student')
    sc_name5 = ET.SubElement(c_student5, 'name')
    sc_name5.text = "Edrhian"
    sc_surname5 = ET.SubElement(c_student5, 'surname')
    sc_surname5.text = "Valerio"
    sc_email5 = ET.SubElement(c_student5, 'email')
    sc_email5.text = "eValerio@gmail.com"
    sc_dni5 = ET.SubElement(c_student5, 'dni')
    sc_dni5.text = "38526751A"

    # Atributs
    c_student1.set('Country', 'Spain')

    c_student2.set('Country', 'Spain')

    c_student3.set('Country', 'France')

    c_student4.set('Country', 'Italy')

    c_student5.set('Country', 'Spain')
    #Indentacio i creacio de fitxer
    ET.indent(p_students)
    tree = ET.ElementTree(p_students)
    tree.write("exercici_A.xml")

    return (ET.dump(p_students))
