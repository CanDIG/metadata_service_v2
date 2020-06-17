from candig_metadata.metadata.backend import query_authorization_level


def resolve_field_factory(field_name):
    def resolve_field(*args, **kwargs):
        instance = args[0]
        info = args[1]
        tiered_field_name = f"{field_name}_tier"

        # TODO: retrieve tier value with some token or something
        # info.context.headers
        tier = query_authorization_level('token will be here', instance.dataset_id)

        if hasattr(instance, tiered_field_name):
            if tier >= getattr(instance, tiered_field_name):
                return getattr(instance, field_name)
            else:
                return None
        else:
            return getattr(instance, field_name)

    return resolve_field
