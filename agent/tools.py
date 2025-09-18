from src.apis.job_fit_api import predict_fit
from src.apis.salary_api import predict_salary
from src.apis.resume_api import predict_resume
from src.apis.hiring_api import predict_hiring

tools = {
    "check_job_fit": predict_fit,
    "predict_salary": predict_salary,
    "screen_resume": predict_resume,
    "get_priority": predict_hiring,
    # add other tools as needed
}
