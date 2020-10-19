from django.db import models


def get_default_action_status():
    """ get a default value for action status; create new status if not available """
    return ActionStatus.objects.get_or_create(name="created")[0]


def get_default_action_result():
    """ get a default value for result status; create new result if not available """
    return ActionResult.objects.get_or_create(name="unknown")[0]


class ActionStatus(models.Model):
    """ table to track statuses of actions, such as 'created', 'started', 'completed', etc. """
    name = models.CharField(max_length=16, unique=True)


class ActionResult(models.Model):
    """ table to track results of actions, such as 'passed', 'failed', 'unknown', etc. """
    name = models.CharField(max_length=16, unique=True)


class Action(models.Model):
    """ table to track individual actions """
    name = models.CharField(max_length=16, unique=True)
    status = models.ForeignKey(ActionStatus, default=get_default_action_status, on_delete=models.CASCADE)
    result = models.ForeignKey(ActionResult, default=get_default_action_result, on_delete=models.CASCADE)
