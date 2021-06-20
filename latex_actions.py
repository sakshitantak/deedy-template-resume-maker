import os
path = os.path.join(os.getcwd(), 'resume_files')
os.chdir(path)

class LatexDocument():

    def __init__(self):
        self.work_exp_title = False
        self.education_title = False
        self.projects_title = False
        self.skills_title = False
        self.coursework_title = False
        self.interests_title = False

    def set_details(self, fname, lname, website, email, phone, github, linkedin):
        with open('resume_template.tex', 'r') as file:
            text = file.read()
            text = text.replace('<First>', fname)
            text = text.replace('<Last>', lname)
            text = text.replace('<email>', email)
            if website != "":
                text = text.replace('<website>', website)
            else:
                text = text.replace('r\newcommand{\yourWebsite}{<website>}', '')

            if phone != "":
                text = text.replace('<phone>', phone)
            else:
                text = text.replace(r'\newcommand{\yourPhone}{<phone}', '')

            if github != "":
                text = text.replace('<github username>', github)
            else:
                text = text.replace(r'\newcommand{\githubUserName}{<github username>}', '')

            if linkedin != "":
                text = text.replace('<linkedin username>', linkedin)
            else:
                text = text.replace(r'\newcommand{\linkedInUserName}{<linkedin username>}', '')

            with open('resume_new.tex', 'w') as output:
                output.write(text)
            output.close()
        file.close()

    def make_experience_section(self, company_name, role, city, country, start_month, start_year, end_month, end_year, description):
        with open('resume_new.tex', 'a') as file:
            if self.work_exp_title == False:
                file.writelines('\n\section{ Work Experience }\n')
                self.work_exp_title = True
            content = r"\resumeHeading{" + company_name + "}{" + role + "}{" + city + " ," + country + "}{" + start_month + " " + start_year + " - " + end_month + " " + end_month + " " + end_year + "}" + "\n" + r"\begin{tightemize}" + "\n" + "\item " + description + "\n" + "\end{tightemize}\n\sectionsep\n\n"
            file.write(content)
        file.close()

    def make_education_section(self, degree, specialization, university, gpa, city, country, grad_month, grad_year):
        with open('resume_new.tex', 'a') as file:
            if self.education_title == False:
                file.writelines('\section{ Education }\n')
                self.education_title = True
            content = "\educationHeading{" + degree + " in " + specialization + "}{" + university + "}{" + city + ", " + country + "}{" + grad_month + " " + grad_year + "}\n" + "\gpa{" + gpa + "}\n\sectionsep\n\n"
            file.write(content)
        file.close()

    def make_projects_section(self, project_name, project_link, stack_description, project_summary):
        with open('resume_new.tex', 'a') as file:
            if self.projects_title == False:
                file.writelines('\section{ Projects }\n')
                self.projects_title = True
            content = "\Project{" + project_name + "}{" + project_link + "}\n" + "\descript{" + stack_description + r"}\\" + "\n" + project_summary + "\n\sectionsep\n\n"
            file.write(content)
        file.close()

    def make_skills_section(self, languages, technologies):
        with open('resume_new.tex', 'a') as file:
            if self.skills_title == False:
                file.writelines("\section{ Skills }\n")
                self.skills_title = True
            content = r"\begin{resumeSkillList}" + "\n" + "\singleItem{Languages:}{"
            i = 0
            for language in languages:
                if i % 16 == 0 and i != 0:
                    content += r"\\" + "\n" + language + " "
                content += language + " "
                i+=1
            i = 0
            content += "}\n" + r"\\" + "\singleItem{Technologies:}{"
            for technology in technologies:
                if i % 16 == 0 and i != 0:
                    content += r"\\" + "\n" + technology + " "
                content += technology + " "
                i+=1
            content += "}\n\end{resumeSkillList}\n\sectionsep\n\n"
            file.write(content)
        file.close()

    def make_coursework_section(self, courses):
        with open('resume_new.tex', 'a') as file:
            if self.coursework_title == False:
                file.writelines("\section{Course Work}\n")
                self.coursework_title = True
            content = r"\begin{resumeSkillList}" + "\n{"
            i = 0
            for course in courses:
                if i % 16 == 0 and i != 0:
                    content += r"\\" + "\n" + course + " "
                content += course + " "
                i+=1
            content += "}\n\end{resumeSkillList}\n\sectionsep\n\n"
            file.write(content)
        file.close()

    def make_interests_section(self, interests):
        with open('resume_new.tex', 'a') as file:
            if self.interests_title == False:
                file.writelines("\section{Interests & Hobbies}\n")
                self.interests_title = True
            i = 0
            content = "\begin{resumeSkillList}\n{"
            for interest in interests:
                if i % 16 == 0 and i != 0:
                    content += r"\\" + "\n" + interest + " "
                content += interest + r" "
                i += 1
            content += "}\n\end{resumeSkillList}\n\sectionsep\n\n"



    def end_document(self):
        with open('resume_new.tex', 'a') as file:
            end = r"\end{document}"
            file.writelines(end)
        file.close()