from pytest_bdd import when, then, parsers, scenarios

from tests import FlowHired

scenarios("01_flow_to_hired.feature", features_base_dir="tests/features/hired/")
CREATE_CANDIDATE = FlowHired()


@when(parsers.parse("submit user: {username} and password: {password} and click on the enter button"))
def submit_credentials(username, password):
    CREATE_CANDIDATE.authentication.user_name(username)
    CREATE_CANDIDATE.authentication.password(password)
    CREATE_CANDIDATE.authentication.login()
    CREATE_CANDIDATE.authentication.make_click_recruitment()
    CREATE_CANDIDATE.register.click_add()


@when(parsers.parse("fill in First Name with {firstname}"))
def fill_first_name(firstname):
    CREATE_CANDIDATE.register.first_name(firstname)


@when(parsers.parse("fill in Middle Name with {middle_name}"))
def fill_middle_name(middle_name):
    CREATE_CANDIDATE.register.middle_name(middle_name)


@when(parsers.parse("fill in Last Name with {lastname}"))
def fill_last_name(lastname):
    CREATE_CANDIDATE.register.last_name(lastname)


@when(parsers.parse("fill in Email with {email}"))
def fill_email(email):
    CREATE_CANDIDATE.register.email(email)


@when(parsers.parse("fill in Contact Number with {phone}"))
def fill_email(phone):
    CREATE_CANDIDATE.register.phone(phone)


@when(parsers.parse("fill in Keywords with {keywords}"))
def fill_keywords(keywords):
    CREATE_CANDIDATE.register.keywords(keywords)


@when(parsers.parse("fill in Notes with {notes}"))
def fill_notes(notes):
    CREATE_CANDIDATE.register.notes(notes)


@when(parsers.parse("select Vacancy with payroll administrator role"))
def select_vacancy_role():
    CREATE_CANDIDATE.register.select_vacancy()


@when(parsers.parse("upload Resume with {path}"))
def upload_cv_file(path):
    CREATE_CANDIDATE.register.upload(path)


@when(parsers.parse("click on consent to keep data"))
def click_consent():
    CREATE_CANDIDATE.register.click_consent()


@when(parsers.parse("click on Save"))
def fill_notes():
    CREATE_CANDIDATE.register.click_save()


@when(parsers.parse("click on Shortlist button"))
def click_shortlist():
    CREATE_CANDIDATE.register.click_shortlist()


@when(parsers.parse("click on save shortlist button"))
def click_save_shortlist():
    CREATE_CANDIDATE.register.click_save_shortlist()


@when(parsers.parse("click on schedule interview"))
def click_schedule_interview():
    CREATE_CANDIDATE.register.click_schedule_interview()


@when(parsers.parse("fill interview title with {title}"))
def fill_interview_title(title):
    CREATE_CANDIDATE.register.interview_title(title)


@when(parsers.parse("fill interview date with {date}"))
def fill_interview_date(date):
    CREATE_CANDIDATE.register.interview_date(date)


@when(parsers.parse("fill interview time with {time}"))
def fill_interview_time(time):
    CREATE_CANDIDATE.register.interview_time(time)


@when(parsers.parse("fill interviewer with {interviewer}"))
def fill_interviewer(interviewer):
    CREATE_CANDIDATE.register.interviewer(interviewer)


@when(parsers.parse("click on save interview"))
def click_save_interview():
    CREATE_CANDIDATE.register.click_save_schedule_interview()


@when(parsers.parse("click on passed interview"))
def click_passed_interview():
    CREATE_CANDIDATE.register.click_passed_interview()


@when(parsers.parse("click on save passed interview"))
def click_save_passed_interview():
    CREATE_CANDIDATE.register.click_save_passed_interview()


@when(parsers.parse("click on offer job button"))
def click_offer_job():
    CREATE_CANDIDATE.register.click_offer_job()


@when(parsers.parse("click on save offer job button"))
def click_save_offer_job():
    CREATE_CANDIDATE.register.click_save_offer_job()


@when(parsers.parse("click on hired button"))
def click_hired():
    CREATE_CANDIDATE.register.click_hired_button()


@when(parsers.parse("click on save hired button"))
def click_save_hired():
    CREATE_CANDIDATE.register.click_save_hired_button()


@then(parsers.parse("the candidate should be hired successfully"))
def verify_hired():
    assert CREATE_CANDIDATE.register.verify_hired() == "Status: Hired"
    CREATE_CANDIDATE.quit_page()
