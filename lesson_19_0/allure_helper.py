import allure


def attach_json(data, name):
    allure.attach(
        data,
        name=name,
        attachment_type=allure.attachment_type.JSON,
    )