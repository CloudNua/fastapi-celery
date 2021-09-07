import json

from fastapi import WebSocket

from . import ws_router
from project import broadcast
from project.celery_utils import get_task_info


@ws_router.websocket("/ws/task_status/{task_id}")
async def ws_task_status(websocket: WebSocket):
    await websocket.accept()

    task_id = websocket.scope["path_params"]["task_id"]

    async with broadcast.subscribe(channel=task_id) as subscriber:
        # just in case the task already finish
        data = get_task_info(task_id)
        await websocket.send_json(data)

        async for event in subscriber:
            await websocket.send_json(json.loads(event.message))


async def update_celery_task_status(task_id: str):
    """
    This function is called by Celery worker in task_postrun signal handler
    """
    await broadcast.connect()
    await broadcast.publish(
        channel=task_id,
        message=json.dumps(get_task_info(task_id))  # RedisProtocol.publish expect str
    )
    await broadcast.disconnect()