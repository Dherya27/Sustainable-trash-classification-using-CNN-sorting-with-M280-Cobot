from setuptools import setup

package_name = 'robot_vision'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='whitchurch',
    maintainer_email='neoblackcyptron@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
    "generic_publisher = robot_vision.generic_publisher:main",
    "generic_subscriber = robot_vision.generic_subscriber:main",
    "camera_publisher = robot_vision.camera_publisher:main",
    "camera_subscriber = robot_vision.camera_subscriber:main",
    "camera_subscriberResnet50 = robot_vision.camera_subscriberResnet50:main",
    "generic_service = robot_vision.generic_service:main",
    "generic_serviceclient = robot_vision.generic_serviceclient:main",
    "visionrobot_serviceclient = robot_vision.visionrobot_service:main",
    "detection_node= robot_vision.detection_node:main",
    "detection_node_v1= robot_vision.detection_node_v1:main"


        ],
    },
)
