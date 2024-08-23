from characters.scraper import sync_characters_with_api

from celery import shared_task


@shared_task
def run_sync_with_appi() -> None:
    return sync_characters_with_api()
