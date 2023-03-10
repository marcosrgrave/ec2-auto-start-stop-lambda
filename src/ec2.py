import time
from http import HTTPStatus

import boto3


class EC2:
    """For now, single region support."""

    def __init__(self, region: str, instances_ids: tuple) -> None:
        self.instances: tuple[str] = instances_ids
        self.ec2 = boto3.client("ec2", region_name=region)

    def start(self) -> tuple[dict[str, str], int]:
        start_time: float = time.time()
        self.ec2.start_instances(InstanceIds=self.instances)
        total_time: float = time.time() - start_time

        return {"total_time": f"{total_time:.3f} seconds", "instances_started": str(self.instances)}, HTTPStatus.OK

    def stop(self) -> tuple[dict[str, str], int]:
        start_time: float = time.time()
        self.ec2.stop_instances(InstanceIds=self.instances)
        total_time: float = time.time() - start_time

        return {"total_time": f"{total_time:.3f} seconds", "instances_stopped": str(self.instances)}, HTTPStatus.OK
