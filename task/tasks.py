from celery import task
import time
from celery import shared_task
from django.core.mail import send_mail
from .models import Task, UpdateType, TaskTracker


@shared_task
def daily_update(sender_email):
    daily_report = Task.objects.filter(daily_updated = False)
    task1_tracker = ''
    task2_tracker = ''
    task3_tracker = ''
    task4_tracker = ''
    for report in daily_report:
        if report.task == 1:
            task1_tracker = task1_tracker + report.description + ' \n'
        elif report.task == 2:
            task2_tracker = task2_tracker + report.description + ' \n'
        elif report.task == 3:
            task3_tracker = task3_tracker + report.description + ' \n'
        elif report.task == 4:
            task4_tracker = task4_tracker + report.description + ' \n'

    update_type = UpdateType.objects.filter(duration='Daily').first()
    daily_update_list = TaskTracker.objects.filter(update_type=update_type.id)
    for d in daily_update_list:
        if d.task == 1:
            subject = 'Daily Update of Task 1.'
            receiver_email = d.email
            res = send_mail(subject, task1_tracker, sender_email, [receiver_email])
        elif d.task == 2:
            subject = 'Daily Update of Task 2.'
            receiver_email = d.email
            res = send_mail(subject, task2_tracker, sender_email, [receiver_email])
        elif d.task == 3:
            subject = 'Daily Update of Task 3.'
            receiver_email = d.email
            res = send_mail(subject, task3_tracker, sender_email, [receiver_email])
        elif d.task == 4:
            subject = 'Daily Update of Task 4.'
            receiver_email = d.email
            res = send_mail(subject, task4_tracker, sender_email, [receiver_email])

    daily_report.update(daily_updated=True)


@shared_task
def weekly_update(sender_email):
    weekly_report = Task.objects.filter(weekly_updated=False)
    task1_tracker = ''
    task2_tracker = ''
    task3_tracker = ''
    task4_tracker = ''
    for report in weekly_report:
        if report.task == 1:
            task1_tracker = task1_tracker + report.description + ' \n'
        elif report.task == 2:
            task2_tracker = task2_tracker + report.description + ' \n'
        elif report.task == 3:
            task3_tracker = task3_tracker + report.description + ' \n'
        elif report.task == 4:
            task4_tracker = task4_tracker + report.description + ' \n'

    update_type = UpdateType.objects.filter(duration='Weekly').first()
    weekly_update_list = TaskTracker.objects.filter(update_type=update_type.id)
    for d in weekly_update_list:
        if d.task == 1:
            subject = 'Weekly Update of Task 1.'
            receiver_email = d.email
            res = send_mail(subject, task1_tracker, sender_email, [receiver_email])
        elif d.task == 2:
            subject = 'Weekly Update of Task 2.'
            receiver_email = d.email
            res = send_mail(subject, task2_tracker, sender_email, [receiver_email])
        elif d.task == 3:
            subject = 'Weekly Update of Task 3.'
            receiver_email = d.email
            res = send_mail(subject, task3_tracker, sender_email, [receiver_email])
        elif d.task == 4:
            subject = 'Weekly Update of Task 4.'
            receiver_email = d.email
            res = send_mail(subject, task4_tracker, sender_email, [receiver_email])

    weekly_report.update(weekly_updated=True)


@shared_task
def monthly_update(sender_email):
    monthly_report = Task.objects.filter(monthly_updated=False)
    task1_tracker = ''
    task2_tracker = ''
    task3_tracker = ''
    task4_tracker = ''
    for report in monthly_report:
        if report.task == 1:
            task1_tracker = task1_tracker + report.description + ' \n'
        elif report.task == 2:
            task2_tracker = task2_tracker + report.description + ' \n'
        if report.task == 3:
            task3_tracker = task3_tracker + report.description + ' \n'
        if report.task == 4:
            task4_tracker = task4_tracker + report.description + ' \n'

    update_type = UpdateType.objects.filter(duration='Monthly').first()
    monthly_update_list = TaskTracker.objects.filter(update_type=update_type.id)
    for d in monthly_update_list:
        if d.task == 1:
            subject = 'Monthly Update of Task 1.'
            receiver_email = d.email
            res = send_mail(subject, task1_tracker, sender_email, [receiver_email])
        elif d.task == 2:
            subject = 'Monthly Update of Task 2.'
            receiver_email = d.email
            res = send_mail(subject, task2_tracker, sender_email, [receiver_email])
        elif d.task == 3:
            subject = 'Monthly Update of Task 3.'
            receiver_email = d.email
            res = send_mail(subject, task3_tracker, sender_email, [receiver_email])
        elif d.task == 4:
            subject = 'Monthly Update of Task 4.'
            receiver_email = d.email
            res = send_mail(subject, task4_tracker, sender_email, [receiver_email])

    monthly_report.update(monthly_updated=True)
