from datetime import datetime

from src.inputs import region, instances_ids, mid_day
from src.ec2 import EC2


def lambda_handler(event, context) -> tuple[dict[str, str], int]:
    ec2_instances: EC2 = EC2(region, instances_ids)
    current_time: str = datetime.now().strftime("%H:%M:%S")

    return ec2_instances.start() if current_time < mid_day else ec2_instances.stop()
