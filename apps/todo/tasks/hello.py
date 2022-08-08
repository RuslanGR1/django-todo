import logging

from celery import shared_task


@shared_task
def hello():
    """Hello periodic task"""
    logging.error('Hello task')
    logger = logging.getLogger(__name__)
    logger.debug('debug Exception')
    logger.info('info Exception')
    logger.warning('warning Exception')
    logger.error('error Exception')
